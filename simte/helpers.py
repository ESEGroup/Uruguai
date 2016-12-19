"""
Helper functions
"""

import json
import requests
import logging

from django.conf import settings

logger = logging.getLogger(__name__)

def get_reserved_dates(equip):
    return None

    headers = {'content-type': 'application/json'}
    url = getattr(settings, 'AGENDAMENTO_URL', None)
    url += "/recursos/{}/agendamentos".format(equip.id)

    try:
        response = requests.get(url=url, headers=headers)
    except Exception as e:
        logger.error(e)
        return None

    data = json.load(response.json())
    periodos = data["agendamento"]["periodo"]
    occupied = [(periodo['inicio'], periodo['fim']) for periodo in periodos]
    return occupied
