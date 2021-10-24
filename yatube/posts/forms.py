from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'group', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        required=False,
        label="Имя",
        help_text="Ваше имя",
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(
        required=False,
        label="Email",
        help_text="Ваш Email",
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    to = forms.EmailField(
        label="Куда",
        help_text="Email кому отправляем сообщение")
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="Сообщение",
        help_text="Текст сообщения")


class SearchPostForm(forms.Form):
    text = forms.CharField(
        max_length=25,
        label="Поиск",
        help_text="Поиск")
