from django.conf.urls import url
from api_service import views

urlpatterns = [
    url(r'^players/$', views.get_players),
]
