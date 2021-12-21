from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

DATE_FORMAT = "%d.%m.%Y"


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(
        User,
        verbose_name='Участник')

    def get_absolute_url(self):
        return reverse('users:messages', args=[self.pk])


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name="Чат")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь")
    message = models.TextField(
        max_length=600,
        verbose_name="Сообщение")
    pub_date = models.DateTimeField(
        verbose_name='Дата сообщения',
        default=timezone.now)
    is_readed = models.BooleanField(
        verbose_name='Прочитано',
        default=False)

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.message


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='О себе',
        help_text='Информация о себе')
    location = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Местоположение',
        help_text='Страна проживания')
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
        help_text='Ваша дата рождения')
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Фото',
        help_text='Ваша фотография')
    last_online = models.DateTimeField(
        blank=True,
        null=True)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

    def __str__(self):
        return str(self.user)

    def is_online(self):
        if self.last_online:
            time_delta = timezone.timedelta(minutes=60)
            time_now = timezone.now() - self.last_online
            return time_now < time_delta
        return False

    def get_online_info(self):
        if self.is_online():
            return _('Онлайн')
        if self.last_online:
            date = self.last_online.date().strftime(DATE_FORMAT)
            return _(f'Последний визит {date}')
        return _('Неизвестно')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    try:
        user = Profile.objects.get(pk=instance.pk)
        user.last_online = timezone.now()
        user.save(update_fields=['last_online'])
        instance.profile.save()
        return user
    except User.DoesNotExist:
        return None


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
