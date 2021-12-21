from operator import itemgetter

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from posts.models import Comment, Group, Post

User = get_user_model()


def year(request):
    return {'year': timezone.now()}


@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()


@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()


def aside(request):
    all_posts = Post.objects.all()[:settings.NUMBER_POST]
    groups = Group.objects.all()[:settings.NUMBER_POST]
    # users = User.objects.all().order_by('id')[:settings.NUMBER_POST]
    users = [
        (user, user.posts.count())
        for user in User.objects.filter(
            is_active=True).select_related('profile')
        if user.posts.count() > 0]
    users = reversed(sorted(users[:5], key=itemgetter(1)))
    comments = Comment.objects.all().select_related(
        'post')[:settings.NUMBER_POST]
    return {
        'all_posts': all_posts,
        'groups': groups,
        'users': users,
        'comments': comments
    }
