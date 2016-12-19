"""
Helper functions
"""

import json
import requests

from django.conf import settings

def get_reserved_dates(equip):

    headers = {'content-type': 'application/json'}
    url = getattr(settings, 'AGENDAMENTO_URL', None)
    url += "/recursos/{}/agendamentos".format(equip.id)

    response = requests.get(url=url, headers=headers)
    data = json.load(response.json())

    periodos = data["agendamento"]["periodo"]
    occupied = [(periodo['inicio'], periodo['fim']) for periodo in periodos]
    return occupied
