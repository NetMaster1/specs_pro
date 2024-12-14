from django.urls import path, include
from . import views

urlpatterns = [ 
         #path ('create_from_ozon', views.create_from_ozon, name='create_from_ozon'),
         path ('selenium_search_ozon_monitor', views.selenium_search_ozon_monitor, name='selenium_search_ozon_monitor'),
         path ('selenium_search_ozon_smartphone', views.selenium_search_ozon_smartphone, name='selenium_search_ozon_smartphone'),
         #path ('specs', views.specs, name='specs'),
        #  path ('ozon_test', views.ozon_test, name='ozon_test'),
]