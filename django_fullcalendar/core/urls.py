from django.urls import path

from django_fullcalendar.core.views import all_events as core_all_events
from django_fullcalendar.core.views import index as core_index

app_name = 'core'

urlpatterns = [
    path('', core_index, name='core_index'),
    path('all_events/', core_all_events, name='core_all_events'),
]
