#!/usr/bin/env python
import os
import sys

os.environ.setdefault('APP_NAME', 'main')
os.environ.setdefault('APPLICATION_ENV', 'production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings.{}'.format(os.environ.get('APP_NAME'), os.environ.get('APPLICATION_ENV')))

if __name__ == "__main__":

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
