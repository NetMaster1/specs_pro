from rest_framework import serializers
from .models import  Smartphone
from app_reference_shared.models import OzonCategory, ProcessorModel, Authentication

class SmartphoneSerializer(serializers.ModelSerializer):
    #category_name = serializers.StringRelatedField(source='category')#outputs string repsresentation of foreign key instead of id
    #processor_key = serializers.StringRelatedField(many=True)#outputs string repsresentation of foreign key instead of id
    
    warranty_period = serializers.SerializerMethodField('get_warranty_period')
    model_name = serializers.SerializerMethodField('get_model_name')
    тип = serializers.SerializerMethodField('get_type')
    hard_drive = serializers.SerializerMethodField('get_hard_drive')
        # страна_изготовления = serializers.SerializerMethodField('get_country_of_manufacture')
    тип_матрицы = serializers.SerializerMethodField('get_matrix_type')
    количество_сим_карт = serializers.SerializerMethodField('get_sim_card_qnty')
        # тип_карты_памяти = serializers.SerializerMethodField('get_card_type')
    bluetooth = serializers.SerializerMethodField('get_bluetooth')
        #navigation = serializers.SerializerMethodField('get_navigation')
        #sensor = serializers.SerializerMethodField('get_sensor')
        #sim_type = serializers.SerializerMethodField('get_sim_type')
        # модуль_связи_WiFi = serializers.SerializerMethodField('get_wifi_type')
    бренд_графического_процессора = serializers.SerializerMethodField('get_video_processor_brand')
    разрешение_экрана = serializers.SerializerMethodField('get_screen_resolution')
    качество_видео = serializers.SerializerMethodField('get_video_quality')
    модель_устройства = serializers.SerializerMethodField('get_gadget_model')
    степень_защиты = serializers.SerializerMethodField('get_protection_grade')
    линейка_мобильных_устройств = serializers.SerializerMethodField('get_gadget_series')
        # функции_камеры = serializers.SerializerMethodField('get_camera_function')
        # класс_опасности = serializers.SerializerMethodField('get_hazard_grade')
        # цвет = serializers.SerializerMethodField('get_colour')
    количество_основных_камер = serializers.SerializerMethodField('get_qnty_of_basic_cameras')
    процессор = serializers.SerializerMethodField('get_processor')
    видеопроцессор = serializers.SerializerMethodField('get_video_processor')
    бренд_процессора = serializers.SerializerMethodField('get_processor_brand')
    модель_процессора = serializers.SerializerMethodField('get_processor_model')
        # беспроводные_интерфейсы = serializers.SerializerMethodField('get_wireless_interface')
        # основной_материал_корпуса = serializers.SerializerMethodField('get_case_material')
    операционная_система = serializers.SerializerMethodField('get_operation_system')
    версия_андроид = serializers.SerializerMethodField('get_android_version')
    интерфейсы = serializers.SerializerMethodField('get_interface')
    слот_для_карты_памяти = serializers.SerializerMethodField('get_microsd_slot')
        # особенности = serializers.SerializerMethodField('get_special_feature')
        # функции_зарядки = serializers.SerializerMethodField('get_charging_function')
        # стабилизация = serializers.SerializerMethodField('get_stabilization')
        # аутентификация = serializers.SerializerMethodField('get_authentification')
    тип_корпуса = serializers.SerializerMethodField('get_case_form')
        # версия_iOS = serializers.SerializerMethodField('get_ios_version')
    ТН_ВЭД_коды_ЕАЭС = serializers.SerializerMethodField('get_euro_asian_code')
    поддержка_eSim = serializers.SerializerMethodField('get_esim_support')
    оперативная_память = serializers.SerializerMethodField('get_ram')
    год_анонсирования = serializers.SerializerMethodField('get_publishing_year')
    версия_смарфтона = serializers.SerializerMethodField('get_smartphone_version')
#=============================dictionary_id > 0============================
    каталожный_номер = serializers.SerializerMethodField('get_part_number')
    размер = serializers.SerializerMethodField('get_size')
    вес = serializers.SerializerMethodField('get_weight')
    комплектация = serializers.SerializerMethodField('get_product_set')
    front_camera_resolution = serializers.SerializerMethodField('get_front_camera_resolution')
    basic_camera_resolution = serializers.SerializerMethodField('get_basic_camera_resolution')
    battery_capacity = serializers.SerializerMethodField('get_battery_capacity')
    standby_period = serializers.SerializerMethodField('get_standby_period')
    work_period = serializers.SerializerMethodField('get_work_period')
    life_span = serializers.SerializerMethodField('get_life_span')
    record_max_speed = serializers.SerializerMethodField('get_record_max_speed')
    screen_size = serializers.SerializerMethodField('get_screen_size')
    seller_code = serializers.SerializerMethodField('get_seller_code')
    processor_frequency = serializers.SerializerMethodField('get_processor_frequency')
    marketing_colour = serializers.SerializerMethodField('get_marketing_colour')
  

    class Meta:
        model = Smartphone
        fields = [
        'model_name', 'sensor', 'name', 'каталожный_номер', 'размер', 'вес', 'комплектация', 'warranty_period', 'тип', 'hard_drive', 'description', 
        'marketing_text', 'country_of_manufacture', 'тип_матрицы', 'количество_сим_карт', 'card_type',
        'bluetooth', 'navigation', 'front_camera_resolution', 'basic_camera_resolution', 'battery_capacity','sim_type',
        'standby_period', 'wifi', 'бренд_графического_процессора', 'разрешение_экрана', 'качество_видео', 'модель_устройства',
        'степень_защиты', 'work_period', 'record_max_speed', 'life_span', 'screen_size', 'seller_code', 'линейка_мобильных_устройств',
        'camera_function', 'hazard_grade', 'colour', 'marketing_colour', 'количество_основных_камер', 'процессор', 'видеопроцессор',
        'бренд_процессора', 'processor_frequency', 'модель_процессора', 'wireless_interface', 'comms_standard', 'case_material', 'special_feature',
        'операционная_система','версия_андроид', 'интерфейсы', 'слот_для_карты_памяти', 'charging_function', 'stabilization', 'authentification',
        'тип_корпуса','ios_version', 'ТН_ВЭД_коды_ЕАЭС', 'поддержка_eSim', 'оперативная_память', 'год_анонсирования', 'версия_смарфтона'
        ]
        #fields ='__all__'
        depth=1#this field is crucial for displaying ManyToMany Field in serializer
        #Для вывода полей с ForeignField можно использовать функции get_smth или можно просто использовать параметр "depth=1"
        #exclude=['sensor.id']


    def get_model_name(self, smartphone):
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

        return model_name
    def get_part_number(self, smartphone):
        part_number={
            # 'attribute_name': smartphone.part_number.attribute_name, 
            'id': smartphone.part_number.attribute_id, 
            'value': smartphone.part_number.value, 
            'dictionary_value_id': smartphone.part_number.dictionary_value_id, 
            # 'is_required': smartphone.part_number.is_required
            }
        return part_number
    def get_size(self, smartphone):
        size={
            # 'attribute_name': smartphone.size.attribute_name, 
            'id': smartphone.size.attribute_id, 
            'value': smartphone.size.value, 
            'dictionary_value_id': smartphone.size.dictionary_value_id, 
            # 'is_required': smartphone.size.is_required
            }
        return size
    def get_weight(self, smartphone):
        weight={
            # 'attribute_name': smartphone.weight.attribute_name, 
            'id': smartphone.weight.attribute_id, 
            'value': smartphone.weight.value, 
            'dictionary_value_id': smartphone.weight.dictionary_value_id, 
            # 'is_required': smartphone.weight.is_required
            }
        return weight
    def get_product_set(self, smartphone):
        product_set={
        # 'attribute_name': smartphone.product_set.attribute_name, 
        'id': smartphone.product_set.attribute_id, 
        'value': smartphone.product_set.value, 
        'dictionary_value_id': smartphone.product_set.dictionary_value_id, 
        # 'is_required': smartphone.product_set.is_required
        }
        return product_set
    def get_front_camera_resolution(self, smartphone):
        front_camera_resolution={
            # 'attribute_name': smartphone.front_camera_resolution.attribute_name, 
            'id': smartphone.front_camera_resolution.attribute_id, 
            'value': smartphone.front_camera_resolution.value, 
            'dictionary_value_id': smartphone.front_camera_resolution.dictionary_value_id, 
            # 'is_required': smartphone.front_camera_resolution.is_required
            }
        return front_camera_resolution
    def get_basic_camera_resolution(self, smartphone):
        basic_camera_resolution={
            # 'attribute_name': smartphone.basic_camera_resolution.attribute_name, 
            'id': smartphone.basic_camera_resolution.attribute_id, 
            'value': smartphone.basic_camera_resolution.value, 
            'dictionary_value_id': smartphone.basic_camera_resolution.dictionary_value_id, 
            # 'is_required': smartphone.basic_camera_resolution.is_required
            }
        return basic_camera_resolution
    def get_battery_capacity(self, smartphone):
        battery_capacity={
            # 'attribute_name': smartphone.battery_capacity.attribute_name, 
            'id': smartphone.battery_capacity.attribute_id, 
            'value': smartphone.battery_capacity.value, 
            'dictionary_value_id': smartphone.battery_capacity.dictionary_value_id, 
            # 'is_required': smartphone.battery_capacity.is_required
            }
        return battery_capacity
    def get_standby_period(self, smartphone):
        standby_period={
            # 'attribute_name': smartphone.standby_period.attribute_name, 
            'id': smartphone.standby_period.attribute_id, 
            'value': smartphone.standby_period.value, 
            'dictionary_value_id': smartphone.standby_period.dictionary_value_id, 
            # 'is_required': smartphone.standby_period.is_required
            }
        return standby_period
    def get_work_period(self, smartphone):
        work_period={
            # 'attribute_name': smartphone.work_period.attribute_name, 
            'id': smartphone.work_period.attribute_id, 
            'value': smartphone.work_period.value, 
            'dictionary_value_id': smartphone.work_period.dictionary_value_id, 
            # 'is_required': smartphone.work_period.is_required
            }
        return work_period
    def get_life_span(self, smartphone):
        life_span={
            # 'attribute_name': smartphone.life_span.attribute_name, 
            'id': smartphone.life_span.attribute_id, 
            'value': smartphone.life_span.value, 
            'dictionary_value_id': smartphone.life_span.dictionary_value_id, 
            # 'is_required': smartphone.life_span.is_required
            }
        return life_span
    def get_record_max_speed(self, smartphone):
        record_max_speed={
            # 'attribute_name': smartphone.record_max_speed.attribute_name, 
            'id': smartphone.record_max_speed.attribute_id, 
            'value': smartphone.record_max_speed.value, 
            'dictionary_value_id': smartphone.record_max_speed.dictionary_value_id, 
            # 'is_required': smartphone.record_max_speed.is_required
            }
        return record_max_speed
    def get_screen_size(self, smartphone):
        screen_size={
            # 'attribute_name': smartphone.screen_size.attribute_name, 
            'id': smartphone.screen_size.attribute_id, 
            'value': smartphone.screen_size.value, 
            'dictionary_value_id': smartphone.screen_size.dictionary_value_id, 
            # 'is_required': smartphone.screen_size.is_required
            }
        return screen_size
    def get_seller_code(self, smartphone):
        seller_code={
            # 'attribute_name': smartphone.seller_code.attribute_name, 
            'id': smartphone.seller_code.attribute_id, 
            'value': smartphone.seller_code.value, 
            'dictionary_value_id': smartphone.seller_code.dictionary_value_id, 
            # 'is_required': smartphone.seller_code.is_required
            }
        return seller_code
    def get_processor_frequency(self, smartphone):
        processor_frequency={
            # 'attribute_name': smartphone.processor_frequency.attribute_name, 
            'id': smartphone.processor_frequency.attribute_id, 
            'value': smartphone.processor_frequency.value, 
            'dictionary_value_id': smartphone.processor_frequency.dictionary_value_id, 
            # 'is_required': smartphone.processor_frequency.is_required
            }
        return processor_frequency
    def get_marketing_colour(self, smartphone):
        marketing_colour={
            # 'attribute_name': smartphone.marketing_colour.attribute_name, 
            'id': smartphone.marketing_colour.attribute_id, 
            'value': smartphone.marketing_colour.value, 
            'dictionary_value_id': smartphone.marketing_colour.dictionary_value_id, 
            # 'is_required': smartphone.marketing_colour.is_required
            }
        return marketing_colour


#======================================dictionary_id > 0====================================
    def get_warranty_period(self, smartphone):
        warranty_period={
            # 'attribute_name': smartphone.warranty_period.attribute_name, 
            'id': smartphone.warranty_period.attribute_id, 
            'value': smartphone.warranty_period.value, 
            'dictionary_value_id': smartphone.warranty_period.dictionary_value_id, 
            # 'is_required': smartphone.warranty_period.is_required
            }
        return warranty_period
    def get_type(self, smartphone):
        type={
            # 'attribute_name': smartphone.type.attribute_name,
            'id': smartphone.type.attribute_id,
            'value': smartphone.type.value,
            'dictionary_value_id': smartphone.type.dictionary_value_id,
            # 'is_required': smartphone.type.is_required 
            }
        return type
    def get_hard_drive(self, smartphone):
        hard_drive={
            # 'attribute_name': smartphone.hard_drive.attribute_name,
            'id': smartphone.hard_drive.attribute_id,
            'value': smartphone.hard_drive.value,
            'dictionnary_value_id': smartphone.hard_drive.dictionary_value_id,
            # 'is_required': smartphone.hard_drive.is_required
            }
        return hard_drive
    # def get_country_of_manufacture(self, smartphone):
    #     country_of_manufacture={
    #         'attribute_name': smartphone.country_of_manufacture.attribute_name,
    #         'id': smartphone.country_of_manufacture.attribute_id, 
    #         'dictionary_value_id': smartphone.country_of_manufacture.dictionary_value_id, 
    #         'value': smartphone.country_of_manufacture.value, 
    #         'is_required': smartphone.country_of_manufacture.is_required}
        return country_of_manufacture
    def get_matrix_type(self, smartphone):
        matrix_type={
            # 'attribute_name': smartphone.matrix_type.attribute_name,
            'id': smartphone.matrix_type.attribute_id, 
            'dictionary_value_id': smartphone.matrix_type.dictionary_value_id, 
            'value': smartphone.matrix_type.value, 
            # 'is_required': smartphone.matrix_type.is_required
            }
        return matrix_type
    def get_sim_card_qnty(self, smartphone):
        sim_card_qnty={
            # 'attribute_name': smartphone.sim_card_qnty.attribute_name, 
            'id': smartphone.sim_card_qnty.attribute_id, 
            'dictionary_value_id': smartphone.sim_card_qnty.dictionary_value_id, 
            'value': smartphone.sim_card_qnty.value,
            # 'is_required': smartphone.sim_card_qnty.is_required
            }
        return sim_card_qnty
    # def get_card_type(self, smartphone):
    #     card_type={
    #         'attribute_name': smartphone.card_type.value, 
    #         'id': smartphone.card_type.attribute_id, 
    #         'dictionary_value_id': smartphone.card_type.dictionary_value_id, 
    #         'value': smartphone.card_type.value,
    #         'is_required': smartphone.card_type.is_required}
    #     return card_type
    def get_bluetooth(self, smartphone):
        bluetooth={
            # 'attribute_name': smartphone.bluetooth.attribute_name, 
            'attribute_id': smartphone.bluetooth.attribute_id, 
            'dictionary_value_id': smartphone.bluetooth.dictionary_value_id, 
            'value': smartphone.bluetooth.attribute_name,
            # 'is_required': smartphone.bluetooth.is_required
            }
        return bluetooth
    # def get_navigation(self, smartphone):
    #     navigation={
    #         'attribute_name': smartphone.navigation.attribute_name, 
    #         'attribute_id': smartphone.navigation.attribute_id, 
    #         'dictionary_value_id': smartphone.navigation.dictionary_value_id, 
    #         'value': smartphone.navigation.value,
    #         'is_required': smartphone.navigation.is_required}
    #     return navigation
    # def get_sensor(self, smartphone):
    #     sensor={
    #         'attribute_name': smartphone.sensor.attribute_name, 
    #         'attribute_id': smartphone.sensor.attribute_id, 
    #         'dictionary_value_id': smartphone.sensor.dictionary_value_id, 
    #         'value': smartphone.sensor.value,
    #         'is_required': smartphone.sensor.is_required}
    #     return sensor
    # def get_sim_type(self, smartphone):
    #     sim_type={
    #         'attribute_name': smartphone.sim_type.attribute_name, 
    #         'attribute_id': smartphone.sim_type.attribute_name, 
    #         'dictionary_value_id': smartphone.sim_type.dictionary_value_id, 
    #         'value': smartphone.sim_type.value,
    #         'is_required': smartphone.sim_type.is_required }
    #     return sim_type
    # def get_wifi_type(self, smartphone):
    #     wifi={
    #         'attribute_name': smartphone.wifi.attribute_name, 
    #         'attribute_id': smartphone.wifi.attribute_id, 
    #         'dictionary_value_id': smartphone.wifi.dictionary_value_id, 
    #         'value': smartphone.wifi.value,
    #         'is_required': smartphone.wifi.is_required}
    #     return wifi
    def get_video_processor_brand(self, smartphone):
        video_processor_brand={
            # 'attribute_name': smartphone.video_processor_brand.attribute_name, 
            'attribute_id': smartphone.video_processor_brand.attribute_id, 
            'dictionary_value_id': smartphone.video_processor_brand.dictionary_value_id, 
            'value': smartphone.video_processor_brand.value,
            # 'is_required': smartphone.video_processor.is_required
            }
        return video_processor_brand
    def get_screen_resolution(self, smartphone):
        screen_resolution={
            # 'attribute_name': smartphone.screen_resolution.attribute_name, 
            'attribute_id': smartphone.screen_resolution.attribute_id, 
            'dictionary_value_id': smartphone.screen_resolution.dictionary_value_id, 
            'value': smartphone.screen_resolution.value,
            # 'is_required': smartphone.screen_resolution.is_required
            }
        return screen_resolution
    def get_video_quality(self, smartphone):
        video_quality={
            # 'attribute_name': smartphone.video_quality.attribute_name, 
            'attribute_id': smartphone.video_quality.attribute_id, 
            'dictionary_value_id': smartphone.video_quality.dictionary_value_id, 
            'value': smartphone.video_quality.value,
            # 'is_required': smartphone.video_quality.is_required
            }
        return video_quality
    def get_gadget_model(self, smartphone):
        gadget_model={
            # 'attribute_name': smartphone.gadget_model.attribute_name, 
            'attribute_id': smartphone.gadget_model.attribute_id, 
            'dictionary_value_id': smartphone.gadget_model.dictionary_value_id, 
            'value': smartphone.gadget_model.value,
            # 'is_required': smartphone.gadget_model.is_required
            }
        return gadget_model
    def get_protection_grade(self, smartphone):
        protection_grade={
            # 'attribute_name': smartphone.protection_grade.attribute_name, 
            'attribute_id': smartphone.protection_grade.attribute_id, 
            'dictionary_value_id': smartphone.protection_grade.dictionary_value_id, 
            'value': smartphone.protection_grade.value,
            # 'is_required': smartphone.protection_grade.is_required
            }
        return protection_grade
    def get_gadget_series(self, smartphone):
        gadget_serie={
            # 'attribute_name': smartphone.gadget_serie.attribute_name, 
            'attribute_id': smartphone.gadget_serie.attribute_id, 
            'dictionary_value_id': smartphone.gadget_serie.dictionary_value_id, 
            'value': smartphone.gadget_serie.attribute_name,
            # 'is_required': smartphone.gadget_serie.is_required
            }
        return gadget_serie
    # def get_camera_function(self, smartphone):
    #     camera_function={
    #         'attribute_name': smartphone.camera_function.attribute_name, 
    #         'attribute_id': smartphone.camera_function.attribute_id, 
    #         'dictionary_value_id': smartphone.camera_function.dictionary_value_id, 
    #         'value': smartphone.camera_function.attribute_name,
    #         'is_required': smartphone.camera_function.is_required}
        return camera_function
    # def get_hazard_grade(self, smartphone):
    #     hazard_grade={
    #         'attribute_name': smartphone.hazard_grade.attribute_name, 
    #         'attribute_id': smartphone.hazard_grade.attribute_id, 
    #         'dictionary_value_id': smartphone.hazard_grade.dictionary_value_id, 
    #         'value': smartphone.hazard_grade.attribute_name,
    #         'is_required': smartphone.hazard_grade.is_required }
    #     return hazard_grade
    # def get_colour(self, smartphone):
    #     colour={
    #         'attribute_name': smartphone.colour.attribute_name, 
    #         'attribute_id': smartphone.colour.attribute_id, 
    #         'dictionary_value_id': smartphone.colour.dictionary_value_id, 
    #         'value': smartphone.colour.value,
    #         'is_required': smartphone.colour.is_required }
    #     return colour
    def get_qnty_of_basic_cameras(self, smartphone):
        qnty_of_basic_cameras={
            # 'attribute_name': smartphone.qnty_of_basic_cameras.attribute_name, 
            'attribute_id': smartphone.qnty_of_basic_cameras.attribute_id, 
            'dictionary_value_id': smartphone.qnty_of_basic_cameras.dictionary_value_id, 
            'value': smartphone.qnty_of_basic_cameras.value,
            # 'is_required': smartphone.qnty_of_basic_cameras.is_required
            }
        return qnty_of_basic_cameras
    def get_processor(self, smartphone):
        processor={
            # 'attribute_name': smartphone.processor.attribute_name, 
            'attribute_id': smartphone.processor.attribute_id, 
            'dictionary_value_id': smartphone.processor.dictionary_value_id, 
            'value': smartphone.processor.value,
            # 'is_required': smartphone.processor.is_required
            }
        return processor
    def get_video_processor(self, smartphone):
        video_processor={
            # 'attribute_name': smartphone.video_processor.attribute_name, 
            'attribute_id': smartphone.video_processor.value, 
            'dictionary_value_id': smartphone.video_processor.dictionary_value_id, 
            'value': smartphone.video_processor.value,
            # 'is_required': smartphone.video_processor.is_required
            }
        return video_processor
    def get_processor_brand(self, smartphone):
        processor_brand={
            # 'attribute_name': smartphone.processor_brand.attribute_name, 
            'attribute_id': smartphone.processor_brand.attribute_id, 
            'dictionary_value_id': smartphone.processor_brand.dictionary_value_id, 
            'value': smartphone.processor_brand.value,
            # 'is_required': smartphone.processor_brand.is_required
            }
        return processor_brand
    def get_processor_model(self, smartphone):
        processor_model={
            # 'attribute_name': smartphone.processor_model.attribute_name, 
            'attribute_id': smartphone.processor_model.attribute_id, 
            'dictionary_value_id': smartphone.processor_model.dictionary_value_id, 
            'value': smartphone.processor_model.value,
            # 'is_required': smartphone.processor_model.is_required
            }
        return processor_model
    # def get_wireless_interface(self, smartphone):
    #     wireless_interface={
    #         'attribute_name': smartphone.wireless_interface.attribute_name, 
    #         'attribute_id': smartphone.wireless_interface.attribute_id, 
    #         'dictionary_value_id': smartphone.wireless_interface.dictionary_value_id, 
    #         'value': smartphone.wireless_interface.value,
    #         'is_required': smartphone.wireless_interface.is_required}
    #     return wireless_interface
    # def get_case_material(self, smartphone):
    #     case_material={
    #         'attribute_name': smartphone.case_material.attribute_name, 
    #         'attribute_id': smartphone.case_material.attribute_id, 
    #         'dictionary_value_id': smartphone.case_material.dictionary_value_id, 
    #         'value': smartphone.case_material.value,
    #         'is_required': smartphone.case_material.is_required}
    #     return case_material
    def get_operation_system(self, smartphone):
        operation_system={
            # 'attribute_name': smartphone.operation_system.attribute_name, 
            'attribute_id': smartphone.operation_system.attribute_id, 
            'dictionary_value_id': smartphone.operation_system.dictionary_value_id, 
            'value': smartphone.operation_system.value,
            # 'is_required': smartphone.operation_system.is_required 
            }
        return operation_system
    def get_android_version(self, smartphone):
        android_version={
            # 'attribute_name': smartphone.android_version.attribute_name, 
            'attribute_id': smartphone.android_version.attribute_id, 
            'dictionary_value_id': smartphone.android_version.dictionary_value_id, 
            'value': smartphone.android_version.value,
            # 'is_required': smartphone.android_version.is_required
            }
        return android_version
    def get_interface(self, smartphone):
        interface={
            # 'attribute_name': smartphone.interface.attribute_name, 
            'attribute_id': smartphone.interface.attribute_id, 
            'dictionary_value_id': smartphone.interface.dictionary_value_id, 
            'value': smartphone.interface.value,
            # 'is_required': smartphone.interface.is_required
            }
        return interface
    def get_microsd_slot(self, smartphone):
        microsd_slot={
            # 'attribute_name': smartphone.microsd_slot.attribute_name, 
            'attribute_id': smartphone.microsd_slot.attribute_id, 
            'dictionary_value_id': smartphone.microsd_slot.dictionary_value_id, 
            'value': smartphone.microsd_slot.attribute_name,
            # 'is_required': smartphone.microsd_slot.is_required 
            }
        return microsd_slot
    # def get_special_feature(self, smartphone):
    #     special_feature={
    #         'attribute_name': smartphone.special_feature.attribute_name, 
    #         'attriubte_id': smartphone.special_feature.attribute_id, 
    #         'dictionary_value_id': smartphone.special_feature.dictionary_value_id, 
    #         'value': smartphone.special_feature.value,
    #         'is_required': smartphone.special_feature.is_required}
    #     return special_feature
    # def get_charging_function(self, smartphone):
    #     charging_function={
    #         'attribute_name': smartphone.charging_function.attribute_name, 
    #         'attribute_id': smartphone.charging_function.attribute_id, 
    #         'dictionary_value_id': smartphone.charging_function.dictionary_value_id, 
    #         'value': smartphone.charging_function.attribute_name,
    #         'is_required': smartphone.charging_function.is_required}
    #     return charging_function
    # def get_stabilization(self, smartphone):
    #     stabilization={
    #         'attribute_name': smartphone.stabilization.attribute_name, 
    #         'attribute_id': smartphone.stabilization.attribute_id, 
    #         'dictionary_value_id': smartphone.stabilization.dictionary_value_id, 
    #         'value': smartphone.stabilization.value,
    #         'is_required': smartphone.stabilization.is_required}
    #     return stabilization
    # def get_authentification(self, smartphone):
    #     authentification={
    #         'attribute_name': smartphone.authentification.attribute_name, 
    #         'attribute_id': smartphone.authentification.attribute_id, 
    #         'dictionary_value_id': smartphone.authentification.dictionary_value_id, 
    #         'value': smartphone.authentification.value,
    #         'is_required': smartphone.authentification.is_required }
    #     return authentification
    def get_case_form(self, smartphone):
        case_form={
            # 'attribute_name': smartphone.case_form.attribute_name, 
            'attribute_id': smartphone.case_form.attribute_name, 
            'dictionary_value_id': smartphone.case_form.dictionary_value_id, 
            'value': smartphone.case_form.value,
            # 'is_required': smartphone.case_form.is_required
            }
        return case_form
    # def get_ios_version(self, smartphone):
    #     ios_version={
    #         'attribute_name': smartphone.ios_version.attribute_name, 
    #         'attribute_id': smartphone.ios_version.attribute_id, 
    #         'dictionary_value_id': smartphone.ios_version.dictionary_value_id, 
    #         'value': smartphone.ios_version.value,
    #         'is_required': smartphone.ios_version.is_required}
        return ios_version
    def get_euro_asian_code(self, smartphone):
        euro_asian_code={
            # 'attribute_name': smartphone.euro_asian_code.attribute_name, 
            'attribute_id': smartphone.euro_asian_code.attribute_id, 
            'dictionary_value_id': smartphone.euro_asian_code.dictionary_value_id, 
            'value': smartphone.euro_asian_code.value,
            # 'is_required': smartphone.euro_asian_code.is_required
            }
        return euro_asian_code
    def get_esim_support(self, smartphone):
        esim_support={
            # 'attribute_name': smartphone.esim_support.attribute_name, 
            'attribute_id': smartphone.esim_support.attribute_id, 
            'dictionary_value_id': smartphone.esim_support.dictionary_value_id, 
            'value': smartphone.esim_support.value,
            # 'is_required': smartphone.esim_support.is_required
            }
        return esim_support
    def get_ram(self, smartphone):
        ram={
            # 'attribute_name': smartphone.ram.attribute_name, 
            'attribute_id': smartphone.ram.attribute_id, 
            'dictionary_value_id': smartphone.ram.dictionary_value_id, 
            'value': smartphone.ram.value,
            # 'is_required': smartphone.ram.is_required
            }
        return ram
    def get_publishing_year(self, smartphone):
        publishing_year={
            # 'attribute_name': smartphone.publishing_year.attribute_name, 
            'attribure_id': smartphone.publishing_year.attribute_id, 
            'dictionary_value_id': smartphone.publishing_year.dictionary_value_id, 
            'value': smartphone.publishing_year.value,
            # 'is_required': smartphone.publishing_year.is_required
            }
        return publishing_year
    def get_smartphone_version(self, smartphone):
        smartphone_version={
            # 'attribute_name': smartphone.smartphone_version.attribute_name, 
            'attribute_id': smartphone.smartphone_version.attribute_id, 
            'dictionary_value_id': smartphone.smartphone_version.dictionary_value_id, 
            'value': smartphone.smartphone_version.value
            # 'is_required': smartphone.smartphone_version.is_required
        }
        return smartphone_version

# class SmartphoneCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = ('name', 'url', 'id')
#         #fields = ('id', 'name')
#         