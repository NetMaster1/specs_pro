from rest_framework import serializers
from .models import  Smartphone
from app_reference_shared.models import OzonCategory, ProcessorModel, Authentication

class SmartphoneSerializer(serializers.ModelSerializer):
    #category_name = serializers.StringRelatedField(source='category')#outputs string repsresentation of foreign key instead of id
    #processor_key = serializers.StringRelatedField(many=True)#outputs string repsresentation of foreign key instead of id
    
    warranty_period = serializers.SerializerMethodField('get_warranty_period')
    model_name = serializers.SerializerMethodField('get_model_name')
    тип = serializers.SerializerMethodField('get_type')
    встроенная_память = serializers.SerializerMethodField('get_hard_drive')
    страна_изготовления = serializers.SerializerMethodField('get_country_of_manufacture')
    тип_матрицы = serializers.SerializerMethodField('get_matrix_type')
    количество_сим_карт = serializers.SerializerMethodField('get_sim_card_qnty')
    тип_карты_памяти = serializers.SerializerMethodField('get_card_type')
    bluetooth = serializers.SerializerMethodField('get_bluetooth')
    navigation = serializers.SerializerMethodField('get_navigation')
    sensor = serializers.SerializerMethodField('get_sensor')
    sim_type = serializers.SerializerMethodField('get_sim_type')
    модуль_связи_WiFi = serializers.SerializerMethodField('get_wifi_type')
    бренд_графического_процессора = serializers.SerializerMethodField('get_video_processor_brand')
    разрешение_экрана = serializers.SerializerMethodField('get_screen_resolution')
    качество_видео = serializers.SerializerMethodField('get_video_quality')
    модель_устройства = serializers.SerializerMethodField('get_gadget_model')
    степень_защиты = serializers.SerializerMethodField('get_protection_grade')
    линейка_мобильных_устройств = serializers.SerializerMethodField('get_gadget_series')
    функции_камеры = serializers.SerializerMethodField('get_camera_function')
    класс_опасности = serializers.SerializerMethodField('get_hazard_grade')
    цвет = serializers.SerializerMethodField('get_colour')
    количество_основных_камер = serializers.SerializerMethodField('get_qnty_of_basic_cameras')
    процессор = serializers.SerializerMethodField('get_processor')
    видеопроцессор = serializers.SerializerMethodField('get_video_processor')
    бренд_процессора = serializers.SerializerMethodField('get_processor_brand')
    модель_процессора = serializers.SerializerMethodField('get_processor_model')
    беспроводные_интерфейсы = serializers.SerializerMethodField('get_wireless_interface')
    основной_материал_корпуса = serializers.SerializerMethodField('get_case_material')
    операционная_система = serializers.SerializerMethodField('get_operation_system')
    версия_андроид = serializers.SerializerMethodField('get_android_version')
    интерфейсы = serializers.SerializerMethodField('get_interface')
    слот_для_карты_памяти = serializers.SerializerMethodField('get_microsd_slot')
    особенности = serializers.SerializerMethodField('get_special_feature')
    функции_зарядки = serializers.SerializerMethodField('get_charging_function')
    стабилизация = serializers.SerializerMethodField('get_stabilization')
    аутентификация = serializers.SerializerMethodField('get_authentification')
    тип_корпуса = serializers.SerializerMethodField('get_case_form')
    версия_iOS = serializers.SerializerMethodField('get_ios_version')
    ТН_ВЭД_коды_ЕАЭС = serializers.SerializerMethodField('get_euro_asian_code')
    поддержка_eSim = serializers.SerializerMethodField('get_esim_support')
    оперативная_память = serializers.SerializerMethodField('get_ram')
    год_анонсирования = serializers.SerializerMethodField('get_publishing_year')
    версия_смарфтона = serializers.SerializerMethodField('get_smartphone_version')


    class Meta:
        model = Smartphone
        fields = [
        'name', 'part_number', 'warranty_period', 'тип', 'model_name', 'встроенная_память', 'description', 
        'marketing_text', 'size', 'weight', 'product_set', 'страна_изготовления', 'тип_матрицы', 'количество_сим_карт', 'тип_карты_памяти',
        'bluetooth', 'navigation', 'sensor', 'front_camera_resolution', 'basic_camera_resolution', 'battery_capacity','sim_type',
        'standby_period', 'модуль_связи_WiFi', 'бренд_графического_процессора', 'разрешение_экрана', 'качество_видео', 'модель_устройства',
        'степень_защиты', 'work_period', 'record_max_speed', 'life_span', 'screen_size', 'seller_code', 'линейка_мобильных_устройств',
        'функции_камеры', 'класс_опасности', 'цвет', 'marketing_colour', 'количество_основных_камер', 'процессор', 'видеопроцессор',
        'бренд_процессора', 'processor_frequency', 'модель_процессора', 'беспроводные_интерфейсы', 'основной_материал_корпуса', 'операционная_система',
        'версия_андроид', 'интерфейсы', 'слот_для_карты_памяти', 'особенности', 'функции_зарядки', 'стабилизация', 'аутентификация', 'тип_корпуса',
        'версия_iOS', 'ТН_ВЭД_коды_ЕАЭС', 'поддержка_eSim', 'оперативная_память', 'год_анонсирования', 'версия_смарфтона', 'EAN'
        ]
        #fields ='__all__'

    def get_model_name(self, smartphone):
        model_name={'attribute_name': smartphone.model_name.attribute_name, 'id': smartphone.model_name.attribute_id, 'value': smartphone.model_name.name, 'dictionary_value_id': smartphone.model_name.digital_code, }
        return model_name
    def get_warranty_period(self, smartphone):
        warranty_period={'attribute_name': smartphone.warranty_period.attribute_name, 'id': smartphone.warranty_period.attribute_id, 'value': smartphone.warranty_period.name, 'dictionary_value_id': smartphone.warranty_period.digital_code, }
        return warranty_period
    def get_type(self, smartphone):
        type={'attribute_name': smartphone.type.attribute_name, 'id': smartphone.type.attribute_id, 'value': smartphone.type.name, 'dictionary_value_id': smartphone.type.digital_code, }
        return type
    def get_hard_drive(self, smartphone):
        hard_drive={'attribute_name': smartphone.hard_drive.attribute_name, 'id': smartphone.hard_drive.attribute_id,'value': smartphone.hard_drive.name, 'dictionnary_value_id': smartphone.hard_drive.digital_code}
        return hard_drive
    def get_country_of_manufacture(self, smartphone):
        country_of_manufacture={'id': smartphone.country_of_manufacture.name, 'dictionary_value_id': smartphone.country_of_manufacture.digital_code, 'value': smartphone.country_of_manufacture.attribute_name}
        return country_of_manufacture
    def get_matrix_type(self, smartphone):
        matrix_type={'id': smartphone.matrix_type.name, 'dictionary_value_id': smartphone.matrix_type.digital_code, 'value': smartphone.matrix_type.attribute_name}
        return matrix_type
    def get_sim_card_qnty(self, smartphone):
        sim_card_qnty={'id': smartphone.sim_card_qnty.name, 'dictionary_value_id': smartphone.sim_card_qnty.digital_code, 'value': smartphone.sim_card_qnty.attribute_name}
        return sim_card_qnty
    def get_card_type(self, smartphone):
        card_type={'id': smartphone.card_type.name, 'dictionary_value_id': smartphone.card_type.digital_code, 'value': smartphone.card_type.attribute_name}
        return card_type
    def get_bluetooth(self, smartphone):
        bluetooth={'id': smartphone.bluetooth.name, 'dictionary_value_id': smartphone.bluetooth.digital_code, 'value': smartphone.bluetooth.attribute_name}
        return bluetooth
    def get_navigation(self, smartphone):
        navigation={'id': smartphone.navigation.name, 'dictionary_value_id': smartphone.navigation.digital_code, 'value': smartphone.navigation.attribute_name}
        return navigation
    def get_sensor(self, smartphone):
        sensor={'id': smartphone.sensor.name, 'dictionary_value_id': smartphone.sensor.digital_code, 'value': smartphone.sensor.attribute_name}
        return sensor
    def get_sim_type(self, smartphone):
        sim_type={'id': smartphone.sim_type.name, 'dictionary_value_id': smartphone.sim_type.digital_code, 'value': smartphone.sim_type.attribute_name}
        return sim_type
    def get_wifi_type(self, smartphone):
        wifi={'id': smartphone.wifi.name, 'dictionary_value_id': smartphone.wifi.digital_code, 'value': smartphone.wifi.attribute_name}
        return wifi
    def get_video_processor_brand(self, smartphone):
        video_processor_brand={'id': smartphone.video_processor_brand.name, 'dictionary_value_id': smartphone.video_processor_brand.digital_code, 'value': smartphone.video_processor_brand.attribute_name}
        return video_processor_brand
    def get_screen_resolution(self, smartphone):
        screen_resolution={'id': smartphone.screen_resolution.name, 'dictionary_value_id': smartphone.screen_resolution.digital_code, 'value': smartphone.screen_resolution.attribute_name}
        return screen_resolution
    def get_video_quality(self, smartphone):
        video_quality={'id': smartphone.video_quality.name, 'dictionary_value_id': smartphone.video_quality.digital_code, 'value': smartphone.video_quality.attribute_name}
        return video_quality
    def get_gadget_model(self, smartphone):
        gadget_model={'id': smartphone.gadget_model.name, 'dictionary_value_id': smartphone.gadget_model.digital_code, 'value': smartphone.gadget_model.attribute_name}
        return gadget_model
    def get_protection_grade(self, smartphone):
        protection_grade={'id': smartphone.protection_grade.name, 'dictionary_value_id': smartphone.protection_grade.digital_code, 'value': smartphone.protection_grade.attribute_name}
        return protection_grade
    def get_gadget_series(self, smartphone):
        gadget_serie={'id': smartphone.gadget_serie.name, 'dictionary_value_id': smartphone.gadget_serie.digital_code, 'value': smartphone.gadget_serie.attribute_name}
        return gadget_serie
    def get_camera_function(self, smartphone):
        camera_function={'id': smartphone.camera_function.name, 'dictionary_value_id': smartphone.camera_function.digital_code, 'value': smartphone.camera_function.attribute_name}
        return camera_function
    def get_hazard_grade(self, smartphone):
        hazard_grade={'id': smartphone.hazard_grade.name, 'dictionary_value_id': smartphone.hazard_grade.digital_code, 'value': smartphone.hazard_grade.attribute_name}
        return hazard_grade
    def get_colour(self, smartphone):
        colour={'id': smartphone.colour.name, 'dictionary_value_id': smartphone.colour.digital_code, 'value': smartphone.colour.attribute_name}
        return colour
    def get_qnty_of_basic_cameras(self, smartphone):
        qnty_of_basic_cameras={'id': smartphone.qnty_of_basic_cameras.name, 'dictionary_value_id': smartphone.qnty_of_basic_cameras.digital_code, 'value': smartphone.qnty_of_basic_cameras.attribute_name}
        return qnty_of_basic_cameras
    def get_processor(self, smartphone):
        processor={'id': smartphone.processor.name, 'dictionary_value_id': smartphone.processor.digital_code, 'value': smartphone.processor.attribute_name}
        return processor
    def get_video_processor(self, smartphone):
        video_processor={'id': smartphone.video_processor.name, 'dictionary_value_id': smartphone.video_processor.digital_code, 'value': smartphone.video_processor.attribute_name}
        return video_processor
    def get_processor_brand(self, smartphone):
        processor_brand={'id': smartphone.processor_brand.name, 'dictionary_value_id': smartphone.processor_brand.digital_code, 'value': smartphone.processor_brand.attribute_name}
        return processor_brand
    def get_processor_model(self, smartphone):
        processor_model={'id': smartphone.processor_model.name, 'dictionary_value_id': smartphone.processor_model.digital_code, 'value': smartphone.processor_model.attribute_name}
        return processor_model
    def get_wireless_interface(self, smartphone):
        wireless_interface={'id': smartphone.wireless_interface.name, 'dictionary_value_id': smartphone.wireless_interface.digital_code, 'value': smartphone.wireless_interface.attribute_name}
        return wireless_interface
    def get_case_material(self, smartphone):
        case_material={'id': smartphone.case_material.name, 'dictionary_value_id': smartphone.case_material.digital_code, 'value': smartphone.case_material.attribute_name}
        return case_material
    def get_operation_system(self, smartphone):
        operation_system={'id': smartphone.operation_system.name, 'dictionary_value_id': smartphone.operation_system.digital_code, 'value': smartphone.operation_system.attribute_name}
        return operation_system
    def get_android_version(self, smartphone):
        android_version={'id': smartphone.android_version.name, 'dictionary_value_id': smartphone.android_version.digital_code, 'value': smartphone.android_version.attribute_name}
        return android_version
    def get_interface(self, smartphone):
        interface={'id': smartphone.interface.name, 'dictionary_value_id': smartphone.interface.digital_code, 'value': smartphone.interface.attribute_name}
        return interface
    def get_microsd_slot(self, smartphone):
        microsd_slot={'id': smartphone.microsd_slot.name, 'dictionary_value_id': smartphone.microsd_slot.digital_code, 'value': smartphone.microsd_slot.attribute_name}
        return microsd_slot
    def get_special_feature(self, smartphone):
        special_feature={'id': smartphone.special_feature.name, 'dictionary_value_id': smartphone.special_feature.digital_code, 'value': smartphone.special_feature.attribute_name}
        return special_feature
    def get_charging_function(self, smartphone):
        charging_function={'id': smartphone.charging_function.name, 'dictionary_value_id': smartphone.charging_function.digital_code, 'value': smartphone.charging_function.attribute_name}
        return charging_function
    def get_stabilization(self, smartphone):
        Stabilization={'id': smartphone.Stabilization.name, 'dictionary_value_id': smartphone.Stabilization.digital_code, 'value': smartphone.Stabilization.attribute_name}
        return Stabilization
    def get_authentification(self, smartphone):
        authentification={'id': smartphone.authentification.name, 'dictionary_value_id': smartphone.authentification.digital_code, 'value': smartphone.authentification.attribute_name}
        return authentification
    def get_case_form(self, smartphone):
        case_form={'id': smartphone.case_form.name, 'dictionary_value_id': smartphone.case_form.digital_code, 'value': smartphone.case_form.attribute_name}
        return case_form
    def get_ios_version(self, smartphone):
        ios_version={'id': smartphone.ios_version.name, 'dictionary_value_id': smartphone.ios_version.digital_code, 'value': smartphone.ios_version.attribute_name}
        return ios_version
    def get_euro_asian_code(self, smartphone):
        euro_asian_code={'id': smartphone.euro_asian_code.name, 'dictionary_value_id': smartphone.euro_asian_code.digital_code, 'value': smartphone.euro_asian_code.attribute_name}
        return euro_asian_code
    def get_esim_support(self, smartphone):
        esim_support={'id': smartphone.esim_support.name, 'dictionary_value_id': smartphone.esim_support.digital_code, 'value': smartphone.esim_support.attribute_name}
        return esim_support
    def get_ram(self, smartphone):
        ram={'id': smartphone.ram.name, 'dictionary_value_id': smartphone.ram.digital_code, 'value': smartphone.ram.attribute_name}
        return ram
    def get_publishing_year(self, smartphone):
        publishing_year={'id': smartphone.publishing_year.name, 'dictionary_value_id': smartphone.publishing_year.digital_code, 'value': smartphone.publishing_year.attribute_name}
        return publishing_year
    def get_smartphone_version(self, smartphone):
        smartphone_version={'id': smartphone.smartphone_version.name, 'dictionary_value_id': smartphone.smartphone_version.digital_code, 'value': smartphone.smartphone_version.attribute_name}
        return smartphone_version

# class SmartphoneCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = ('name', 'url', 'id')
#         #fields = ('id', 'name')
#         