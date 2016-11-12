"""
Django Admin customizations
"""

from django.contrib import admin
from simte.models import Equipment, Piece

admin.site.register(Equipment)
admin.site.register(Piece)
