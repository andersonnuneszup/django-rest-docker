from django.urls import re_path

from djangostack.viewsets import AboutViewSet

app_name = 'djangostack'

urlpatterns = [
    re_path(r'^about/?$', AboutViewSet.as_view({'get': 'about'}), name='about'),
]