import os
from pathlib import Path

import environ

env = environ.Env()

environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

EMAILHOST_PASSWORD = env(
    'EMAILHOST_PASSWORD',
    default="test@test.test")

EMAILHOST_USER = env(
    'EMAILHOST_USER',
    default="1234")

SECRET_KEY = env(
    'SECRET_KEY',
    default="unsafe-secret-key-1234QWERTYqwerty")

DEBUG = env(
    'DEBUG',
    default='True'
) == 'True'

CSRF_FAILURE_VIEW = 'core.views.csrf_failure'

ALLOWED_HOSTS = env(
    'ALLOWED_HOSTS',
    default='localhost').split(', ')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

EMAIL_HOST = 'smtp.gmail.com'

# EMAIL_HOST_USER = EMAILHOST_USER

# EMAIL_HOST_PASSWORD = EMAILHOST_PASSWORD

EMAIL_PORT = 587

EMAIL_USE_TLS = True

LOGIN_URL = 'users:login'

LOGIN_REDIRECT_URL = 'posts:index'

# LOGOUT_REDIRECT_URL = 'posts:index'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sorl.thumbnail',
    'users.apps.UsersConfig',
    # 'debug_toolbar',
    'posts.apps.PostsConfig',
    'about.apps.AboutConfig',
    'core.apps.CoreConfig',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'py_blog.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',
                'core.context_processors.year.aside',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-cache'
    }
}

WSGI_APPLICATION = 'py_blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': env(
#             'DB_ENGINE',
#             default='django.db.backends.postgresql'),
#         'NAME': env(
#             'POSTGRES_DB'),
#         'USER': env(
#             'POSTGRES_USER',
#             default='postgres'),
#         'PASSWORD': env(
#             'POSTGRES_PASSWORD',
#             default='postgres'),
#         'HOST': env(
#             'DB_HOST',
#             default='localhost'),
#         'PORT': env(
#             'DB_PORT',
#             default='5432')
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth'
        '.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
        'password_validation.NumericPasswordValidator',
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd E Y'

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

NUMBER_POST = 5

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / STATIC_URL]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'codeSnippet_languages': {
            'html': 'HTML',
            'css': 'CSS',
            'javascript': 'JavaScript',
            'python': 'Python',
            'php': 'PHP',
            'go': 'Golang',
            'bash': 'BASH',
        },
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat', 'CodeSnippet']},
            {'name': 'paragraph', 'items': [
                'NumberedList',
                'BulletedList',
                '-', 'Outdent',
                'Indent',
                '-',
                'Blockquote',
                'CreateDiv',
                '-',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock',
                '-',
                'BidiLtr',
                'BidiRtl',
            ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Youtube', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            {'name': 'tools', 'items': ['Maximize', ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'height': 300,
        'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True,
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'youtube',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'codesnippet',
            'elementspath'
        ]),
    }
}

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

AWS_QUERYSTRING_AUTH = False
