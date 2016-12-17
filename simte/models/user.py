"""
Users models
"""

import logging

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class Department(models.Model):
    """
    Department
    """

    name = models.CharField(max_length=256,
                            null=True,
                            blank=True,
                            verbose_name=_('Name'))

    def __unicode__(self):
        return "{}".format(self.name)


class Profession(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    class Meta:
        abstract = True


class Administrator(Profession):
    """
    Administrator
    """

    def __unicode__(self):
        return "Administrator {}".format(self.user.username)


class Manager(Profession):
    """
    Manager
    """

    department = models.ForeignKey('Department',
                                   verbose_name=_('Equipment'))

    def __unicode__(self):
        return "Manager {}".format(self.user.username)


def Technician(Profession):
    """
    Technician
    """
    department = models.ForeignKey('Department',
                                   verbose_name=_('Equipment'))

    def __unicode__(self):
        return "Tech {}".format(self.user.username)
