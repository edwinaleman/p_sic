# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout # Login/out Usuario

# Create your views here.

#Vista de pruebas
def test(request):
	return render(request, 'inicio.html')

#Vista para cerrar sesion
def logout_view(request):
    logout(request)
    return redirect('usuario:test')

