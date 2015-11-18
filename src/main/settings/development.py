from base import *
import os

# Turn on debug mode
DEBUG = TEMPLATE_DEBUG = True
DEBUG_TOOLBAR = True
PROFILING = True

def custom_show_toolbar(self):
    return True

DEBUG_TOOLBAR_CONFIG = {}
jquery = os.path.join(STATIC_URL, 'bower_components/jquery/dist/jquery.js')
if os.path.exists(os.path.join(BASE_DIR, jquery)):
    DEBUG_TOOLBAR_CONFIG['JQUERY_URL'] = jquery

# Add debug toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
) + MIDDLEWARE_CLASSES


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

if PROFILING:
    INSTALLED_APPS += (
        'debug_toolbar_line_profiler',
    )

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar_line_profiler.panel.ProfilingPanel'
    ]

INTERNAL_IPS = ('127.0.0.1',)

# Fake cache for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Media and static setup
# MEDIA_URL = '/media/'
# STATIC_URL = '/static/'

# temp disable emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# import logging
# l = logging.getLogger('django.db.backends')
# l.setLevel(logging.DEBUG)
# l.addHandler(logging.StreamHandler())
#
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         },
#     }
# }