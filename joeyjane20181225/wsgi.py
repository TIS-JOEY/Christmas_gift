"""
WSGI config for joeyjane20181225 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joeyjane20181225.settings')

application = get_wsgi_application()

## mysite/wsgi.py

from dj_static import Cling
application = Cling(get_wsgi_application())
