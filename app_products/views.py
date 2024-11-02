from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Smartphone, Monitor
from app_reference_shared.models import OzonCategory, Name
from .serializers import SmartphoneSerializer, MonitorSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class SmartphoneView(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    #serializer_class = SmartphoneSerializer(many=True)
    http_method_names= ['get']#allowed methods

class MonitorView(viewsets.ModelViewSet):
    #category="Smartphones"
    queryset =Monitor.objects.all()
    serializer_class = MonitorSerializer
    http_method_names= ['get']#allowed methods

def api_search_smartphone (request, name):
    item=Name.objects.get(value=name)
    item=SmartphoneView.objects.get(name=item)
    serializer_class = SmartphoneSerializer
    http_method_names= ['get']#allowed methods

    return item


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
        url='http://127.0.0.1:8000/apimonitors'
    elif category.type_name=="Смартфон":
        products=Smartphone.objects.all()
        url='http://127.0.0.1:8000/apismartphones'
    context = {
        'category': category,
        'products': products,
        'url': url,
    }
    return render (request, 'products.html', context)

def search_sku(request):
    if request.method == "POST":
        text = request.POST["text"]
        items=Name.objects.filter(value__icontains=text)
        for i in items:
            print(i)
        array=[]
        for i in items:
            if Monitor.objects.filter(name=i).exists():
                product=Monitor.objects.get(name=i)
                array.append(product)
           
        context = {
            'array' : array,
        }
        return render (request, 'search_results.html', context)
    





#@api_view(['GET', ])
def search_page(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            name_item=Name.objects.get(value=name)
            item = Smartphone.objects.get(name=name_item)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SmartphoneSerializer(item)
        data=serializer.data
        print('=========================')
        print(data)
        context = {
            'data': data,
        }
        return render(request, 'search_page.html', context)
        #return Response(serializer.data, template_name='search_page.html')
    
   

    else:
        return render (request, 'search_page.html')
    
        


#api=json.loads(api_request.content)