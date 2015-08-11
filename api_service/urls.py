from django.conf.urls import url
from api_service import views

urlpatterns = [
    url(r'^players/$', views.get_players),
    url(r'^player/(?P<id>[0-9]+)/$', views.get_player),
]
