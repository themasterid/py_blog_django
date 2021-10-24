from django.urls import path

from . import views
from .views import SearchResultsView

app_name = 'posts'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('posts/<int:post_id>/share/', views.post_share, name='post_share'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='delete'),
    path('create/', views.post_create, name='create'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'posts/<int:post_id>/add_comment/',
        views.add_comment, name='add_comment'),
    path(
        'posts/<int:post_id>/<int:comment_id>/delete_comment/',
        views.delete_comment, name='delete_comment'),
    path('follow/', views.follow_index, name='follow_index'),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name="profile_unfollow"
    ),
    path('like/<int:post_id>/', views.get_post_like, name="post_like"),
]
