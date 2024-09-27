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
                android_version=product.android_version,
                ios_version=product.ios_version,
                product_set=product.product_set,
                publishing_year=product.publishing_year,
                warranty_period=product.warranty_period,
                life_span=product.life_span,
                sim_card_qnty=product.sim_card_qnty,
                processor=product.processor,
                processor_brand=product.processor_brand,
                processor_model=product.processor_model,
                processor_core_qnty=product.processor_core_qnty,
                processor_frequency=product.processor_frequency,
                video_processor_brand=product.video_processor_brand,
                video_processor=product.video_processor,
                microsd_slot=product.microsd_slot,
                max_card_volume=product.max_card_volume,
                battery_capacity=product.battery_capacity,
                standby_period=product.standby_period,
                work_period=product.work_period,
                matrix_type=product.matrix_type,
                screen_resolution=product.screen_resolution,
                basic_camera_resolution=product.basic_camera_resolution,
                front_camera_resolution=product.front_camera_resolution,
                record_max_speed=product.record_max_speed,
                video_quality=product.video_quality,
                bluetooth=product.bluetooth,
                case_form=product.case_form,
                size=product.size,
                weight=product.weight,
                marketing_colour=product.marketing_colour,
                description=product.description,
                key_word=product.key_word,
                smartphone_version=product.smartphone_version,
                model_name=product.model_name,
                card_title_model_name=product.card_title_model_name,
                type=product.type,
                gadget_serie=product.gadget_serie,
                part_number=product.part_number,
                hazard_grade=product.hazard_grade,

            )
            #iterate multiple objects related to many-to-many field
            for i in product.comms_standard.all():
                new_product.comms_standard.add(i)
            for i in product.sim_type.all():
                new_product.sim_type.add(i)
            for i in product.country_of_manufacture.all():
                new_product.country_of_manufacture.add(i)
            for i in product.card_type.all():
                new_product.card_type.add(i)
            for i in product.charging_function.all():
                new_product.charging_function.add(i)
            for i in product.camera_function.all():
                new_product.camera_function.add(i)
            for i in product.stabilization.all():
                new_product.stabilization.add(i)
            for i in product.wifi.all():
                new_product.wifi.add(i)
            for i in product.wireless_interface.all():
                new_product.wireless_interface.add(i)
            for i in product.interface.all():
                new_product.interface.add(i)
            for i in product.sensor.all():
                new_product.sensor.add(i)
            for i in product.navigation.all():
                new_product.navigation.add(i)
            for i in product.authentification.all():
                new_product.authentification.add(i)
            for i in product.case_material.all():
                new_product.case_material.add(i)
            for i in product.special_feature.all():
                new_product.special_feature.add(i)
            for i in product.gadget_model.all():
                new_product.gadget_model.add(i)
            for i in product.protection_grade.all():
                new_product.protection_grade.add(i)
            new_product.save()
          
         
            return render (request, 'duplicate.html')
        else:
            return render (request, 'duplicate.html')