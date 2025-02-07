from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='login'),
    path('welcome/<int:user_id>/', views.d_welcome, name='d_welcome'),  
    path('caja-welcome/<int:user_id>/', views.e_welcome, name='e_welcome'),  
    path('logout/', views.salir, name='logout'),

]  