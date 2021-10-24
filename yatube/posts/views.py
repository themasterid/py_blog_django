# from operator import itemgetter

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from users.models import Profile

from .forms import CommentForm, EmailPostForm, PostForm
from .models import Comment, Follow, Group, Ip, Post

User = get_user_model()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


@login_required
def get_post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('posts:post_detail', post_id)


class SearchResultsView(ListView):
    model = Post
    template_name = 'posts/search_results.html'
    paginate_by = settings.NUMBER_POST

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(text__icontains=query) | Q(title__icontains=query)
        ).filter(status=True)


def get_paginator(request, req):
    paginator = Paginator(
        req,
        settings.NUMBER_POST
    )
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    page_obj = get_paginator(
        request,
        Post.objects.select_related('author', 'group').filter(status=True))
    template = 'posts/index.html'
    context = {'page_obj': page_obj}
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    page_obj = get_paginator(
        request,
        group.posts.select_related(
            'author').filter(group=group, status=True))
    context = {
        'group': group,
        'page_obj': page_obj}
    return render(
        request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    if request.user == author:
        page_obj = get_paginator(
            request,
            author.posts.select_related(
                'author').filter(author=author))
    if request.user != author:
        page_obj = get_paginator(
            request,
            author.posts.select_related(
                'author').filter(author=author, status=True))
    profile = get_object_or_404(
        Profile.objects.select_related('user'),
        user=author)
    following = request.user.is_authenticated
    if following:
        following = author.following.filter(user=request.user).exists()
    template = 'posts/profile.html'
    context = {
        'page_obj': page_obj,
        'author': author,
        'following': following,
        'profile': profile}
    return render(request, template, context)


def post_detail(request, post_id):
    likes_connected = get_object_or_404(
        Post, id=post_id)
    post_is_liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        post_is_liked = True
    post = get_object_or_404(Post, id=post_id)
    profile = get_object_or_404(Profile, user=post.author)
    comments_details = post.comments.all()
    form = CommentForm()
    author = get_object_or_404(User, username=post.author)
    following = request.user.is_authenticated
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        post.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.views.add(Ip.objects.get(ip=ip))

    if following:
        following = author.following.filter(user=request.user).exists()
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'requser': request.user,
        'author': post.author,
        'form': form,
        'profile': profile,
        'comments_details': comments_details,
        'following': following,
        'post_is_liked': post_is_liked,
    }
    return render(request, template, context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = Comment.objects.get(pk=comment_id)
    if request.user != user.author:
        return redirect('posts:post_detail', post_id)
    comment.delete()
    return redirect('posts:post_detail', post_id)


@login_required
def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None)
    if form.is_valid():
        create_post = form.save(commit=False)
        create_post.author = request.user
        create_post.save()
        cache.clear()
        return redirect('posts:profile', create_post.author)
    template = 'posts/create_post.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post)
    if form.is_valid():
        form.save()
        cache.clear()
        return redirect('posts:post_detail', post_id)
    template = 'posts/create_post.html'
    context = {
        'form': form,
        'post': post,
        'is_edit': True}
    return render(request, template, context)


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    post.delete()
    cache.clear()
    return redirect('posts:profile', post.author)


@login_required
def follow_index(request):
    page_obj = get_paginator(
        request,
        Post.objects.filter(author__following__user=request.user))
    template = 'posts/follow.html'
    context = {'page_obj': page_obj}
    return render(request, template, context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('posts:profile', author)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    profile_follow = Follow.objects.filter(
        user=request.user, author=author).select_related('user')
    if profile_follow.exists():
        profile_follow.delete()
    return redirect('posts:profile', username=username)


'''
@login_required
def profile_unfollow(request, username):
    user_follower = get_object_or_404(
        Follow,
        user=request.user,
        author__username=username
    )
    if user_follower.exists():
        user_follower.delete()
    return redirect('posts:profile', username)
'''


@login_required
def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=True)
    send = False
    user_name = f'{request.user.first_name} {request.user.last_name}'
    user_email = request.user.email
    if request.method == 'GET':
        data = {
            'name': user_name,
            'email': user_email,
            'to': user_email}
        form = EmailPostForm(data)
        return render(
            request, 'posts/share.html', {'post': post, 'form': form})
    form = EmailPostForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['comments'] == '':
            cd['comments'] = '---пусто---'
        post_url = f'https://themasterid.pythonanywhere.com/posts/{post_id}/'
        # post_url = request.build_absolute_uri(post.get_absolute_url())
        subject = '{} ({}) рекоменду прочитать "{}"'.format(
            cd['name'], cd['email'], post.title)
        message = 'Прочти "{}" на {}\n\n{} оставил комментарий: {}'.format(
            post.title, post_url, cd['name'], cd['comments'])
        send_mail(subject, message, 'thebrootos@gmail.com', [cd['to']])
        send = True
        return render(
            request,
            'posts/share.html',
            {'post': post, 'form': form, 'send': send, 'post_url': post_url})
    form = EmailPostForm()
    return render(
        request,
        'posts/share.html',
        {'post': post, 'form': form, 'send': send})
