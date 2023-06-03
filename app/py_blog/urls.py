from ckeditor_uploader import views as ckeditor_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='index')),
    path('about/', include('about.urls', namespace='about')),
    path('ckeditor/upload/', login_required(
        ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(
        login_required(ckeditor_views.browse)), name='ckeditor_browse'),
]


if settings.DEBUG:
    import mimetypes

    import debug_toolbar

    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
