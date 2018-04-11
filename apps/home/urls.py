from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^explore$', views.explore, name='explore'),
	url(r'^manage$', views.manage, name='explore'),
	url(r'^about', views.about, name='about')
]