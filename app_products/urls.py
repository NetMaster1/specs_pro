from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductView)


#router.register('categories', views.ProductCategoryView)

urlpatterns = [ 
    path('api', include(router.urls)),
    path ('', views.products, name='products'),
   
    
    #path ('', views., name='reference'),
    
]
