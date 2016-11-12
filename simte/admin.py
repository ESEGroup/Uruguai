"""
Django Admin customizations
"""

from django.contrib import admin
from simte.models import (Inspection, Equipment, Piece)

admin.site.register(Equipment)
admin.site.register(Piece)
admin.site.register(Inspection)
