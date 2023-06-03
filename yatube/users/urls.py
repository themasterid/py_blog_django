from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('update/', views.update_profile, name='update_profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('logout/', LogoutView.as_view(
        template_name='users/logged_out.html'), name='logout'),

    path('login/', LoginView.as_view(
        template_name='users/login.html'), name='login'),

    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change_form.html'),
        name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html'),
        name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path(
        'dialogs/',
        login_required(views.DialogsView.as_view()),
        name='dialogs'),
    path(
        'dialogs/create/<int:user_id>/',
        login_required(views.CreateDialogView.as_view()),
        name='create_dialog'),
    path(
        'dialogs/<int:chat_id>/',
        login_required(views.MessagesView.as_view()),
        name='messages'),
]
