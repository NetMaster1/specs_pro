from django.urls import path, include
from . import views

urlpatterns = [ 
         path ('create_smartphone', views.create_smartphone, name='create_smartphone'),
         #path ('create_from_ozon', views.create_from_ozon, name='create_from_ozon'),
         path ('selenium_search_ozon_monitor', views.selenium_search_ozon_monitor, name='selenium_search_ozon_monitor'),
         #path ('specs', views.specs, name='specs'),
         path ('parsing_images', views.parsing_images, name='parsing_images'),
        #  path ('ozon_test', views.ozon_test, name='ozon_test'),
]