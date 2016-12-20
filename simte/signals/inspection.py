"""
Inspection signals
"""

import json
import requests
import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from simte.models import Inspection

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Inspection)
def reserve_equip(sender, instance, created, **kwargs):

    equip_id = instance.equipment.id
    start_date = instance.equipment.start_date
    end_date = instance.equipment.end_date

    if not created:

        headers = {'content-type': 'application/json'}
        auth_param = getattr(settings, 'AGENDAMENTO_PARAM', None)
        url = getattr(settings, 'AGENDAMENTO_URL', None)

        url += "api/recursos/{}/cancelar_agendamento".format(equip_id)
        data = {
            "agendamento": {
                "intervalo": {
                    "inicio": start_date.isoformat()
                    "fim": end_date.isoformat()
                }
            }
        }

        logger.debug("Desagendando {}: {}".format(equip_id, start_date.isoformat()))
        requests.post(url=url, headers=headers, params=auth_param, data=json.dumps(data))

    headers = {'content-type': 'application/json'}
    auth_param = getattr(settings, 'AGENDAMENTO_PARAM', None)
    url = getattr(settings, 'AGENDAMENTO_URL', None)


    if end_date:
        url += "api/recursos/{}/agendamentos".format(equip_id)
        data = {
            "agendamento": {
                "intervalo": {
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

    logger.debug("Agendando {}: {}".format(equip_id, start_date.isoformat()))
    requests.post(url=url, headers=headers, params=auth_param, data=json.dumps(data))
