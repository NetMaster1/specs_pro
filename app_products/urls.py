from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('smartphones', views.SmartphoneView)
router.register('monitors', views.MonitorView)

urlpatterns = [ 
    path('api', include(router.urls)),
    path ('', views.categories, name='categories'),
    path ('product/<int:category_id>', views.product, name='product'),
   
    
    #path ('', views., name='reference'),
    
]
