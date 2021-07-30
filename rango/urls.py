from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
	path('', views.index, name='index'),
	
]

urlpatterns = [
	path('about/', views.about, name='about'),
]

#urlpatterns = [
#	path('rango/', views.index, name='index'),
#] 加了没用，about报错