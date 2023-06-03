from django.contrib import admin
from django.utils.html import mark_safe

from .models import Message, Profile


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'get_text',
        'pub_date',
        'is_readed'
    )

    def get_text(self, obj):
        return obj.message[:100]

    get_text.short_description = 'Сообщение'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'location',
        'birth_date',
        'get_image',
    )
    # list_editable = ('bio',)
    search_fields = ('location',)
    list_filter = ('birth_date',)
    empty_value_display = '-пусто-'
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.avatar == '':
            obj.avatar = 'avatars/no_photo.png'
        return mark_safe(
            f'<img src={obj.avatar.url} width="20%"')

    get_image.short_description = 'Аватар'
