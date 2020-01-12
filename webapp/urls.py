from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),   #homepage setup
	url(r'^GetOrbitalLaunchesCSV/', views.GetOrbitalLaunchesCSV, name="GetOrbitalLaunchesCSV"),
url(r'^GetOrbitalLaunchesData/', views.GetOrbitalLaunchesData, name="GetOrbitalLaunchesData"),
]
