from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^inicio$', test, name='test'), # URL de prueba
    url(r'^session_logout$', logout_view, name='pag_logout'), # Login/out Usuario
]