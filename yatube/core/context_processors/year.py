from operator import itemgetter

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from posts.models import Comment, Group, Post

User = get_user_model()


def year(request):
    return {'year': timezone.now()}


def aside(request):
    all_posts = Post.objects.all()[:settings.NUMBER_POST]
    groups = Group.objects.all()[:settings.NUMBER_POST]
    users = [
        (user, user.posts.count())
        for user in User.objects.filter(
            is_active=True).select_related('profile')
        if user.posts.count() > 0]
    users = reversed(sorted(users[:settings.NUMBER_POST], key=itemgetter(1)))
    comments = Comment.objects.all().select_related(
        'post')[:settings.NUMBER_POST]
    return {
        'all_posts': all_posts,
        'groups': groups,
        'users': users,
        'comments': comments
    }
