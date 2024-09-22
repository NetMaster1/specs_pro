from django.urls import path, include
from . import views

urlpatterns = [ 
         path ('create_model', views.create_model, name='create_model'),
]