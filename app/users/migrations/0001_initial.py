# Generated by Django 3.2.8 on 2023-06-03 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Dialog'), ('C', 'Chat')], default='D', max_length=1, verbose_name='Тип')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Информация о себе', max_length=500, verbose_name='О себе')),
                ('genre', models.CharField(choices=[('m', 'Мужчина'), ('w', 'Женщина')], max_length=1, null=True)),
                ('location', models.CharField(blank=True, help_text='Страна проживания', max_length=30, verbose_name='Местоположение')),
                ('birth_date', models.DateField(blank=True, help_text='Ваша дата рождения (ГГГГ-ММ-ДД)', null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(blank=True, help_text='Ваша фотография', null=True, upload_to='avatars/', verbose_name='Фото')),
                ('last_online', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=600, verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.chat', verbose_name='Чат')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['pub_date'],
            },
        ),
    ]
