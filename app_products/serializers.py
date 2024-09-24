from rest_framework import serializers
from .models import  Smartphone
from app_reference_shared.models import OzonCategory, ProcessorModel, Authentication

class SmartphoneSerializer(serializers.ModelSerializer):
    #category_name = serializers.StringRelatedField(source='category')#outputs string repsresentation of foreign key instead of id
    #processor_key = serializers.StringRelatedField(many=True)#outputs string repsresentation of foreign key instead of id
    items = serializers.SerializerMethodField('get_items')
   
    #other_fields = serializers.SerializerMethodField('get_other_fields')
    class Meta:
        model = Smartphone
        fields = ['items',]
        #fields ='__all__'
        depth=1#this field is crucial for displaying ManyToMany Field in serializer
        #Для вывода полей с ForeignField можно использовать функции get_smth или можно просто использовать параметр "depth=1"
        #exclude=['sensor.id']
    def get_items (self, smartphone):
        attributes =[]
        #=================================================
        # brand={
        # "complex_id": 0,
        # 'id': smartphone.brand.attribute_id,
        # "values": [{
        # # 'attribute_name': smartphone.brand.attribute_name, 
        # 'dictionary_value_id': smartphone.brand.dictionary_value_id,
        # 'value': smartphone.brand.value,
        # # 'is_required': smartphone.brand.is_required
        # }]
        # }
        # attributes.append(brand)
        #=================================================
        part_number={
        "complex_id": 0,
        'id': smartphone.part_number.attribute_id,
        "values": [{
        # 'attribute_name': smartphone.part_number.attribute_name, 
        'dictionary_value_id': smartphone.part_number.dictionary_value_id,
        'value': smartphone.part_number.value,
        # 'is_required': smartphone.part_number.is_required
        }]
        }
        attributes.append(part_number)
        #=================================================
        warranty_period={
        "complex_id": 0,
        'id': smartphone.warranty_period.attribute_id,
        "values": [{
        # 'attribute_name': smartphone.warranty_period.attribute_name, 
        'dictionary_value_id': smartphone.warranty_period.dictionary_value_id,
        'value': smartphone.warranty_period.value,
        # 'is_required': smartphone.warranty_period.is_required
        }]
        }
        attributes.append(warranty_period)
        #=================================================
        type={
        "complex_id": 0,
        'id': smartphone.type.attribute_id,
        "values": [{
        # 'attribute_name': smartphone.type.attribute_name, 
        'dictionary_value_id': smartphone.type.dictionary_value_id,
        'value': smartphone.type.value,
        # 'is_required': smartphone.type.is_required
        }]
        }
        attributes.append(type)
        #===============================================================
        model_name={
        "complex_id": 0,
        'id': smartphone.model_name.attribute_id,
        "values": [{
        # 'attribute_name': smartphone.model_name.attribute_name, 
        'dictionary_value_id': smartphone.model_name.dictionary_value_id,
        'value': smartphone.model_name.value,
        # 'is_required': smartphone.model_name.is_required
        }]
        }
        attributes.append(model_name)
        #================================================
        try:
            card_title_model_name={
            "complex_id": 0,
            'id': smartphone.card_title_model_name.attribute_id,
            "values": [{
            # 'attribute_name': smartphone.card_title_model_name.attribute_name, 
            'dictionary_value_id': smartphone.card_title_model_name.dictionary_value_id,
            'value': smartphone.card_title_model_name.value,
            # 'is_required': smartphone.card_title_model_name.is_required
            }]
            }
            attributes.append(card_title_model_name)
        except:
            print('No data provided')
        #================================================
        hard_drive={
        "complex_id": 0,
        'id': smartphone.hard_drive.attribute_id,
        "values": [{
        # 'attribute_name': smartphone.hard_drive.attribute_name, 
        'dictionary_value_id': smartphone.hard_drive.dictionary_value_id,
        'value': smartphone.hard_drive.value,
        # 'is_required': smartphone.hard_drive.is_required
        }]
        }
        attributes.append(hard_drive)
        #==================================================
        try:
            name={
            "complex_id": 0,
            'id': smartphone.name.attribute_id,
            "values": [{
            # 'attribute_name': smartphone.name.attribute_name, 
            'dictionary_value_id': smartphone.name.dictionary_value_id,
            'value': smartphone.name.value,
            # 'is_required': smartphone.name.is_required
            }]
            }
            attributes.append(name)
        except:
            print('No name provided')
        #==================================================
        try:
            description={
            "complex_id": 0,
            'id': smartphone.description.attribute_id,
            "values": [{
            # 'attribute_description': smartphone.description.attribute_description, 
            'dictionary_value_id': smartphone.description.dictionary_value_id,
            'value': smartphone.description.value,
            # 'is_required': smartphone.description.is_required
            }]
            }
            attributes.append(description)
        except:
            print('No description provided')
        #====================================================
        try:
            size={
            "complex_id": 0,
            "id": smartphone.size.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.size.attribute_name, 
            'dictionary_value_id': smartphone.size.dictionary_value_id, 
            'value': smartphone.size.value, 
            # 'is_required': smartphone.size.is_required
            }]
            }
            attributes.append(size)
        except:
            print('No size provided')
        #====================================================
        try:
            weight={
                "complex_id": 0,
                "id": smartphone.weight.attribute_id, 
                "values": [{ 
                    # 'attribute_name': smartphone.weight.attribute_name, 
                'dictionary_value_id': smartphone.weight.dictionary_value_id, 
                'value': smartphone.weight.value, 
                # 'is_required': smartphone.weight.is_required
                }]
                }
            attributes.append(weight)
        except:
            print('No weight provided')    
        #====================================================
        try:
            product_set={
            "complex_id": 0,
            "id": smartphone.product_set.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.product_set.attribute_name, 
            'dictionary_value_id': smartphone.product_set.dictionary_value_id, 
            'value': smartphone.product_set.value, 
            # 'is_required': smartphone.product_set.is_required
            }]
            }
            attributes.append(product_set)
        except:
            print('No product set provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in smartphone.country_of_manufacture.all():
                a= i.dictionary_value_id
                b= i.value
                item={
                    'dictionary_value_id':a,
                    'value': b
                }
                id=i.attribute_id
                array.append(item)
            dict['id']=id#добавляем ключ(id) и значение (id) в словарь dict
            dict['values']=array
            attributes.append(dict)
        except:
            print ('No country of manufacture provided')
        #=====================================================
        try:
            matrix_type={
            "complex_id": 0,
            "id": smartphone.matrix_type.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.matrix_type.attribute_name, 
            'dictionary_value_id': smartphone.matrix_type.dictionary_value_id, 
            'value': smartphone.matrix_type.value, 
            # 'is_required': smartphone.matrix_type.is_required
            }]
            }
            attributes.append(matrix_type)
        except:
            print('No matrix type provided')
        #======================================================
        try:
            sim_card_qnty={
            "complex_id": 0,
            "id": smartphone.sim_card_qnty.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.sim_card_qnty.attribute_name, 
            'dictionary_value_id': smartphone.sim_card_qnty.dictionary_value_id, 
            'value': smartphone.sim_card_qnty.value, 
            # 'is_required': smartphone.sim_card_qnty.is_required
            }]
            }
            attributes.append(sim_card_qnty)
        except:
            print('No sim card quanty provided')
        #======================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.card_type.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id#добавляем ключ(id) и значение (id) в словарь dict
        dict['values']=array
        attributes.append(dict)
        #=====================================================
        max_card_volume={
        "complex_id": 0,
        "id": smartphone.max_card_volume.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.max_card_volume.attribute_name, 
        'dictionary_value_id': smartphone.max_card_volume.dictionary_value_id, 
        'value': smartphone.max_card_volume.value, 
        # 'is_required': smartphone.max_card_volume.is_required
        }]
        }
        attributes.append(max_card_volume)
        #=====================================================
        bluetooth={
        "complex_id": 0,
        "id": smartphone.bluetooth.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.bluetooth.attribute_name, 
        'dictionary_value_id': smartphone.bluetooth.dictionary_value_id, 
        'value': smartphone.bluetooth.value, 
        # 'is_required': smartphone.bluetooth.is_required
        }]
        }
        attributes.append(bluetooth)
        #=====================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.navigation.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id#добавляем ключ(id) и значение (id) в словарь dict
        dict['values']=array
        attributes.append(dict)
        #========================================================
        array=[]
        dict={"complex_id":0}
                
        for i in smartphone.sensor.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        front_camera_resolution={
        "complex_id": 0,
        "id": smartphone.front_camera_resolution.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.front_camera_resolution.attribute_name, 
        'dictionary_value_id': smartphone.front_camera_resolution.dictionary_value_id, 
        'value': smartphone.front_camera_resolution.value, 
        # 'is_required': smartphone.front_camera_resolution.is_required
        }]
        }
        attributes.append(front_camera_resolution)
        #==========================================================
        basic_camera_resolution={
        "complex_id": 0,
        "id": smartphone.basic_camera_resolution.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.basic_camera_resolution.attribute_name, 
        'dictionary_value_id': smartphone.basic_camera_resolution.dictionary_value_id, 
        'value': smartphone.basic_camera_resolution.value, 
        # 'is_required': smartphone.basic_camera_resolution.is_required
        }]
        }
        attributes.append(basic_camera_resolution)
        #==========================================================
        battery_capacity={
        "complex_id": 0,
        "id": smartphone.battery_capacity.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.battery_capacity.attribute_name, 
        'dictionary_value_id': smartphone.battery_capacity.dictionary_value_id, 
        'value': smartphone.battery_capacity.value, 
        # 'is_required': smartphone.battery_capacity.is_required
        }]
        }
        attributes.append(battery_capacity)
        #========================================================
        array=[]
        dict={"complex_id":0}
                
        for i in smartphone.sim_type.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        battery_capacity={
        "complex_id": 0,
        "id": smartphone.battery_capacity.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.battery_capacity.attribute_name, 
        'dictionary_value_id': smartphone.battery_capacity.dictionary_value_id, 
        'value': smartphone.battery_capacity.value, 
        # 'is_required': smartphone.battery_capacity.is_required
        }]
        }
        attributes.append(battery_capacity)
        #==========================================================
        standby_period={
        "complex_id": 0,
        "id": smartphone.standby_period.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.standby_period.attribute_name, 
        'dictionary_value_id': smartphone.standby_period.dictionary_value_id, 
        'value': smartphone.standby_period.value, 
        # 'is_required': smartphone.standby_period.is_required
        }]
        }
        attributes.append(standby_period)
        #========================================================
        array=[]
        dict={"complex_id":0}
                
        for i in smartphone.wifi.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        video_processor_brand={
        "complex_id": 0,
        "id": smartphone.video_processor_brand.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.video_processor_brand.attribute_name, 
        'dictionary_value_id': smartphone.video_processor_brand.dictionary_value_id, 
        'value': smartphone.video_processor_brand.value, 
        # 'is_required': smartphone.video_processor_brand.is_required
        }]
        }
        attributes.append(video_processor_brand)
        #========================================================
        screen_resolution={
        "complex_id": 0,
        "id": smartphone.screen_resolution.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.screen_resolution.attribute_name, 
        'dictionary_value_id': smartphone.screen_resolution.dictionary_value_id, 
        'value': smartphone.screen_resolution.value, 
        # 'is_required': smartphone.screen_resolution.is_required
        }]
        }
        attributes.append(screen_resolution)
        #========================================================
        video_quality={
        "complex_id": 0,
        "id": smartphone.video_quality.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.video_quality.attribute_name, 
        'dictionary_value_id': smartphone.video_quality.dictionary_value_id, 
        'value': smartphone.video_quality.value, 
        # 'is_required': smartphone.video_quality.is_required
        }]
        }
        attributes.append(video_quality)
        #========================================================
        array=[]
        dict={"complex_id":0}
                
        for i in smartphone.gadget_model.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.protection_grade.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        work_period={
        "complex_id": 0,
        "id": smartphone.work_period.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.work_period.attribute_name, 
        'dictionary_value_id': smartphone.work_period.dictionary_value_id, 
        'value': smartphone.work_period.value, 
        # 'is_required': smartphone.work_period.is_required
        }]
        }
        attributes.append(work_period)
        #========================================================
        record_max_speed={
        "complex_id": 0,
        "id": smartphone.record_max_speed.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.record_max_speed.attribute_name, 
        'dictionary_value_id': smartphone.record_max_speed.dictionary_value_id, 
        'value': smartphone.record_max_speed.value, 
        # 'is_required': smartphone.record_max_speed.is_required
        }]
        }
        attributes.append(record_max_speed)
        #========================================================
        life_span={
        "complex_id": 0,
        "id": smartphone.life_span.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.life_span.attribute_name, 
        'dictionary_value_id': smartphone.life_span.dictionary_value_id, 
        'value': smartphone.life_span.value, 
        # 'is_required': smartphone.life_span.is_required
        }]
        }
        attributes.append(life_span)
        #========================================================
        #========================================================
        screen_size={
        "complex_id": 0,
        "id": smartphone.screen_size.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.screen_size.attribute_name, 
        'dictionary_value_id': smartphone.screen_size.dictionary_value_id, 
        'value': smartphone.screen_size.value, 
        # 'is_required': smartphone.screen_size.is_required
        }]
        }
        attributes.append(screen_size)
        #========================================================
        # seller_code={
        # "complex_id": 0,
        # "id": smartphone.seller_code.attribute_id, 
        # "values": [{ 
        #     # 'attribute_name': smartphone.seller_code.attribute_name, 
        # 'dictionary_value_id': smartphone.seller_code.dictionary_value_id, 
        # 'value': smartphone.seller_code.value, 
        # # 'is_required': smartphone.seller_code.is_required
        # }]
        # }
        # attributes.append(seller_code)
        #========================================================
        gadget_serie={
        "complex_id": 0,
        "id": smartphone.gadget_serie.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.gadget_serie.attribute_name, 
        'dictionary_value_id': smartphone.gadget_serie.dictionary_value_id, 
        'value': smartphone.gadget_serie.value, 
        # 'is_required': smartphone.gadget_serie.is_required
        }]
        }
        attributes.append(gadget_serie)
        #========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.camera_function.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        hazard_grade={
        "complex_id": 0,
        "id": smartphone.hazard_grade.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.hazard_grade.attribute_name, 
        'dictionary_value_id': smartphone.hazard_grade.dictionary_value_id, 
        'value': smartphone.hazard_grade.value, 
        # 'is_required': smartphone.hazard_grade.is_required
        }]
        }
        attributes.append(hazard_grade)
        #========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.colour.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        marketing_colour={
        "complex_id": 0,
        "id": smartphone.marketing_colour.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.marketing_colour.attribute_name, 
        'dictionary_value_id': smartphone.marketing_colour.dictionary_value_id, 
        'value': smartphone.marketing_colour.value, 
        # 'is_required': smartphone.marketing_colour.is_required
        }]
        }
        attributes.append(marketing_colour)
        #==========================================================
        qnty_of_basic_cameras={
        "complex_id": 0,
        "id": smartphone.qnty_of_basic_cameras.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.qnty_of_basic_cameras.attribute_name, 
        'dictionary_value_id': smartphone.qnty_of_basic_cameras.dictionary_value_id, 
        'value': smartphone.qnty_of_basic_cameras.value, 
        # 'is_required': smartphone.qnty_of_basic_cameras.is_required
        }]
        }
        attributes.append(qnty_of_basic_cameras)
        #==========================================================
        processor={
        "complex_id": 0,
        "id": smartphone.processor.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.processor.attribute_name, 
        'dictionary_value_id': smartphone.processor.dictionary_value_id, 
        'value': smartphone.processor.value, 
        # 'is_required': smartphone.processor.is_required
        }]
        }
        attributes.append(processor)
        #===========================================================
        video_processor={
        "complex_id": 0,
        "id": smartphone.video_processor.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.video_processor.attribute_name, 
        'dictionary_value_id': smartphone.video_processor.dictionary_value_id, 
        'value': smartphone.video_processor.value, 
        # 'is_required': smartphone.video_processor.is_required
        }]
        }
        attributes.append(video_processor)
        #===========================================================
        processor_brand={
        "complex_id": 0,
        "id": smartphone.processor_brand.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.processor_brand.attribute_name, 
        'dictionary_value_id': smartphone.processor_brand.dictionary_value_id, 
        'value': smartphone.processor_brand.value, 
        # 'is_required': smartphone.processor_brand.is_required
        }]
        }
        attributes.append(processor_brand)
        #===========================================================
        processor_frequency={
        "complex_id": 0,
        "id": smartphone.processor_frequency.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.processor_frequency.attribute_name, 
        'dictionary_value_id': smartphone.processor_frequency.dictionary_value_id, 
        'value': smartphone.processor_frequency.value, 
        # 'is_required': smartphone.processor_frequency.is_required
        }]
        }
        attributes.append(processor_frequency)
        #===========================================================
        processor_core_qnty={
        "complex_id": 0,
        "id": smartphone.processor_core_qnty.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.processor_core_qnty.attribute_name, 
        'dictionary_value_id': smartphone.processor_core_qnty.dictionary_value_id, 
        'value': smartphone.processor_core_qnty.value, 
        # 'is_required': smartphone.processor_core_qnty.is_required
        }]
        }
        attributes.append(processor_core_qnty)
        #===========================================================
        processor_model={
        "complex_id": 0,
        "id": smartphone.processor_model.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.processor_model.attribute_name, 
        'dictionary_value_id': smartphone.processor_model.dictionary_value_id, 
        'value': smartphone.processor_model.value, 
        # 'is_required': smartphone.processor_model.is_required
        }]
        }
        attributes.append(processor_model)
        #========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.wireless_interface.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.case_material.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        operation_system={
        "complex_id": 0,
        "id": smartphone.operation_system.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.operation_system.attribute_name, 
        'dictionary_value_id': smartphone.operation_system.dictionary_value_id, 
        'value': smartphone.operation_system.value, 
        # 'is_required': smartphone.operation_system.is_required
        }]
        }
        attributes.append(operation_system)
        if smartphone.operation_system.value=='iOS':
            ios_version={
            "complex_id": 0,
            "id": smartphone.ios_version.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.ios_version.attribute_name, 
            'dictionary_value_id': smartphone.ios_version.dictionary_value_id, 
            'value': smartphone.ios_version.value, 
            # 'is_required': smartphone.ios_version.is_required
            }]
            }
            attributes.append(ios_version)
        elif smartphone.operation_system.value=='Android':
            android_version={
            "complex_id": 0,
            "id": smartphone.android_version.attribute_id, 
            "values": [{ 
                # 'attribute_name': smartphone.android_version.attribute_name, 
            'dictionary_value_id': smartphone.android_version.dictionary_value_id, 
            'value': smartphone.android_version.value, 
            # 'is_required': smartphone.android_version.is_required
            }]
            }
            attributes.append(android_version)
        
        #========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.interface.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.comms_standard.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        microsd_slot={
        "complex_id": 0,
        "id": smartphone.microsd_slot.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.microsd_slot.attribute_name, 
        'dictionary_value_id': smartphone.microsd_slot.dictionary_value_id, 
        'value': smartphone.microsd_slot.value, 
        # 'is_required': smartphone.microsd_slot.is_required
        }]
        }
        attributes.append(microsd_slot)
        #========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.special_feature.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.charging_function.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.stabilization.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        array=[]
        dict={"complex_id":0}
        for i in smartphone.authentification.all():
            a= i.dictionary_value_id
            b= i.value
            item={
                'dictionary_value_id':a,
                'value': b
            }
            id=i.attribute_id
            array.append(item)
        dict['id']=id
        dict['values']=array
        attributes.append(dict)
        #==========================================================
        case_form={
        "complex_id": 0,
        "id": smartphone.case_form.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.case_form.attribute_name, 
        'dictionary_value_id': smartphone.case_form.dictionary_value_id, 
        'value': smartphone.case_form.value, 
        # 'is_required': smartphone.case_form.is_required
        }]
        }
        attributes.append(case_form)
        #==========================================================
        esim_support={
        "complex_id": 0,
        "id": smartphone.esim_support.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.esim_support.attribute_name, 
        'dictionary_value_id': smartphone.esim_support.dictionary_value_id, 
        'value': smartphone.esim_support.value, 
        # 'is_required': smartphone.esim_support.is_required
        }]
        }
        attributes.append(esim_support)
        #==========================================================
        key_word={
        "complex_id": 0,
        "id": smartphone.key_word.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.key_word.attribute_name, 
        'dictionary_value_id': smartphone.key_word.dictionary_value_id, 
        'value': smartphone.key_word.value, 
        # 'is_required': smartphone.key_word.is_required
        }]
        }
        attributes.append(key_word)
        #==========================================================
        ram={
        "complex_id": 0,
        "id": smartphone.ram.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.ram.attribute_name, 
        'dictionary_value_id': smartphone.ram.dictionary_value_id, 
        'value': smartphone.ram.value, 
        # 'is_required': smartphone.ram.is_required
        }]
        }
        attributes.append(ram)
        #==========================================================
        publishing_year={
        "complex_id": 0,
        "id": smartphone.publishing_year.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.publishing_year.attribute_name, 
        'dictionary_value_id': smartphone.publishing_year.dictionary_value_id, 
        'value': smartphone.publishing_year.value, 
        # 'is_required': smartphone.publishing_year.is_required
        }]
        }
        attributes.append(publishing_year)
        #==========================================================
        smartphone_version={
        "complex_id": 0,
        "id": smartphone.smartphone_version.attribute_id, 
        "values": [{ 
            # 'attribute_name': smartphone.smartphone_version.attribute_name, 
        'dictionary_value_id': smartphone.smartphone_version.dictionary_value_id, 
        'value': smartphone.smartphone_version.value, 
        # 'is_required': smartphone.smartphone_version.is_required
        }]
        }
        attributes.append(smartphone_version)
        items=[{}]
        items=[{"attributes" : attributes, 
               "barcode": "",
                "description_category_id": 15621050,
                "new_description_category_id": 0,
                "color_image": "",
                "complex_attributes": [],
                "currency_code": "RUB",
                "depth": "",
                "dimension_unit": "mm",
                "height": "100",
                "images":   [ smartphone.image_1, 
                                smartphone.image_2,
                                smartphone.image_3
                            ],
                "images360": [],
                "name": smartphone.name.value,
                "offer_id": smartphone.part_number.value,
                "old_price": "",
                "pdf_list": [],
                "price": "1000",
                "primary_image": "",
                "vat": "",
                "weight": smartphone.weight.value,
                "weight_unit": "g",
                "width":""
                 }]

        # return attributes
        return items






   