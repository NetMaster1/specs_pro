from django.shortcuts import render
from rest_framework import viewsets
from .models import Smartphone, Monitor
from app_reference_shared.models import OzonCategory
from .serializers import SmartphoneSerializer, MonitorSerializer

# Create your views here.

class SmartphoneView(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    # queryset = Monitor.objects.all()
    serializer_class = SmartphoneSerializer
    #serializer_class = SmartphoneSerializer(many=True)
    http_method_names= ['get']#allowed methods

class MonitorView(viewsets.ModelViewSet):
    #category="Smartphones"
    queryset =Monitor.objects.all()
    serializer_class = MonitorSerializer
    http_method_names= ['get']#allowed methods

#========================================================================

def categories (request):
    categories=OzonCategory.objects.filter(activated=True)
    context = {
        'categories': categories
    }
    return render (request, 'categories.html', context)

def product (request, category_id):
    category=OzonCategory.objects.get(id=category_id)
    if category.type_name == 'Монитор':
        products=Monitor.objects.all()
    elif category.type_name=="Смартфон":
        products=Smartphone.objects.all()
 
    context = {
        'products': products
    }
    return render (request, 'products.html', context)



#api=json.loads(api_request.content)