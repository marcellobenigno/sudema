from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('pagina-2/', views.pag2, name='pag2'),
    path('sobre/', views.sobre, name='sobre'),
]