"""
Inspection signals
"""

import json
import requests

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from simte.models import Inspection


@receiver(post_save, sender=Inspection)
def reserve_equip(sender, instance, created, **kwargs):

    equip_id = instance.equipment.id
    start_date = instance.equipment.start_date
    end_date = instance.equipment.end_date

    if not created:

        headers = {'content-type': 'application/json'}
        url = getattr(settings, 'AGENDAMENTO_URL', None)

        url += "/recursos/{}/remover_agendamento".format(equip_id)
        data = {
            "agendamento": {
                "inicio": start_date.isoformat()
            }
        }

        requests.post(url=url, headers=headers, data=json.dumps(data))

    headers = {'content-type': 'application/json'}
    url = getattr(settings, 'AGENDAMENTO_URL', None)


    if end_date:
        url += "/recursos/{}/agendamentos".format(equip_id)
        data = {
            "agendamento": {
                "periodo": {
                    "inicio": start_date.isoformat(),
                    "fim": end_date.isoformat()
                }
            }
        }

    else:
        url += "/recursos/{}/estado".format(equip_id)
        data = {
            "utilizavel": False
        }

    requests.post(url=url, headers=headers, data=json.dumps(data))
