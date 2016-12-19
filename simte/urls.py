"""
URLs dispatcher
"""

import logging
from django.conf.urls import url
from . import views

logger = logging.getLogger(__name__)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'inspection_list/$', views.InspectionListView.as_view(), name="inspection_list"),
    url(r'inspection/(?P<pk>[0-9]+)/$', views.InspectionEditView.as_view(), name="inspection"),
    url(r'inspection/add/$', views.InspectionCreateView.as_view(), name="inspection_add"),
    url(r'equipment_list/$', views.EquipmentListView.as_view(), name="equipment_list"),
    url(r'equipment/(?P<pk>[0-9]+)/$', views.EquipmentEditView.as_view(), name="equipment"),
    url(r'equipment/add/$', views.EquipmentCreateView.as_view(), name="equipment_add"),
]
