from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, View

from .forms import CreationForm, MessageForm, ProfileForm, UserForm
from .models import Chat


class DialogsView(LoginRequiredMixin, View):
    def get(self, request):
        user_chats = Chat.objects.filter(members__in=[request.user.id])
        template_name = 'users/dialogs.html'
        context = {
            'user_profile': request.user,
            'chats': user_chats
        }
        return render(request, template_name, context)


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(
            members__in=[request.user.id, user_id],
            type=Chat.DIALOG).annotate(
                c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(
            reverse(
                'users:messages',
                kwargs={'chat_id': chat.id}))


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(
                    is_readed=False).exclude(
                        author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            'users/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


@login_required
@transaction.atomic
def update_profile(request):
    user_form = UserForm(
        request.POST or None,
        instance=request.user)
    profile_form = ProfileForm(
        request.POST or None,
        files=request.FILES or None,
        instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('posts:profile', request.user)
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
