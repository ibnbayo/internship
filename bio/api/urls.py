from django.urls import path
from . views import bio_api_view

urlpatterns = [
    path('',bio_api_view,name='bio')
]
