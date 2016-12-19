"""
Shortcut functions
"""

from simte.models import Equipment, Administrator, Technician, Manager

def get_user_equips(user):
    job = None
    if hasattr(user, 'technician'):
        job = user.technician
    if hasattr(user, 'manager'):
        job = user.manager
    if hasattr(user, 'administrator'):
        job = user.administrator

    equips = [equip for equip in Equipment.objects.all() if equip.department is None]
    if isinstance(job, Technician) or isinstance(job, Manager):
        equips += list(Equipment.objects.filter(department=job.department))
    if isinstance(job, Administrator):
        equips = list(Equipment.objects.all())

    return equips
