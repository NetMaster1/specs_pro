from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('smartphones', views.SmartphoneView)
router.register('monitors', views.MonitorView)


urlpatterns = [ 
    path('api', include(router.urls)),
    path ('api_search_smartphone<str:name>', views.api_search_smartphone, name='api_search_smartphone'),
    #============================================================================
    path ('', views.categories, name='categories'),
    path ('search_page', views.search_page, name='search_page'),
    path ('product/<int:category_id>', views.product, name='product'),
    path ('search_sku', views.search_sku, name='search_sku'),
   
    
    #path ('', views., name='reference'),
    
]
