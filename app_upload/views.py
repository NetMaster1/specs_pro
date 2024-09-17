from django.shortcuts import render
from django.http import request
from rest_framework import viewsets
from app_reference_smartphones.models import (
    Brand, 
    EuroAsianCode, 
    CaseForm, MicroSDSlot, 
    ProcessorCoreQnty, 
    Processor, 
    QntyOfBasicCamera, 
    Colour, 
    ProtectionGrade, 
    GadgetModel, 
    VideoQuality,
    ScreenResolution, 
    Type,
    SimCardQnty
)
#from app_tv.models import TV_Brand
from app_reference_shared.models import (
    ProcessorBrand,
    CardType, 
    SmartphoneVersion, 
    PublishingYear, 
    RAM, 
    ESimSupport, 
    IOSVersion, 
    Authentication, 
    Stabilization, 
    ChargingFunction, 
    SpecialFeature, 
    Interface, 
    AndroidVersion,
    OperationSystem, 
    CaseMaterial, 
    WirelessInterface, 
    ProcessorModel, 
    VideoProcessor, 
    HazardGrade, 
    CameraFunction, 
    GadgetSerie, 
    VideoProcessorBrand, 
    OzonCategory, 
    HardDrive, 
    CountryOfManufacture, 
    MatrixType, 
    BluetoothType, 
    NavigationType, 
    Sensor, 
    SimType, 
    WifiType,
    CommunicationStandard
)
#from django.http import HttpResponse
import requests

def upload_ozon_categories(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "language": "DEFAULT"
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/tree', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        children=i['children']
        for k in children:
            children=k['children']
            for x in children:
                type_id=x['type_id']
        try:
            OzonCategory.objects.get(type_id=type_id)
        except OzonCategory.DoesNotExist:
            group_description_category_id=i['description_category_id']
            group_category_name=i['category_name']
            array_1=i['children']
            for k in array_1:
                description_category_id=k['description_category_id']
                category_name=k['category_name']
                array_2=k['children']
                for n in array_2:
                    ozon_category= OzonCategory.objects.create(
                        type_name=n['type_name'],
                        type_id=n['type_id'],
                        description_category_id=description_category_id,
                        category_name=category_name,
                        group_description_category_id=group_description_category_id,
                        group_category_name=group_category_name
                    )
                
    
    return render (request, 'products.html')

def upload_brands(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 85,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Brand.objects.get(digital_code=i['id'])
            item.is_required=True
            item.category_dependent=True
            item.save()
        except Brand.DoesNotExist:
            item= Brand.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='85',
                attribute_name='Бренд',
                is_required=True,
                catgegory_dependent=True
            )
    
    return render (request, 'products.html')

def upload_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 8229,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Type.objects.get(digital_code=i['id'])
            item.is_required=True
            item.category_dependent=True
            item.save()
        except Type.DoesNotExist:
            type= Type.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='8229',
                attribute_name='Тип'
            )
    
    return render (request, 'products.html')

def upload_hard_drive (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22788,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HardDrive.objects.get(digital_code=i['id'])
            item.is_required=True
            item.category_dependent=False
            item.save()
        except HardDrive.DoesNotExist:
            hardDrive= HardDrive.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22788',
                attribute_name='Встроенная память'
            )
    
    return render (request, 'products.html')

def upload_country_of_manufacture (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4389,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CountryOfManufacture.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except CountryOfManufacture.DoesNotExist:
            country= CountryOfManufacture.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4389',
                attribute_name='Страна-изготовитель'
            )
    
    return render (request, 'products.html')

def upload_matrix_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4406,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MatrixType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except MatrixType.DoesNotExist:
            country= MatrixType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4406',
                attribute_name='Технология матрицы'
            )
    
    return render (request, 'products.html')

def upload_card_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4411,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CardType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except CardType.DoesNotExist:
            item= CardType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4411',
                attribute_name='Тип карты памяти'
            )
    
    return render (request, 'products.html')

def upload_bluetooth_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4414,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BluetoothType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except BluetoothType.DoesNotExist:
            country= BluetoothType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4414',
                attribute_name='Модуль связи Bluetooth'
            )
    
    return render (request, 'products.html')

def upload_navigation_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4417,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NavigationType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except NavigationType.DoesNotExist:
            country= NavigationType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4417',
                attribute_name='Навигация'
            )
    
    return render (request, 'products.html')

def upload_sensor (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4418,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Sensor.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except Sensor.DoesNotExist:
            country= Sensor.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4418',
                attribute_name='Встроенные датчики'
            )
    
    return render (request, 'products.html')

def upload_sim_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4437,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SimType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except SimType.DoesNotExist:
            country= SimType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4437',
                attribute_name='Форм-фактор SIM'
            )
    
    return render (request, 'products.html')

def upload_wifi_type (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4465,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=WifiType.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except WifiType.DoesNotExist:
            wifi= WifiType.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4465',
                attribute_name='Модуль связи WiFi'
            )
    
    return render (request, 'products.html')

def upload_video_processor_brand(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5142,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoProcessorBrand.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except VideoProcessorBrand.DoesNotExist:
            video= VideoProcessorBrand.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5142',
                attribute_name='Бренд графического процессора'
            )
    
    return render (request, 'products.html')

def upload_screen_resolution(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5186,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ScreenResolution.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except ScreenResolution.DoesNotExist:
            item= ScreenResolution.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5186',
                attribute_name='Разрешение экрана'
            )
    
    return render (request, 'products.html')

def upload_video_quality(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5200,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoQuality.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except VideoQuality.DoesNotExist:
            item= VideoQuality.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5200',
                attribute_name='Качество видео'
            )
    
    return render (request, 'products.html')

def upload_gadget_model(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5219,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=GadgetModel.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except GadgetModel.DoesNotExist:
            item= GadgetModel.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5219',
                attribute_name='Модель устройства'
            )

    return render (request, 'products.html')

def upload_protection_grade(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5269,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ProtectionGrade.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except ProtectionGrade.DoesNotExist:
            item= ProtectionGrade.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5269',
                attribute_name='Степень защиты'
            )
            
    return render (request, 'products.html')

def upload_gadget_series(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 9225,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=GadgetSerie.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except GadgetSerie.DoesNotExist:
            item= GadgetSerie.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='9225',
                attribute_name='Линейка мобильных устройств'
            )
            
    return render (request, 'products.html')

def upload_camera_functions(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 9504,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CameraFunction.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except CameraFunction.DoesNotExist:
            item= CameraFunction.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='9504',
                attribute_name='Функции камеры'
            )
            
    return render (request, 'products.html')

def upload_hazard_grade(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 9782,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HazardGrade.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except HazardGrade.DoesNotExist:
            item= HazardGrade.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='9782',
                attribute_name='Класс опасности товара'
            )
            
    return render (request, 'products.html')

def upload_colour(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10096,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Colour.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except Colour.DoesNotExist:
            item= Colour.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10096',
                attribute_name='Цвет товара'
            )
            
    return render (request, 'products.html')

def upload_qnty_of_basic_cameras(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10172,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=QntyOfBasicCamera.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except QntyOfBasicCamera.DoesNotExist:
            item= QntyOfBasicCamera.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10172',
                attribute_name='Количество основных камер'
            )
            
    return render (request, 'products.html')

def upload_processor (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10313,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Processor.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except Processor.DoesNotExist:
            item= Processor.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10313',
                attribute_name='Процессор'
            )
    
    return render (request, 'products.html')

def upload_video_processor (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10314,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoProcessor.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except VideoProcessor.DoesNotExist:
            item= VideoProcessor.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10314',
                attribute_name='Видеопроцессор'
            )
    
    return render (request, 'products.html')

def upload_processor_brands (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10315,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ProcessorBrand.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except ProcessorBrand.DoesNotExist:
            item= ProcessorBrand.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10315',
                attribute_name='Бренд процессора'
            )
    
    return render (request, 'products.html')

def upload_processor_core_qnty (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10318,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ProcessorCoreQnty.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except ProcessorCoreQnty.DoesNotExist:
            item= ProcessorCoreQnty.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10318',
                attribute_name='Число ядер процессора'
            )
    
    return render (request, 'products.html')

def upload_processor_model (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10320,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ProcessorModel.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except ProcessorModel.DoesNotExist:
            item= ProcessorModel.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10320',
                attribute_name='Модель процессора'
            )
    
    return render (request, 'products.html')

def upload_wireless_interfaces (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10387,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=WirelessInterface.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except WirelessInterface.DoesNotExist:
            item= WirelessInterface.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10387',
                attribute_name='Беспроводные интерфейсы'
            )
    
    return render (request, 'products.html')

def upload_case_material (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10746,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CaseMaterial.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except CaseMaterial.DoesNotExist:
            item= CaseMaterial.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10746',
                attribute_name='Основной материал корпуса'
            )
    
    return render (request, 'products.html')

def upload_operation_systems (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10889,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=OperationSystem.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except OperationSystem.DoesNotExist:
            item= OperationSystem.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10889',
                attribute_name='Операционная система'
            )
    
    return render (request, 'products.html')

def upload_android_versions (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 10890,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=AndroidVersion.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except AndroidVersion.DoesNotExist:
            item= AndroidVersion.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='10890',
                attribute_name='Версия Android'
            )
    
    return render (request, 'products.html')

def upload_interfaces (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11298,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Interface.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except Interface.DoesNotExist:
            item= Interface.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11298',
                attribute_name='Интерфейсы'
            )
    
    return render (request, 'products.html')

def upload_communication_standards (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11375,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CommunicationStandard.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except CommunicationStandard.DoesNotExist:
            item= CommunicationStandard.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11375',
                attribute_name='Стандарты связи'
            )
    
    return render (request, 'products.html')

def upload_microsd_slots (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11448,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MicroSDSlot.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except MicroSDSlot.DoesNotExist:
            item= MicroSDSlot.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11448',
                attribute_name='Слот для карты памяти'
            )
    
    return render (request, 'products.html')

def upload_special_features (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11449,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SpecialFeature.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except SpecialFeature.DoesNotExist:
            item= SpecialFeature.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11449',
                attribute_name='Особенности'
            )
    
    return render (request, 'products.html')

def upload_charging_functions (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11450,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ChargingFunction.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except ChargingFunction.DoesNotExist:
            item= ChargingFunction.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11450',
                attribute_name='Функция зарядки'
            )
    
    return render (request, 'products.html')

def upload_stabilization (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11590,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Stabilization.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except Stabilization.DoesNotExist:
            item= Stabilization.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11590',
                attribute_name='Стабилизация'
            )
    
    return render (request, 'products.html')

def upload_authentication (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11591,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Authentication.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except Authentication.DoesNotExist:
            item= Authentication.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='11591',
                attribute_name='Аутентификация'
            )
    
    return render (request, 'products.html')

def upload_case_forms (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 12126,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CaseForm.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except CaseForm.DoesNotExist:
            item= CaseForm.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='12126',
                attribute_name='Тип корпуса'
            )
    
    return render (request, 'products.html')

def upload_ios_versions (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 12958,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=IOSVersion.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except IOSVersion.DoesNotExist:
            item= IOSVersion.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='12958',
                attribute_name='Версия iOS'
            )
    
    return render (request, 'products.html')

def upload_euroasian_codes (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22232,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=EuroAsianCode.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except EuroAsianCode.DoesNotExist:
            item= EuroAsianCode.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22232',
                attribute_name='ТН ВЭД коды ЕАЭС'
            )
    
    return render (request, 'products.html')

def upload_sim_qnty (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 4407,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SimCardQnty.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except SimCardQnty.DoesNotExist:
            item= SimCardQnty.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='4407',
                attribute_name='Число физических SIM-карт'
            )
    
    return render (request, 'products.html')

def upload_esim_support (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22233,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ESimSupport.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except ESimSupport.DoesNotExist:
            item= ESimSupport.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22233',
                attribute_name='Поддержка eSim'
            )
    
    return render (request, 'products.html')

def upload_ram (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22803,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=RAM.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except RAM.DoesNotExist:
            item= RAM.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22803',
                attribute_name='Оперативная память'
            )
    
    return render (request, 'products.html')

def upload_publishing_year (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22808,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=PublishingYear.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except PublishingYear.DoesNotExist:
            item= PublishingYear.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22808',
                attribute_name='Год аннонсирования'
            )
    
    return render (request, 'products.html')

def upload_smartphone_versions (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 22975,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 10000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SmartphoneVersion.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=False
            item.save()
        except SmartphoneVersion.DoesNotExist:
            item= SmartphoneVersion.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='22975',
                attribute_name='Версия смартфона'
            )
    
    return render (request, 'products.html')

def upload_video_quality (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5200,
    "description_category_id": 15621050,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 95139
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoQuality.objects.get(digital_code=i['id'])
            item.is_required=False
            item.category_dependent=True
            item.save()
        except VideoQuality.DoesNotExist:
            item= VideoQuality.objects.create(
                name=i['value'],
                digital_code=i['id'],
                attribute_id='5200',
                attribute_name='Качество видео'
            )
    
    return render (request, 'products.html')

def upload_tv_brands(request):
    pass

def delete_tables (request):
    tables=Processor.objects.all()
    for i in tables:
        i.delete()
    tables=ProtectionGrade.objects.all()
    for i in tables:
        i.delete()
    tables=QntyOfBasicCamera.objects.all()
    for i in tables:
        i.delete()
    tables=ScreenResolution.objects.all()
    for i in tables:
        i.delete()
    tables=SimCardQnty.objects.all()
    for i in tables:
        i.delete()
    tables=Type.objects.all()
    for i in tables:
        i.delete()
    tables=VideoQuality.objects.all()
    for i in tables:
        i.delete()
    for i in tables:
        i.delete()


    
    return render (request, 'products.html')
