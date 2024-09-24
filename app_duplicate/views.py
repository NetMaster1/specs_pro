from django.shortcuts import render
from app_products.models import Smartphone
from app_reference_shared.models import Name

# Create your views here.
def duplicate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name_1 = request.POST["name_1"]
            name_2 = request.POST["name_2"]
            try:
                item=Name.objects.get(value=name_1)
            except:
                print('=====================================')
                print('No such smartphone model')
            if Name.objects.filter(value=name_2):
                name=Name.objects.get(value=name_2)
            else:
                name=Name.objects.create(
                    attribute_name = "Название",
                    attribute_id = "4180",
                    value = name_2,
                    dictionary_value_id =0,
                    is_required = False,
                    category_dependent = False,
                    is_collection = False,
                )
            product=Smartphone.objects.get(name=item)
            
            new_product = Smartphone.objects.create(
                category_name=product.category_name,
                name=name,
                esim_support=product.esim_support,
                ram=product.ram,
                hard_drive=product.hard_drive,
                screen_size=product.screen_size,
                qnty_of_basic_cameras=product.qnty_of_basic_cameras,
                operation_system=product.operation_system,
            )
            #iterate multiple objects related to many-to-many field
            for i in product.comms_standard.all():
                new_product.comms_standard.add(i)
            new_product.save()
            for i in product.sim_type.all():
                new_product.sim_type.add(i)
            new_product.save()
         
            return render (request, 'duplicate.html')
        else:
            return render (request, 'duplicate.html')