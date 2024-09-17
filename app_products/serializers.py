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
    # катложный_номер = serializers.SerializerMethodField('get_part_number')


    class Meta:
        model = Smartphone
        fields = [
        'name', 'каталожный_номер', 'warranty_period', 'тип', 'model_name', 'hard_drive', 'description', 
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
        model_name={
            'attribute_name': smartphone.model_name.attribute_name, 
            'id': smartphone.model_name.attribute_id, 
            'value': smartphone.model_name.name, 
            'dictionary_value_id': smartphone.model_name.digital_code, 
            'is_required': smartphone.model_name.is_required}
        return model_name
    # def get_part_number(self, smartphone):
    #     model_name={
    #         'attribute_name': smartphone.model_name.attribute_name, 
    #         'id': smartphone.model_name.attribute_id, 
    #         'value': smartphone.model_name.name, 
    #         'dictionary_value_id': smartphone.model_name.digital_code, 
    #         'is_required': smartphone.model_name.is_required}
    #     return model_name

    def get_warranty_period(self, smartphone):
        warranty_period={
            'attribute_name': smartphone.warranty_period.attribute_name, 
            'id': smartphone.warranty_period.attribute_id, 
            'value': smartphone.warranty_period.name, 
            'dictionary_value_id': smartphone.warranty_period.digital_code, 
            'is_required': smartphone.warranty_period.is_required}
        return warranty_period
    def get_type(self, smartphone):
        type={
            'attribute_name': smartphone.type.attribute_name,
            'id': smartphone.type.attribute_id,
            'value': smartphone.type.name,
            'dictionary_value_id': smartphone.type.digital_code,
            'is_required': smartphone.type.is_required }
        return type
    def get_hard_drive(self, smartphone):
        hard_drive={
            'attribute_name': smartphone.hard_drive.attribute_name,
            'id': smartphone.hard_drive.attribute_id,
            'value': smartphone.hard_drive.name,
            'dictionnary_value_id': smartphone.hard_drive.digital_code,
            'is_required': smartphone.hard_drive.is_required}
        return hard_drive
    def get_country_of_manufacture(self, smartphone):
        country_of_manufacture={
            'attribute_name': smartphone.country_of_manufacture.attribute_name,
            'id': smartphone.country_of_manufacture.attribute_id, 
            'dictionary_value_id': smartphone.country_of_manufacture.digital_code, 
            'value': smartphone.country_of_manufacture.name, 
            'is_required': smartphone.country_of_manufacture.is_required}
        return country_of_manufacture
    def get_matrix_type(self, smartphone):
        matrix_type={
            'attribute_name': smartphone.matrix_type.attribute_name,
            'id': smartphone.matrix_type.attribute_id, 
            'dictionary_value_id': smartphone.matrix_type.digital_code, 
            'value': smartphone.matrix_type.name, 
            'is_required': smartphone.matrix_type.is_required}
        return matrix_type
    def get_sim_card_qnty(self, smartphone):
        sim_card_qnty={
            'attribute_name': smartphone.sim_card_qnty.attribute_name, 
            'id': smartphone.sim_card_qnty.attribute_id, 
            'dictionary_value_id': smartphone.sim_card_qnty.digital_code, 
            'value': smartphone.sim_card_qnty.name,
            'is_required': smartphone.sim_card_qnty.is_required}
        return sim_card_qnty
    def get_card_type(self, smartphone):
        card_type={
            'attribute_name': smartphone.card_type.name, 
            'id': smartphone.card_type.attribute_id, 
            'dictionary_value_id': smartphone.card_type.digital_code, 
            'value': smartphone.card_type.name,
            'is_required': smartphone.card_type.is_required}
        return card_type
    def get_bluetooth(self, smartphone):
        bluetooth={
            'attribute_name': smartphone.bluetooth.attribute_name, 
            'attribute_id': smartphone.bluetooth.attribute_id, 
            'dictionary_value_id': smartphone.bluetooth.digital_code, 
            'value': smartphone.bluetooth.attribute_name,
            'is_required': smartphone.bluetooth.is_required}
        return bluetooth
    def get_navigation(self, smartphone):
        navigation={
            'attribute_name': smartphone.navigation.attribute_name, 
            'attribute_id': smartphone.navigation.attribute_id, 
            'dictionary_value_id': smartphone.navigation.digital_code, 
            'value': smartphone.navigation.name,
            'is_required': smartphone.navigation.is_required}
        return navigation
    def get_sensor(self, smartphone):
        sensor={
            'attribute_name': smartphone.sensor.attribute_name, 
            'attribute_id': smartphone.sensor.attribute_id, 
            'dictionary_value_id': smartphone.sensor.digital_code, 
            'value': smartphone.sensor.name,
            'is_required': smartphone.sensor.is_required}
        return sensor
    def get_sim_type(self, smartphone):
        sim_type={
            'attribute_name': smartphone.sim_type.attribute_name, 
            'attribute_id': smartphone.sim_type.attribute_name, 
            'dictionary_value_id': smartphone.sim_type.digital_code, 
            'value': smartphone.sim_type.name,
            'is_required': smartphone.sim_type.is_required }
        return sim_type
    def get_wifi_type(self, smartphone):
        wifi={
            'attribute_name': smartphone.wifi.attribute_name, 
            'attribute_id': smartphone.wifi.attribute_id, 
            'dictionary_value_id': smartphone.wifi.digital_code, 
            'value': smartphone.wifi.name,
            'is_required': smartphone.wifi.is_required}
        return wifi
    def get_video_processor_brand(self, smartphone):
        video_processor_brand={
            'attribute_name': smartphone.video_processor_brand.attribute_name, 
            'attribute_id': smartphone.video_processor_brand.attribute_id, 
            'dictionary_value_id': smartphone.video_processor_brand.digital_code, 
            'value': smartphone.video_processor_brand.name,
            'is_required': smartphone.video_processor.is_required}
        return video_processor_brand
    def get_screen_resolution(self, smartphone):
        screen_resolution={
            'attribute_name': smartphone.screen_resolution.attribute_name, 
            'attribute_id': smartphone.screen_resolution.attribute_id, 
            'dictionary_value_id': smartphone.screen_resolution.digital_code, 
            'value': smartphone.screen_resolution.name,
            'is_required': smartphone.screen_resolution.is_required}
        return screen_resolution
    def get_video_quality(self, smartphone):
        video_quality={
            'attribute_name': smartphone.video_quality.attribute_name, 
            'attribute_id': smartphone.video_quality.attribute_id, 
            'dictionary_value_id': smartphone.video_quality.digital_code, 
            'value': smartphone.video_quality.name,
            'is_required': smartphone.video_quality.is_required}
        return video_quality
    def get_gadget_model(self, smartphone):
        gadget_model={
            'attribute_name': smartphone.gadget_model.attribute_name, 
            'attribute_id': smartphone.gadget_model.attribute_id, 
            'dictionary_value_id': smartphone.gadget_model.digital_code, 
            'value': smartphone.gadget_model.name,
            'is_required': smartphone.gadget_model.is_required}
        return gadget_model
    def get_protection_grade(self, smartphone):
        protection_grade={
            'attribute_name': smartphone.protection_grade.attribute_name, 
            'attribute_id': smartphone.protection_grade.attribute_id, 
            'dictionary_value_id': smartphone.protection_grade.digital_code, 
            'value': smartphone.protection_grade.name,
            'is_required': smartphone.protection_grade.is_required}
        return protection_grade
    def get_gadget_series(self, smartphone):
        gadget_serie={
            'attribute_name': smartphone.gadget_serie.attribute_name, 
            'attribute_id': smartphone.gadget_serie.attribute_id, 
            'dictionary_value_id': smartphone.gadget_serie.digital_code, 
            'value': smartphone.gadget_serie.attribute_name,
            'is_required': smartphone.gadget_serie.is_required}
        return gadget_serie
    def get_camera_function(self, smartphone):
        camera_function={
            'attribute_name': smartphone.camera_function.attribute_name, 
            'attribute_id': smartphone.camera_function.attribute_id, 
            'dictionary_value_id': smartphone.camera_function.digital_code, 
            'value': smartphone.camera_function.attribute_name,
            'is_required': smartphone.camera_function.is_required}
        return camera_function
    def get_hazard_grade(self, smartphone):
        hazard_grade={
            'attribute_name': smartphone.hazard_grade.attribute_name, 
            'attribute_id': smartphone.hazard_grade.attribute_id, 
            'dictionary_value_id': smartphone.hazard_grade.digital_code, 
            'value': smartphone.hazard_grade.attribute_name,
            'is_required': smartphone.hazard_grade.is_required }
        return hazard_grade
    def get_colour(self, smartphone):
        colour={
            'attribute_name': smartphone.colour.attribute_name, 
            'attribute_id': smartphone.colour.attribute_id, 
            'dictionary_value_id': smartphone.colour.digital_code, 
            'value': smartphone.colour.name,
            'is_required': smartphone.colour.is_required }
        return colour
    def get_qnty_of_basic_cameras(self, smartphone):
        qnty_of_basic_cameras={
            'attribute_name': smartphone.qnty_of_basic_cameras.attribute_name, 
            'attribute_id': smartphone.qnty_of_basic_cameras.attribute_id, 
            'dictionary_value_id': smartphone.qnty_of_basic_cameras.digital_code, 
            'value': smartphone.qnty_of_basic_cameras.name,
            'is_required': smartphone.qnty_of_basic_cameras.is_required}
        return qnty_of_basic_cameras
    def get_processor(self, smartphone):
        processor={
            'attribute_name': smartphone.processor.attribute_name, 
            'attribute_id': smartphone.processor.attribute_id, 
            'dictionary_value_id': smartphone.processor.digital_code, 
            'value': smartphone.processor.name,
            'is_required': smartphone.processor.is_required}
        return processor
    def get_video_processor(self, smartphone):
        video_processor={
            'attribute_name': smartphone.video_processor.attribute_name, 
            'attribute_id': smartphone.video_processor.name, 
            'dictionary_value_id': smartphone.video_processor.digital_code, 
            'value': smartphone.video_processor.name,
            'is_required': smartphone.video_processor.is_required }
        return video_processor
    def get_processor_brand(self, smartphone):
        processor_brand={
            'attribute_name': smartphone.processor_brand.attribute_name, 
            'attribute_id': smartphone.processor_brand.attribute_id, 
            'dictionary_value_id': smartphone.processor_brand.digital_code, 
            'value': smartphone.processor_brand.name,
            'is_required': smartphone.processor_brand.is_required}
        return processor_brand
    def get_processor_model(self, smartphone):
        processor_model={
            'attribute_name': smartphone.processor_model.attribute_name, 
            'attribute_id': smartphone.processor_model.attribute_id, 
            'dictionary_value_id': smartphone.processor_model.digital_code, 
            'value': smartphone.processor_model.name,
            'is_required': smartphone.processor_model.is_required}
        return processor_model
    def get_wireless_interface(self, smartphone):
        wireless_interface={
            'attribute_name': smartphone.wireless_interface.attribute_name, 
            'attribute_id': smartphone.wireless_interface.attribute_id, 
            'dictionary_value_id': smartphone.wireless_interface.digital_code, 
            'value': smartphone.wireless_interface.name,
            'is_required': smartphone.wireless_interface.is_required}
        return wireless_interface
    def get_case_material(self, smartphone):
        case_material={
            'attribute_name': smartphone.case_material.attribute_name, 
            'attribute_id': smartphone.case_material.attribute_id, 
            'dictionary_value_id': smartphone.case_material.digital_code, 
            'value': smartphone.case_material.name,
            'is_required': smartphone.case_material.is_required}
        return case_material
    def get_operation_system(self, smartphone):
        operation_system={
            'attribute_name': smartphone.operation_system.attribute_name, 
            'attribute_id': smartphone.operation_system.attribute_id, 
            'dictionary_value_id': smartphone.operation_system.digital_code, 
            'value': smartphone.operation_system.name,
            'is_required': smartphone.operation_system.is_required }
        return operation_system
    def get_android_version(self, smartphone):
        android_version={
            'attribute_name': smartphone.android_version.attribute_name, 
            'attribute_id': smartphone.android_version.attribute_id, 
            'dictionary_value_id': smartphone.android_version.digital_code, 
            'value': smartphone.android_version.name,
            'is_required': smartphone.android_version.is_required }
        return android_version
    def get_interface(self, smartphone):
        interface={
            'attribute_name': smartphone.interface.attribute_name, 
            'attribute_id': smartphone.interface.attribute_id, 
            'dictionary_value_id': smartphone.interface.digital_code, 
            'value': smartphone.interface.name,
            'is_required': smartphone.interface.is_required}
        return interface
    def get_microsd_slot(self, smartphone):
        microsd_slot={
            'attribute_name': smartphone.microsd_slot.attribute_name, 
            'attribute_id': smartphone.microsd_slot.attribute_id, 
            'dictionary_value_id': smartphone.microsd_slot.digital_code, 
            'value': smartphone.microsd_slot.attribute_name,
            'is_required': smartphone.microsd_slot.is_required }
        return microsd_slot
    def get_special_feature(self, smartphone):
        special_feature={
            'attribute_name': smartphone.special_feature.attribute_name, 
            'attriubte_id': smartphone.special_feature.attribute_id, 
            'dictionary_value_id': smartphone.special_feature.digital_code, 
            'value': smartphone.special_feature.name,
            'is_required': smartphone.special_feature.is_required}
        return special_feature
    def get_charging_function(self, smartphone):
        charging_function={
            'attribute_name': smartphone.charging_function.attribute_name, 
            'attribute_id': smartphone.charging_function.attribute_id, 
            'dictionary_value_id': smartphone.charging_function.digital_code, 
            'value': smartphone.charging_function.attribute_name,
            'is_required': smartphone.charging_function.is_required}
        return charging_function
    def get_stabilization(self, smartphone):
        stabilization={
            'attribute_name': smartphone.stabilization.attribute_name, 
            'attribute_id': smartphone.stabilization.attribute_id, 
            'dictionary_value_id': smartphone.stabilization.digital_code, 
            'value': smartphone.stabilization.name,
            'is_required': smartphone.stabilization.is_required}
        return stabilization
    def get_authentification(self, smartphone):
        authentification={
            'attribute_name': smartphone.authentification.attribute_name, 
            'attribute_id': smartphone.authentification.attribute_id, 
            'dictionary_value_id': smartphone.authentification.digital_code, 
            'value': smartphone.authentification.name,
            'is_required': smartphone.authentification.is_required }
        return authentification
    def get_case_form(self, smartphone):
        case_form={
            'attribute_name': smartphone.case_form.attribute_name, 
            'attribute_id': smartphone.case_form.attribute_name, 
            'dictionary_value_id': smartphone.case_form.digital_code, 
            'value': smartphone.case_form.name,
            'is_required': smartphone.case_form.is_required}
        return case_form
    def get_ios_version(self, smartphone):
        ios_version={
            'attribute_name': smartphone.ios_version.attribute_name, 
            'attribute_id': smartphone.ios_version.attribute_id, 
            'dictionary_value_id': smartphone.ios_version.digital_code, 
            'value': smartphone.ios_version.name,
            'is_required': smartphone.ios_version.is_required}
        return ios_version
    def get_euro_asian_code(self, smartphone):
        euro_asian_code={
            'attribute_name': smartphone.euro_asian_code.attribute_name, 
            'attribute_id': smartphone.euro_asian_code.attribute_id, 
            'dictionary_value_id': smartphone.euro_asian_code.digital_code, 
            'value': smartphone.euro_asian_code.name,
            'is_required': smartphone.euro_asian_code.is_required}
        return euro_asian_code
    def get_esim_support(self, smartphone):
        esim_support={
            'attribute_name': smartphone.esim_support.attribute_name, 
            'attribute_id': smartphone.esim_support.attribute_id, 
            'dictionary_value_id': smartphone.esim_support.digital_code, 
            'value': smartphone.esim_support.name,
            'is_required': smartphone.esim_support.is_required}
        return esim_support
    def get_ram(self, smartphone):
        ram={
            'attribute_name': smartphone.ram.attribute_name, 
            'attribute_id': smartphone.ram.attribute_id, 
            'dictionary_value_id': smartphone.ram.digital_code, 
            'value': smartphone.ram.name,
            'is_required': smartphone.ram.is_required}
        return ram
    def get_publishing_year(self, smartphone):
        publishing_year={
            'attribute_name': smartphone.publishing_year.attribute_name, 
            'attribure_id': smartphone.publishing_year.attribute_id, 
            'dictionary_value_id': smartphone.publishing_year.digital_code, 
            'value': smartphone.publishing_year.name,
            'is_required': smartphone.publishing_year.is_required}
        return publishing_year
    def get_smartphone_version(self, smartphone):
        smartphone_version={
            'attribute_name': smartphone.smartphone_version.attribute_name, 
            'attribute_id': smartphone.smartphone_version.attribute_id, 
            'dictionary_value_id': smartphone.smartphone_version.digital_code, 
            'value': smartphone.smartphone_version.attribute_name}
        return smartphone_version

# class SmartphoneCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = ('name', 'url', 'id')
#         #fields = ('id', 'name')
#         