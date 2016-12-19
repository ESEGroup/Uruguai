"""
Django Admin customizations
"""

from django.contrib import admin
from simte.models import (Inspection, Equipment, Piece, Department,
                          Administrator, Manager, Technician)

admin.site.register(Equipment)
admin.site.register(Piece)
admin.site.register(Inspection)
admin.site.register(Department)
admin.site.register(Administrator)
admin.site.register(Manager)
admin.site.register(Technician)
