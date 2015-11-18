"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('APP_NAME', 'main')
os.environ.setdefault('APPLICATION_ENV', 'production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings.{}'.format(os.environ.get('APP_NAME'), os.environ.get('APPLICATION_ENV'))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
