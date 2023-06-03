from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Comment, Follow, Group, Ip, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'pub_date',
        'author',
        'group',
        'get_image',
        'status',
    )
    # fields = ['likes']
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.image == '':
            obj.image = 'posts/no_photo.png'
        return mark_safe(
            f'<img src={obj.image.url} width="20%"')

    get_image.short_description = 'Картинка'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('slug',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text_safe', 'created', 'active')
    list_filter = ('active', 'text', 'created', 'updated')
    search_fields = ('post', 'author', 'text')

    def text_safe(self, obj):
        return mark_safe(obj.text)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    list_filter = ('user', 'author')
    search_fields = ('user', 'author')


admin.site.register(Ip)
admin.site.site_title = 'DJANGO PYBLOG'
admin.site.site_header = 'DJANGO PYBLOG'
