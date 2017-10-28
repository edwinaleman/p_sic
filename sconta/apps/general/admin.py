# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TipoCuenta)
admin.site.register(GrupoCuenta)
admin.site.register(Cuenta)
admin.site.register(PeriodoContable)
admin.site.register(LibroMayor)
admin.site.register(Diario)
admin.site.register(DocLibro)