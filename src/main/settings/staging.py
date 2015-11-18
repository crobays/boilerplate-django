from base import *
import os

# Speed up templates
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# Optimize thumbnails for production
INSTALLED_APPS += (
    'easy_thumbnails.optimize',
)

# Save sessions in cache
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'
