"""
Helper functions
"""

import json
import requests
import logging

from django.conf import settings
from django.utils.dateparse import parse_datetime

logger = logging.getLogger(__name__)

def get_reserved_dates(equip):

    headers = {'content-type': 'application/json'}
    auth_param = getattr(settings, 'AGENDAMENTO_PARAM', None)
    url = getattr(settings, 'AGENDAMENTO_URL', None)
    url += "api/recursos/{}".format(equip.id)

    try:
        response = requests.get(url=url, params=auth_param, headers=headers)
    except Exception as e:
        logger.error(e)
        return None

    data = response.json()
    logger.debug(data)

    occupied = []

    agendamentos = data["recurso"]["agendamentos"]
    for agendamento in agendamentos:
        occupied += [(parse_datetime(agendamento['intervalo']['inicio']), parse_datetime(agendamento['intervalo']['fim']))]

    return occupied
