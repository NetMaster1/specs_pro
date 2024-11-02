from rest_framework import serializers
from .models import  Smartphone, Monitor
from app_reference_shared.models import OzonCategory, ProcessorModel, Authentication

class SmartphoneSerializer(serializers.ModelSerializer):
#class SmartphoneSerializer(serializers.HyperlinkedModelSerializer):
    #category_name = serializers.StringRelatedField(source='category')#outputs string repsresentation of foreign key instead of id
    #processor_key = serializers.StringRelatedField(many=True)#outputs string repsresentation of foreign key instead of id
    items = serializers.SerializerMethodField('get_items')
   
    #other_fields = serializers.SerializerMethodField('get_other_fields')
    class Meta:
        model = Smartphone
        fields = ['items',]
        #fields = ['url', 'items',]
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
        # type={
        # "complex_id": 0,
        # 'id': smartphone.type.attribute_id,
        # "values": [{
        # # 'attribute_name': smartphone.type.attribute_name, 
        # 'dictionary_value_id': smartphone.type.dictionary_value_id,
        # 'value': smartphone.type.value,
        # # 'is_required': smartphone.type.is_required
        # }]
        # }
        # attributes.append(type)
        #===============================================================
        # model_name={
        # "complex_id": 0,
        # 'id': smartphone.model_name.attribute_id,
        # "values": [{
        # # 'attribute_name': smartphone.model_name.attribute_name, 
        # 'dictionary_value_id': smartphone.model_name.dictionary_value_id,
        # 'value': smartphone.model_name.value,
        # # 'is_required': smartphone.model_name.is_required
        # }]
        # }
        # attributes.append(model_name)
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
        try:
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
        except:
            print('No data provided')
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
        try:
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
        except:
            print('no card_type provided')
        #=====================================================
        try:
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
        except:
            print('No data provided')
        #=====================================================
        try:
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
        except:
            print('No data provided')
        #=====================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
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
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #===========================================================
        try:
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
        except:
            print('No data provided')
        #===========================================================
        try:
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
        except:
            print('No data provided')
        #===========================================================
        try:
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
        except:
            print('No data provided')
        #===========================================================
        try:
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
        except:
            print('No data provided')
        #===========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
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
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #==========================================================
        try:
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
        except:
            print('No data provided')
        #=====================================
        #items=[{}]
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

#class MonitorSerializer(serializers.ModelSerializer):
class MonitorSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.SerializerMethodField('get_items')

    class Meta:
        model = Monitor
        fields = ['url', 'items',]

    def get_items (self, monitor):
        attributes =[]
        try:
            warranty_period={
            "complex_id": 0,
            'id': monitor.warranty_period.attribute_id,
            "values": [{
            # 'attribute_name': monitor.warranty_period.attribute_name, 
            'dictionary_value_id': monitor.warranty_period.dictionary_value_id,
            'value': monitor.warranty_period.value,
            # 'is_required': monitor.warranty_period.is_required
            }]
            }
        except:
            warranty_period={
            "complex_id": 0,
            'id': 9048,
            "values": [{
            # 'attribute_name': monitor.warranty_period.attribute_name, 
            'dictionary_value_id': 0,
            'value': '1 год',
            # 'is_required': monitor.warranty_period.is_required
            }]
            }
        attributes.append(warranty_period)
        #=================================================
        type={
        "complex_id": 0,
        'id': monitor.type.attribute_id,
        "values": [{
        # 'attribute_name': monitor.type.attribute_name, 
        'dictionary_value_id': monitor.type.dictionary_value_id,
        'value': monitor.type.value,
        # 'is_required': monitor.type.is_required
        }]
        }
        attributes.append(type)
        #===============================================================
        model_name={
        "complex_id": 0,
        'id': monitor.model_name.attribute_id,
        "values": [{
        # 'attribute_name': monitor.model_name.attribute_name, 
        'dictionary_value_id': monitor.model_name.dictionary_value_id,
        'value': monitor.model_name.value,
        # 'is_required': monitor.model_name.is_required
        }]
        }
        attributes.append(model_name)
        #===============================================================
        try:
            resolution={
            "complex_id": 0,
            'id': monitor.resolution.attribute_id,
            "values": [{
            # 'attribute_name': monitor.resolution.attribute_name, 
            'dictionary_value_id': monitor.resolution.dictionary_value_id,
            'value': monitor.resolution.value,
            # 'is_required': monitor.resolution.is_required
            }]
            }
        except:
            resolution={
            "complex_id": 0,
            'id': 5592,
            "values": [{
            # 'attribute_name': monitor.resolution.attribute_name, 
            'dictionary_value_id': 971410300,
            'value': '1920x1080',
            # 'is_required': monitor.resolution.is_required
            }]
            }
        attributes.append(resolution)



        #================================================
        try:
            product_set={
            "complex_id": 0,
            'id': monitor.product_set.attribute_id,
            "values": [{
            # 'attribute_name': monitor.product_set.attribute_name, 
            'dictionary_value_id': monitor.product_set.dictionary_value_id,
            'value': monitor.product_set.value,
            # 'is_required': monitor.product_set.is_required
            }]
            }
            attributes.append(product_set)
        except:
            print('No product_set data  provided')
        #================================================
        try:
            name={
            "complex_id": 0,
            'id': monitor.name.attribute_id,
            "values": [{
            # 'attribute_name': monitor.name.attribute_name, 
            'dictionary_value_id': monitor.name.dictionary_value_id,
            'value': monitor.name.value,
            # 'is_required': monitor.name.is_required
            }]
            }
            attributes.append(name)
        except:
            print('No name data  provided')
        #================================================
        try:
            country_of_manufacture={
            "complex_id": 0,
            'id': monitor.country_of_manufacture.attribute_id,
            "values": [{
            # 'attribute_country_of_manufacture': monitor.country_of_manufacture.attribute_country_of_manufacture, 
            'dictionary_value_id': monitor.country_of_manufacture.dictionary_value_id,
            'value': monitor.country_of_manufacture.value,
            # 'is_required': monitor.country_of_manufacture.is_required
            }]
            }
            attributes.append(country_of_manufacture)
        except:
            print('No country_of_manufacture data  provided')
        #================================================
        try:
            screen_coating={
            "complex_id": 0,
            'id': monitor.screen_coating.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.screen_coating.attribute_screen_coating, 
            'dictionary_value_id': monitor.screen_coating.dictionary_value_id,
            'value': monitor.screen_coating.value,
            # 'is_required': monitor.screen_coating.is_required
            }]
            }
            attributes.append(screen_coating)
        except:
            print('No screen_coating data  provided')
        #================================================
        try:
            hdmi_ports={
            "complex_id": 0,
            'id': monitor.hdmi_ports.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.hdmi_ports.attribute_screen_coating, 
            'dictionary_value_id': monitor.hdmi_ports.dictionary_value_id,
            'value': monitor.hdmi_ports.value,
            # 'is_required': monitor.hdmi_ports.is_required
            }]
            }
            attributes.append(hdmi_ports)
        except:
            print('No hdmi_ports data  provided')
        #================================================
        try:
            hdmi_ports={
            "complex_id": 0,
            'id': monitor.hdmi_ports.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.hdmi_ports.attribute_screen_coating, 
            'dictionary_value_id': monitor.hdmi_ports.dictionary_value_id,
            'value': monitor.hdmi_ports.value,
            # 'is_required': monitor.hdmi_ports.is_required
            }]
            }
            attributes.append(hdmi_ports)
        except:
            print('No hdmi_ports data  provided')
        #================================================
        try:
            pixel_size={
            "complex_id": 0,
            'id': monitor.pixel_size.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.pixel_size.attribute_screen_coating, 
            'dictionary_value_id': monitor.pixel_size.dictionary_value_id,
            'value': monitor.pixel_size.value,
            # 'is_required': monitor.pixel_size.is_required
            }]
            }
            attributes.append(pixel_size)
        except:
            print('No pixel_size data  provided')
        #================================================
        try:
            ratio={
            "complex_id": 0,
            'id': monitor.ratio.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.ratio.attribute_screen_coating, 
            'dictionary_value_id': monitor.ratio.dictionary_value_id,
            'value': monitor.ratio.value,
            # 'is_required': monitor.ratio.is_required
            }]
            }
            attributes.append(ratio)
        except:
            print('No ratio data  provided')
        #================================================
        try:
            max_screen_frq={
            "complex_id": 0,
            'id': monitor.max_screen_frq.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.max_screen_frq.attribute_screen_coating, 
            'dictionary_value_id': monitor.max_screen_frq.dictionary_value_id,
            'value': monitor.max_screen_frq.value,
            # 'is_required': monitor.max_screen_frq.is_required
            }]
            }
            attributes.append(max_screen_frq)
        except:
            print('No max_screen_frq data  provided')
        #================================================
        try:
            brightness={
            "complex_id": 0,
            'id': monitor.brightness.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.brightness.attribute_screen_coating, 
            'dictionary_value_id': monitor.brightness.dictionary_value_id,
            'value': monitor.brightness.value,
            # 'is_required': monitor.brightness.is_required
            }]
            }
            attributes.append(brightness)
        except:
            print('No brightness data  provided')
        #================================================
        try:
            contrast={
            "complex_id": 0,
            'id': monitor.contrast.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.contrast.attribute_screen_coating, 
            'dictionary_value_id': monitor.contrast.dictionary_value_id,
            'value': monitor.contrast.value,
            # 'is_required': monitor.contrast.is_required
            }]
            }
            attributes.append(contrast)
        except:
            print('No contrast data  provided')
        #================================================
        try:
            dynamic_contrast={
            "complex_id": 0,
            'id': monitor.dynamic_contrast.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.dynamic_contrast.attribute_screen_coating, 
            'dictionary_value_id': monitor.dynamic_contrast.dictionary_value_id,
            'value': monitor.dynamic_contrast.value,
            # 'is_required': monitor.dynamic_contrast.is_required
            }]
            }
            attributes.append(dynamic_contrast)
        except:
            print('No dynamic_contrast data  provided')
        #================================================
        try:
            look_angle={
            "complex_id": 0,
            'id': monitor.look_angle.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.look_angle.attribute_screen_coating, 
            'dictionary_value_id': monitor.look_angle.dictionary_value_id,
            'value': monitor.look_angle.value,
            # 'is_required': monitor.look_angle.is_required
            }]
            }
            attributes.append(look_angle)
        except:
            print('No look_angle data  provided')
        #================================================
        try:
            horizontal_frequency={
            "complex_id": 0,
            'id': monitor.horizontal_frequency.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.horizontal_frequency.attribute_screen_coating, 
            'dictionary_value_id': monitor.horizontal_frequency.dictionary_value_id,
            'value': monitor.horizontal_frequency.value,
            # 'is_required': monitor.horizontal_frequency.is_required
            }]
            }
            attributes.append(horizontal_frequency)
        except:
            print('No horizontal_frequency data  provided')
        #================================================
        try:
            vertical_frequency={
            "complex_id": 0,
            'id': monitor.vertical_frequency.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.vertical_frequency.attribute_screen_coating, 
            'dictionary_value_id': monitor.vertical_frequency.dictionary_value_id,
            'value': monitor.vertical_frequency.value,
            # 'is_required': monitor.vertical_frequency.is_required
            }]
            }
            attributes.append(vertical_frequency)
        except:
            print('No vertical_frequency data  provided')
        #================================================
        try:
            web_camera={
            "complex_id": 0,
            'id': monitor.web_camera.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.web_camera.attribute_screen_coating, 
            'dictionary_value_id': monitor.web_camera.dictionary_value_id,
            'value': monitor.web_camera.value,
            # 'is_required': monitor.web_camera.is_required
            }]
            }
            attributes.append(web_camera)
        except:
            print('No web_camera data  provided')
        #================================================
        try:
            stand_adjustment={
            "complex_id": 0,
            'id': monitor.stand_adjustment.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.stand_adjustment.attribute_screen_coating, 
            'dictionary_value_id': monitor.stand_adjustment.dictionary_value_id,
            'value': monitor.stand_adjustment.value,
            # 'is_required': monitor.stand_adjustment.is_required
            }]
            }
            attributes.append(stand_adjustment)
        except:
            print('No stand_adjustment data  provided')
        #================================================
        try:
            power_capacity={
            "complex_id": 0,
            'id': monitor.power_capacity.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.power_capacity.attribute_screen_coating, 
            'dictionary_value_id': monitor.power_capacity.dictionary_value_id,
            'value': monitor.power_capacity.value,
            # 'is_required': monitor.power_capacity.is_required
            }]
            }
            attributes.append(power_capacity)
        except:
            print('No power_capacity data  provided')
        #================================================
        try:
            usb_port={
            "complex_id": 0,
            'id': monitor.usb_port.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.usb_port.attribute_screen_coating, 
            'dictionary_value_id': monitor.usb_port.dictionary_value_id,
            'value': monitor.usb_port.value,
            # 'is_required': monitor.usb_port.is_required
            }]
            }
            attributes.append(usb_port)
        except:
            print('No usb_port data  provided')
        #================================================
        try:
            life_span={
            "complex_id": 0,
            'id': monitor.life_span.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.life_span.attribute_screen_coating, 
            'dictionary_value_id': monitor.life_span.dictionary_value_id,
            'value': monitor.life_span.value,
            # 'is_required': monitor.life_span.is_required
            }]
            }
            attributes.append(life_span)
        except:
            print('No life_span data  provided')
        #================================================
        try:
            builtin_speaker={
            "complex_id": 0,
            'id': monitor.builtin_speaker.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.builtin_speaker.attribute_screen_coating, 
            'dictionary_value_id': monitor.builtin_speaker.dictionary_value_id,
            'value': monitor.builtin_speaker.value,
            # 'is_required': monitor.builtin_speaker.is_required
            }]
            }
            attributes.append(builtin_speaker)
        except:
            print('No builtin_speaker data  provided')
        #================================================
        try:
            weight={
            "complex_id": 0,
            'id': monitor.weight.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.weight.attribute_screen_coating, 
            'dictionary_value_id': monitor.weight.dictionary_value_id,
            'value': monitor.weight.value,
            # 'is_required': monitor.weight.is_required
            }]
            }
            attributes.append(weight)
        except:
            print('No weight data  provided')
        #================================================
        try:
            pixel_per_inch={
            "complex_id": 0,
            'id': monitor.pixel_per_inch.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.pixel_per_inch.attribute_screen_coating, 
            'dictionary_value_id': monitor.pixel_per_inch.dictionary_value_id,
            'value': monitor.pixel_per_inch.value,
            # 'is_required': monitor.pixel_per_inch.is_required
            }]
            }
            attributes.append(pixel_per_inch)
        except:
            print('No pixel_per_inch data  provided')
        #================================================
        try:
            curved_display={
            "complex_id": 0,
            'id': monitor.curved_display.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.curved_display.attribute_screen_coating, 
            'dictionary_value_id': monitor.curved_display.dictionary_value_id,
            'value': monitor.curved_display.value,
            # 'is_required': monitor.curved_display.is_required
            }]
            }
            attributes.append(curved_display)
        except:
            print('No curved_display data provided')
        #================================================
        try:
            response_time={
            "complex_id": 0,
            'id': monitor.response_time.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.response_time.attribute_screen_coating, 
            'dictionary_value_id': monitor.response_time.dictionary_value_id,
            'value': monitor.response_time.value,
            # 'is_required': monitor.response_time.is_required
            }]
            }
            attributes.append(response_time)
        except:
            print('No response_time data provided')
        #================================================
        try:
            monitor_matrix={
            "complex_id": 0,
            'id': monitor.monitor_matrix.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.monitor_matrix.attribute_screen_coating, 
            'dictionary_value_id': monitor.monitor_matrix.dictionary_value_id,
            'value': monitor.monitor_matrix.value,
            # 'is_required': monitor.monitor_matrix.is_required
            }]
            }
            attributes.append(monitor_matrix)
        except:
            print('No monitor_matrix data provided')
        #================================================
        try:
            hdr={
            "complex_id": 0,
            'id': monitor.hdr.attribute_id,
            "values": [{
            # 'attribute_screen_coating': monitor.hdr.attribute_screen_coating, 
            'dictionary_value_id': monitor.hdr.dictionary_value_id,
            'value': monitor.hdr.value,
            # 'is_required': monitor.hdr.is_required
            }]
            }
            attributes.append(hdr)
        except:
            print('No hdr data provided')





        #===============================Many To Many Fields======================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.country_of_manufacture.all():
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
            print ('No country_of_manufacture provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.lighting_type.all():
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
            print ('No lighting_type provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.adjustments.all():
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
            print ('No adjustment data provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.special_feature.all():
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
            print ('No special_feature provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.vesa_fixture.all():
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
            print ('No vesa_fixture provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.colour_monitor.all():
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
            print ('No colour_monitor provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.monitor_installation.all():
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
            print ('No monitor_installation data provided')
        #=====================================================
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.design_feature.all():
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
            print ('No design_feature data provided')
        #=====================================================   
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.monitor_application.all():
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
            print ('No monitor_application data provided')
        #=====================================================   
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.monitor_connector.all():
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
            print ('No monitor_connector data provided')
        #=====================================================   
        try:
            array=[]
            dict={"complex_id":0}
            for i in monitor.hdr_standard.all():
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
            print ('No hdr_standard data provided')
        #==========================================
        items=[{}]
        items=[{"attributes" : attributes, 
               "barcode": "",
                "description_category_id": 	17028926,
                "new_description_category_id": 0,
                "color_image": "",
                "complex_attributes": [],
                "currency_code": "RUB",
                "depth": "",
                "dimension_unit": "mm",
                "height": "100",
                "images":   [ monitor.image_1, 
                                monitor.image_2,
                                monitor.image_3
                            ],
                "images360": [],
                "name": monitor.name.value,
                "offer_id": "", #monitor.part_number.value,
                "old_price": "",
                "pdf_list": [],
                "price": "1000",
                "primary_image": "",
                "vat": "",
                "weight": "", #monitor.weight.value,
                "weight_unit": "g",
                "width":""
                 }]
        return items