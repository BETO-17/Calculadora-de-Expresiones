"""
WSGI config for calculadora_django project.

This file exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
from django.core.wsgi import get_wsgi_application

# Define la configuración por defecto del entorno de Django
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'calculadora_django.settings'
)

# Crea y expone la aplicación WSGI que será utilizada por el servidor
application = get_wsgi_application()
