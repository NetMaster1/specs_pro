from django.urls import path, include
from . import views

urlpatterns = [ 
         path ('create_smartphone', views.create_smartphone, name='create_smartphone'),
         path ('create_from_ozon', views.create_from_ozon, name='create_from_ozon'),
         path ('ozon_test', views.ozon_test, name='ozon_test'),
]