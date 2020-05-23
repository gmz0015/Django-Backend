"""
WSGI config for initial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys, django

from django.core.wsgi import get_wsgi_application
# from django.core.handlers.wsgi import  WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'initial.settings')

application = get_wsgi_application()

# django.setup()     #避免在虚拟环境下找不到django的app
#
# application = WSGIHandler()  #实例化一个WSGI application用作接受nginx服务器传递的envrion、start_response参数
