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
        ('A', _('Available')),
        ('U', _('Unavailable'))
    )

    eq_type = models.CharField(max_length=256,
                               blank=True,
                               null=True,
                               verbose_name=_('Type'))
    serial_number = models.CharField(max_length=256,
                                     null=True,
                                     blank=True,
                                     verbose_name=_('Serial Number'))
    department = models.ForeignKey('Department',
                                   null=True,
                                   blank=True,
                                   verbose_name=_('Department'))
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default='A',
                              verbose_name=_('Status'))

    def occupied_dates(self, excluding_inspection=None):
        """
        Return a sorted list containing date pairs (start & end dates) with occupied dates.
        End date is not mandatory, in this case we consider that the equip will be unavailable
        for an undetermined amount of time.
        If excluding_inspection is defined it will not count as occupied, usefull for editing
        inspection.

        return eg: [(10/11/2016Z14:00, 11/11/2016Z8:00), (22/12/2016Z10:00, None)]
        """
        inspections = self.inspection_set.all().order_by('start_date')

        if excluding_inspection:
            inspections = [insp for insp in inspections if insp != excluding_inspection]

        result = []
        for inspec in inspections:
            result.append((inspec.start_date, inspec.end_date))
        return result


    def is_available(self, start_date, end_date=None, excluding_inspection=None):
        """
        Return true if equip is available in range date.
        If excluding_inspection is defined it will not count as occupied, usefull for editing
        inspection.

        (kind of Skyline problem)
        """
        occupied_dates = self.occupied_dates(excluding_inspection)

        for dates in occupied_dates:
            if end_date == None and start_date < dates[0]:
                return False

            if dates[1] == None and start_date > dates[0]:
                return False

            if end_date == None or dates[1] == None:
                pass

            if start_date > dates[0] and start_date < dates[1]:
                return False

            if end_date > dates[0] and end_date < dates[1]:
                return False

        return True

    def __unicode__(self):
        return "{}: {}".format(self.eq_type, self.serial_number)


class Piece(models.Model):
    """
    Equipment's piece
    """

    equipment = models.ForeignKey('Equipment',
                                  verbose_name=_('Equipment'))

    pc_type = models.CharField(max_length=256,
                               blank=True,
                               null=True,
                               verbose_name=_('Type'))

    serial_number = models.CharField(max_length=256,
                                     blank=True,
                                     null=True,
                                     verbose_name=_('Serial Number'))

    def __unicode__(self):
        return "{}: {}".format(self.pc_type, self.serial_number)
