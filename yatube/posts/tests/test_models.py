from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Comment, Follow, Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            text='Тестовый текст больше 15 символов для проверки...',
            author=cls.user,
        )

    def test_post_str(self):
        """Проверка __str__ у post."""
        self.assertEqual(self.post.text[:15], str(self.post))

    def test_post_verbose_name(self):
        """Проверка verbose_name у post."""
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группа', }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.post._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)

    def test_post_help_text(self):
        """Проверка help_text у post."""
        feild_help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост', }
        for value, expected in feild_help_texts.items():
            with self.subTest(value=value):
                help_text = self.post._meta.get_field(value).help_text
                self.assertEqual(help_text, expected)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_group_str(self):
        """Проверка __str__ у group."""
        self.assertEqual(self.group.title, str(self.group))

    def test_group_verbose_name(self):
        """Проверка verbose_name у group."""
        field_verboses = {
            'title': 'Заголовок',
            'slug': 'ЧПУ',
            'description': 'Описание',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.group._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)


class FollowModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user1 = User.objects.create_user(username='auth1')
        cls.user2 = User.objects.create_user(username='auth2')
        cls.follow = Follow.objects.create(
            user=cls.user1,
            author=cls.user2,
        )

    def test_follow_str(self):
        """Проверка __str__ у follow."""
        self.assertEqual(
            f'{self.follow.user} подписался на {self.follow.author}',
            str(self.follow))

    def test_follow_verbose_name(self):
        """Проверка verbose_name у follow."""
        field_verboses = {
            'user': 'Пользователь',
            'author': 'Автор',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.follow._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            text='Тестовый пост',
            author=cls.user,
        )
        cls.comment = Comment.objects.create(
            text='Комментарий для поста',
            author=cls.user,
            post=cls.post,
        )

    def test_сomment_str(self):
        """Проверка __str__ у сomment."""
        self.assertEqual(self.comment.text[:15], str(self.comment))

    def test_сomment_verbose_name(self):
        """Проверка verbose_name у сomment."""
        field_verboses = {
            'post': 'Пост',
            'author': 'Автор',
            'text': 'Коментарий',
            'created': 'Создан',
            'updated': 'Обнавлен',
            'active': 'Активен',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.comment._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)
