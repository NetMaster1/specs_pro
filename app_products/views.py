from django.shortcuts import render
from rest_framework import viewsets
from .models import Smartphone
from app_reference_shared.models import OzonCategory
from .serializers import SmartphoneSerializer

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    #serializer_class = SmartphoneSerializer(many=True)
    http_method_names= ['get']#allowed methods


#class ProductCategoryView(viewsets.ModelViewSet):
    #category="Smartphones"
    #queryset = ProductCategory.objects.filter(name=category)
    # queryset = ProductCategory.objects.all()
    # serializer_class = ProductCategorySerializer

#========================================================================

def products (request):
    #products=Smartphone.objects.all()
    categories=OzonCategory.objects.all()
    #print(products)
    context = {

        'categories': categories
    }
    return render (request, 'products.html', context)


#api=json.loads(api_request.content)