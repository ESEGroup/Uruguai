"""
Equipments models
"""

import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class Equipment(models.Model):
    """
    Equipment
    """
    STATUS_CHOICES = (
        ('av', _('Available')),
        ('na', _('Not Available'))
    ),

    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default='av',
                              verbose_name=_('Status'))
    eq_type = models.CharField(max_length=256,
                               null=True,
                               blank=True,
                               verbose_name=_('Type'))
    serial_number = models.CharField(max_length=256,
                                     null=True,
                                     blank=True,
                                     verbose_name=_('Serial Number'))

class Piece(models.Model):
    """
    Equipment's piece
    """

    equipment = models.ForeignKey('Equipment')

    pc_type = models.CharField(max_length=256,
                               null=True,
                               blank=True,
                               verbose_name=_('Type'))

    serial_number = models.CharField(max_length=256,
                                     null=True,
                                     blank=True,
                                     verbose_name=_('Serial Number'))
