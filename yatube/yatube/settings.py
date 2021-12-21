import os

# from .secret_email import EMAILHOST_PASSWORD, EMAILHOST_USER

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open('yatube/secret_settings.txt') as f:
    SECRET_KEY = f.read().strip()

DEBUG = True

CSRF_FAILURE_VIEW = 'core.views.csrf_failure'

ALLOWED_HOSTS = [
    'themasterid.pythonanywhere.com',
    '*',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

'''
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = EMAILHOST_USER

EMAIL_HOST_PASSWORD = EMAILHOST_PASSWORD

EMAIL_PORT = 587

EMAIL_USE_TLS = True
'''

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
    'debug_toolbar',
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'yatube.urls'

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
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': os.path.join(BASE_DIR, 'yatube_cache/')
    }
}

WSGI_APPLICATION = 'yatube.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd E Y'

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

NUMBER_POST = 5

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'basicstyles', 'items': ['CodeSnippet', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
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
            'codesnippet',
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
            'elementspath'
        ]),
    }
}

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

AWS_QUERYSTRING_AUTH = False
