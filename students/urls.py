from django.conf.urls import url
import views

urlpatterns = [
	url("^([0-9]+)$", views.index),
	url("^$", views.index)
]