from django.shortcuts import render
from django.http import request
from rest_framework import viewsets
import time
from app_reference_smartphones.models import (
    BrandSmartphone, 
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
    #TypeSmartphone,
    SimCardQnty
)
#from app_tv.models import TV_Brand
from app_reference_shared.models import (
    ProcessorBrand,
    CardType, 
    SmartphoneVersion, 
    PublishingYear, 
    RamSmartphone, 
    ESimSupport, 
    IOSVersion, 
    Authentication, 
    Stabilization, 
    ChargingFunction, 
    SpecialFeature, 
    SpecialFeatureSmartphone, 
    Interface, 
    AndroidVersion,
    OSMobile, 
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
    CommunicationStandard,
    Json,
    LightningType,
    ScreenCoating,
    HDMIPort,
    Adjustment,
    PixelSize,
    Ratio,
    MaxScreenFrequency,
    Brightness,
    Contrast,
    DynamicContrast,
    LookAngle,
    HorizontalFrequency,
    VerticalFrequency,
    WebCamera,
    StandAdjustment,
    PowerCapacity,
    VESAFixture,
    PixelPerInch,
    MonitorInstallation,
    DesignFeature,
    ResponseTime,
    MonitorMatrix,
    MonitorApplication,
    MonitorConnector,
    HDRStandard,
    ProcessorModelNotebook,
    NotebookFormFactor,
    Chipset,
    RAMFormFactor,
    DVDrive,
    VideoCardType,
    SoundConfig,
    ManualInputDevice,
    ManualInputDeviceFeature,
    LANCard,
    BuiltInDevice,
    WebCamResolution,
    CaseCoating,
    BatteryType,
    PowerSupplyVoltage,
    CardReader,
    NotebookProcessor,
    NotebookProcessorBrand,
    NotebookVideoProcessorBrand,
    OperationSystem,
    VideoProcessorFamily,
    NotebookMatrixType,
    WindowsVersion,
    MacOSVersion,
    KeyboardLayout,
    WebCamShutter,
)
from app_monitor_reference.models import (
    Resolution, TypeMonitor, USBPort, BuiltinSpeaker, CurvedDispaly, HDR, Brand_Monitor, EuroAsianCodeMonitor, ColourMonitor,
)
from app_notebook_reference.models import (
    BrandNotebook, TypeNotebook, HDDQnty, RAMNotebook, NotebookRAMType, NotebookMaxRAM, RAMExtraSlot, SSDQnty, VideoRAM, KeyboardColour, NotebookCaseMaterial, 
    NotebookInterfacesConnector, BatteryElementQnty, NotebookScreenResolution, HDDFormFactor, SSDFormFactor, StorageType, VideoCard, VRSupport,
    NotebookColour, TouchScreen, NotebookProcessorCoreQnty, KeyboardLightning, MobileCommsModule, 
)

#from django.http import HttpResponse
import requests

def upload_type_nb(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 8229,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=TypeNotebook.objects.get(dictionary_value_id=i['id'])
        except TypeNotebook.DoesNotExist:
            item= TypeNotebook.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='8229',
                attribute_name='Тип',
                is_collection=False,
                is_required=True,
                category_dependent=True
            )


def upload_notebook(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 85,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BrandNotebook.objects.get(dictionary_value_id=i['id'])
        except BrandNotebook.DoesNotExist:
            item= BrandNotebook.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='85',
                attribute_name='Бренд',
                is_collection=False,
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 8229,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=TypeNotebook.objects.get(dictionary_value_id=i['id'])
        except TypeNotebook.DoesNotExist:
            item= TypeNotebook.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='8229',
                attribute_name='Тип',
                is_collection=False,
                is_required=True,
                category_dependent=True
            )
    
    #==============================================================================
    task = {
    "attribute_id": 10316,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ProcessorModelNotebook.objects.get(dictionary_value_id=i['id'])
        except ProcessorModelNotebook.DoesNotExist:
            item= ProcessorModelNotebook.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10316',
                attribute_name='Модель процессора',
                is_collection=False,
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4438,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HDDQnty.objects.get(dictionary_value_id=i['id'])
        except HDDQnty.DoesNotExist:
            item= HDDQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4438',
                attribute_name='Количество HDD',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4441,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookFormFactor.objects.get(dictionary_value_id=i['id'])
        except NotebookFormFactor.DoesNotExist:
            item= NotebookFormFactor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4441',
                attribute_name='Форм-фактор ноутбука',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 4442,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Chipset.objects.get(dictionary_value_id=i['id'])
        except Chipset.DoesNotExist:
            item= Chipset.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4442',
                attribute_name='Чипсет',
                is_collection=True,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4443,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=RAMNotebook.objects.get(dictionary_value_id=i['id'])
        except RAMNotebook.DoesNotExist:
            item= RAMNotebook.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4443',
                attribute_name='Оперативная память',
                is_collection=True,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4444,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookRAMType.objects.get(dictionary_value_id=i['id'])
        except NotebookRAMType.DoesNotExist:
            item= NotebookRAMType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4444',
                attribute_name='Тип памяти',
                is_collection=True,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4445,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookMaxRAM.objects.get(dictionary_value_id=i['id'])
        except NotebookMaxRAM.DoesNotExist:
            item= NotebookMaxRAM.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4445',
                attribute_name='Возможность расширения RAM, до',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4447,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=RAMFormFactor.objects.get(dictionary_value_id=i['id'])
        except RAMFormFactor.DoesNotExist:
            item= RAMFormFactor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4447',
                attribute_name='Форм-фактор RAM',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4448,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=RAMExtraSlot.objects.get(dictionary_value_id=i['id'])
        except RAMExtraSlot.DoesNotExist:
            item= RAMExtraSlot.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4448',
                attribute_name='Доп. слоты RAM памяти',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4451,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SSDQnty.objects.get(dictionary_value_id=i['id'])
        except SSDQnty.DoesNotExist:
            item= SSDQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4451',
                attribute_name='Количество SSD',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4452,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=DVDrive.objects.get(dictionary_value_id=i['id'])
        except DVDrive.DoesNotExist:
            item= DVDrive.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4452',
                attribute_name='Оптический привод',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 4454,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoCardType.objects.get(dictionary_value_id=i['id'])
        except VideoCardType.DoesNotExist:
            item= VideoCardType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4454',
                attribute_name='Тип видеокарты',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 4455,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoRAM.objects.get(dictionary_value_id=i['id'])
        except VideoRAM.DoesNotExist:
            item= VideoRAM.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4455',
                attribute_name='Видеопамять',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4459,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SoundConfig.objects.get(dictionary_value_id=i['id'])
        except SoundConfig.DoesNotExist:
            item= SoundConfig.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4459',
                attribute_name='Конфигурация звука',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4461,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ManualInputDevice.objects.get(dictionary_value_id=i['id'])
        except ManualInputDevice.DoesNotExist:
            item= ManualInputDevice.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4461',
                attribute_name='Устройства ручного ввода',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4462,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ManualInputDeviceFeature.objects.get(dictionary_value_id=i['id'])
        except ManualInputDeviceFeature.DoesNotExist:
            item= ManualInputDeviceFeature.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4462',
                attribute_name='Особенности устройств ручного ввода',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4463,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=KeyboardColour.objects.get(dictionary_value_id=i['id'])
        except KeyboardColour.DoesNotExist:
            item= KeyboardColour.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4463',
                attribute_name='Цвет клавиатуры',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4466,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=LANCard.objects.get(dictionary_value_id=i['id'])
        except LANCard.DoesNotExist:
            item= LANCard.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4466',
                attribute_name='Сетевая карта',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4463,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=KeyboardColour.objects.get(dictionary_value_id=i['id'])
        except KeyboardColour.DoesNotExist:
            item= KeyboardColour.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4463',
                attribute_name='Цвет клавиатуры',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4467,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BuiltInDevice.objects.get(dictionary_value_id=i['id'])
        except BuiltInDevice.DoesNotExist:
            item= BuiltInDevice.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4467',
                attribute_name='Встроенные устройства',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4468,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=WebCamResolution.objects.get(dictionary_value_id=i['id'])
        except WebCamResolution.DoesNotExist:
            item= WebCamResolution.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4468',
                attribute_name='Разрешение Web-камеры',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4469,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookCaseMaterial.objects.get(dictionary_value_id=i['id'])
        except NotebookCaseMaterial.DoesNotExist:
            item= NotebookCaseMaterial.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4469',
                attribute_name='Материал корпуса',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4470,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CaseCoating.objects.get(dictionary_value_id=i['id'])
        except CaseCoating.DoesNotExist:
            item= CaseCoating.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4470',
                attribute_name='Покрытие корпуса',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4471,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookInterfacesConnector.objects.get(dictionary_value_id=i['id'])
        except NotebookInterfacesConnector.DoesNotExist:
            item= NotebookInterfacesConnector.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4471',
                attribute_name='Интерфейсы и разъемы',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4479,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BatteryElementQnty.objects.get(dictionary_value_id=i['id'])
        except BatteryElementQnty.DoesNotExist:
            item= BatteryElementQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4479',
                attribute_name='Кол-во элементов аккумулятора',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4480,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BatteryType.objects.get(dictionary_value_id=i['id'])
        except BatteryType.DoesNotExist:
            item= BatteryType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4480',
                attribute_name='Тип аккумулятора',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4481,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=PowerSupplyVoltage.objects.get(dictionary_value_id=i['id'])
        except PowerSupplyVoltage.DoesNotExist:
            item= PowerSupplyVoltage.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4481',
                attribute_name='Напряжение адаптера питания',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 5186,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookScreenResolution.objects.get(dictionary_value_id=i['id'])
        except NotebookScreenResolution.DoesNotExist:
            item= NotebookScreenResolution.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5186',
                attribute_name='Разрешение экрана',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 5580,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CardReader.objects.get(dictionary_value_id=i['id'])
        except CardReader.DoesNotExist:
            item= CardReader.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5580',
                attribute_name='Картридер',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9141,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HDDFormFactor.objects.get(dictionary_value_id=i['id'])
        except HDDFormFactor.DoesNotExist:
            item= HDDFormFactor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9141',
                attribute_name='Форм-фактор HDD',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9142,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=SSDFormFactor.objects.get(dictionary_value_id=i['id'])
        except SSDFormFactor.DoesNotExist:
            item= SSDFormFactor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9142',
                attribute_name='Форм-фактор SSD',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9221,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=StorageType.objects.get(dictionary_value_id=i['id'])
        except StorageType.DoesNotExist:
            item= StorageType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9221',
                attribute_name='Тип накопителя',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9785,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookProcessor.objects.get(dictionary_value_id=i['id'])
        except NotebookProcessor.DoesNotExist:
            item= NotebookProcessor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9785',
                attribute_name='Процессор',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9786,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoCard.objects.get(dictionary_value_id=i['id'])
        except VideoCard.DoesNotExist:
            item= VideoCard.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9786',
                attribute_name='Видеокарта',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 9923,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VRSupport.objects.get(dictionary_value_id=i['id'])
        except VRSupport.DoesNotExist:
            item= VRSupport.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9923',
                attribute_name='Поддержка VR',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 10096,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookColour.objects.get(dictionary_value_id=i['id'])
        except NotebookColour.DoesNotExist:
            item= NotebookColour.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10096',
                attribute_name='Цвет товара',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 10294,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=TouchScreen.objects.get(dictionary_value_id=i['id'])
        except TouchScreen.DoesNotExist:
            item= TouchScreen.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10294',
                attribute_name='Сенсорный экран',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 10318,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookProcessorCoreQnty.objects.get(dictionary_value_id=i['id'])
        except NotebookProcessorCoreQnty.DoesNotExist:
            item= NotebookProcessorCoreQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10318',
                attribute_name='Число ядер процессора',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 10746,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CaseMaterial.objects.get(dictionary_value_id=i['id'])
        except CaseMaterial.DoesNotExist:
            item= CaseMaterial.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10746',
                attribute_name='Основной материал корпуса',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 11362,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookProcessorBrand.objects.get(dictionary_value_id=i['id'])
        except NotebookProcessorBrand.DoesNotExist:
            item= NotebookProcessorBrand.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11362',
                attribute_name='Бренд процессора',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 11363,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookVideoProcessorBrand.objects.get(dictionary_value_id=i['id'])
        except NotebookVideoProcessorBrand.DoesNotExist:
            item= NotebookVideoProcessorBrand.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11363',
                attribute_name='Бренд графического процессора',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 11377,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=OperationSystem.objects.get(dictionary_value_id=i['id'])
        except OperationSystem.DoesNotExist:
            item= OperationSystem.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11377',
                attribute_name='Операционная система',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 11379,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VideoProcessorFamily.objects.get(dictionary_value_id=i['id'])
        except VideoProcessorFamily.DoesNotExist:
            item= VideoProcessorFamily.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11379',
                attribute_name='Серия графического процессора',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 11380,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=NotebookMatrixType.objects.get(dictionary_value_id=i['id'])
        except NotebookMatrixType.DoesNotExist:
            item= NotebookMatrixType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11380',
                attribute_name='Технология матрицы',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 12454,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=WindowsVersion.objects.get(dictionary_value_id=i['id'])
        except WindowsVersion.DoesNotExist:
            item= WindowsVersion.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='12454',
                attribute_name='Версия Windows',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 12455,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MacOSVersion.objects.get(dictionary_value_id=i['id'])
        except MacOSVersion.DoesNotExist:
            item= MacOSVersion.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='12455',
                attribute_name='Версия MacOS',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
    task = {
    "attribute_id": 12611,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=KeyboardLightning.objects.get(dictionary_value_id=i['id'])
        except KeyboardLightning.DoesNotExist:
            item= KeyboardLightning.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='12611',
                attribute_name='Подсветка клавиатуры',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 20102,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MobileCommsModule.objects.get(dictionary_value_id=i['id'])
        except MobileCommsModule.DoesNotExist:
            item= MobileCommsModule.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='20102',
                attribute_name='Модуль сотовой связи',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 21988,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=KeyboardLayout.objects.get(dictionary_value_id=i['id'])
        except KeyboardLayout.DoesNotExist:
            item= KeyboardLayout.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='21988',
                attribute_name='Раскладка клавиатуры',
                is_collection=False,
                is_required=False,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 22288,
    "description_category_id": 17028619,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91477
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=WebCamShutter.objects.get(dictionary_value_id=i['id'])
        except WebCamShutter.DoesNotExist:
            item= WebCamShutter.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22288',
                attribute_name='Шторка для веб-камеры',
                is_collection=False,
                is_required=False,
                category_dependent=False
            )
    #========================================================
 
    return render (request, 'products.html')


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

def upload_all(request):
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
        item= BrandSmartphone.objects.create(
            value=i['value'],
            dictionary_value_id=i['id'],
            attribute_id='85',
            attribute_name='Бренд',
            is_required=True,
            category_dependent=True
        )

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
        type= Type.objects.create(
            value=i['value'],
            dictionary_value_id=i['id'],
            attribute_id='8229',
            attribute_name='Тип',
            is_required=True,
            category_dependent=True
        )
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
        hardDrive= HardDrive.objects.create(
            value=i['value'],
            dictonary_value_id=i['id'],
            attribute_id='22788',
            attribute_name='Встроенная память',
            is_required=True,
            category_dependent=False
        )
#==========================================================
#==========================================================
#==========================================================
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
            item=BrandSmartphone.objects.get(dictionary_value_id=i['id'])
        except BrandSmartphone.DoesNotExist:
            item= BrandSmartphone.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='85',
                attribute_name='Бренд',
                is_required=True,
                category_dependent=True
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
            item=TypeSmartphone.objects.get(dictionary_value_id=i['id'])
        except TypeSmartphone.DoesNotExist:
            type= TypeSmartphone.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='8229',
                attribute_name='Тип',
                is_required=True,
                category_dependent=True
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
            item=HardDrive.objects.get(dictionary_value_id=i['id'])

        except HardDrive.DoesNotExist:
            hardDrive= HardDrive.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22788',
                attribute_name='Встроенная память',
                is_required=True,
                category_dependent=False
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
            item=CountryOfManufacture.objects.get(dictionary_value_id=i['id'])

        except CountryOfManufacture.DoesNotExist:
            country= CountryOfManufacture.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4389',
                attribute_name='Страна-изготовитель',
                is_required=False,
                category_dependent=False
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
            item=MatrixType.objects.get(dictionary_value_id=i['id'])

        except MatrixType.DoesNotExist:
            country= MatrixType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4406',
                attribute_name='Технология матрицы',
                is_required=False,
                category_dependent=False
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
            item=CardType.objects.get(dictionary_value_id=i['id'])

        except CardType.DoesNotExist:
            item= CardType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4411',
                attribute_name='Тип карты памяти',
                is_required=False,
                category_dependent=False
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
            item=BluetoothType.objects.get(dictionary_value_id=i['id'])

        except BluetoothType.DoesNotExist:
            country= BluetoothType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4414',
                attribute_name='Модуль связи Bluetooth',
                is_required=False,
                category_dependent=False
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
            item=NavigationType.objects.get(dictionary_value_id=i['id'])

        except NavigationType.DoesNotExist:
            country= NavigationType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4417',
                attribute_name='Навигация',
                is_required=False,
                category_dependent=False
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
            item=Sensor.objects.get(dictionary_value_id=i['id'])

        except Sensor.DoesNotExist:
            country= Sensor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4418',
                attribute_name='Встроенные датчики',
                is_required=False,
                category_dependent=False
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
            item=SimType.objects.get(dictionary_value_id=i['id'])

        except SimType.DoesNotExist:
            country= SimType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4437',
                attribute_name='Форм-фактор SIM',
                is_required=False,
                category_dependent=False
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
            item=WifiType.objects.get(dictionary_value_id=i['id'])

        except WifiType.DoesNotExist:
            wifi= WifiType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4465',
                attribute_name='Модуль связи WiFi',
                is_required=False,
                category_dependent=False
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
            item=VideoProcessorBrand.objects.get(dictionary_value_id=i['id'])

        except VideoProcessorBrand.DoesNotExist:
            video= VideoProcessorBrand.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5142',
                attribute_name='Бренд графического процессора',
                is_required=False,
                category_dependent=False
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
            item=ScreenResolution.objects.get(dictionary_value_id=i['id'])

        except ScreenResolution.DoesNotExist:
            item= ScreenResolution.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5186',
                attribute_name='Разрешение экрана',
                is_required=False,
                category_dependent=True
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
            item=VideoQuality.objects.get(dictionary_value_id=i['id'])

        except VideoQuality.DoesNotExist:
            item= VideoQuality.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5200',
                attribute_name='Качество видео',
                is_required=False,
                category_dependent=True
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
            item=GadgetModel.objects.get(dictionary_value_id=i['id'])

        except GadgetModel.DoesNotExist:
            item= GadgetModel.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5219',
                attribute_name='Модель устройства',
                is_required=False,
                category_dependent=True
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
            item=ProtectionGrade.objects.get(dictionary_value_id=i['id'])

        except ProtectionGrade.DoesNotExist:
            item= ProtectionGrade.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5269',
                attribute_name='Степень защиты',
                is_required=False,
                category_dependent=True
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
            item=GadgetSerie.objects.get(dictionary_value_id=i['id'])

        except GadgetSerie.DoesNotExist:
            item= GadgetSerie.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9225',
                attribute_name='Линейка мобильных устройств',
                is_required=False,
                category_dependent=False
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
            item=CameraFunction.objects.get(dictionary_value_id=i['id'])

        except CameraFunction.DoesNotExist:
            item= CameraFunction.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9504',
                attribute_name='Функции камеры',
                is_required=False,
                category_dependent=False
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
            item=HazardGrade.objects.get(dictionary_value_id=i['id'])

        except HazardGrade.DoesNotExist:
            item= HazardGrade.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='9782',
                attribute_name='Класс опасности товара',
                is_required=False,
                category_dependent=False
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
            item=Colour.objects.get(dictionary_value_id=i['id'])

        except Colour.DoesNotExist:
            item= Colour.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10096',
                attribute_name='Цвет товара',
                is_required=False,
                category_dependent=True
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
            item=QntyOfBasicCamera.objects.get(dictionary_value_id=i['id'])

        except QntyOfBasicCamera.DoesNotExist:
            item= QntyOfBasicCamera.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10172',
                attribute_name='Количество основных камер',
                is_required=False,
                category_dependent=True
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
            item=Processor.objects.get(dictionary_value_id=i['id'])

        except Processor.DoesNotExist:
            item= Processor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10313',
                attribute_name='Процессор',
                is_required=False,
                category_dependent=True
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
            item=VideoProcessor.objects.get(dictionary_value_id=i['id'])

        except VideoProcessor.DoesNotExist:
            item= VideoProcessor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10314',
                attribute_name='Видеопроцессор',
                is_required=False,
                category_dependent=False
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
            item=ProcessorBrand.objects.get(dictionary_value_id=i['id'])

        except ProcessorBrand.DoesNotExist:
            item= ProcessorBrand.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10315',
                attribute_name='Бренд процессора',
                is_required=False,
                category_dependent=False
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
            item=ProcessorCoreQnty.objects.get(dictionary_value_id=i['id'])

        except ProcessorCoreQnty.DoesNotExist:
            item= ProcessorCoreQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10318',
                attribute_name='Число ядер процессора',
                is_required=False,
                category_dependent=True
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
            item=ProcessorModel.objects.get(dictionary_value_id=i['id'])

        except ProcessorModel.DoesNotExist:
            item= ProcessorModel.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10320',
                attribute_name='Модель процессора',
                is_required=False,
                category_dependent=False
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
            item=WirelessInterface.objects.get(dictionary_value_id=i['id'])

        except WirelessInterface.DoesNotExist:
            item= WirelessInterface.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10387',
                attribute_name='Беспроводные интерфейсы',
                is_required=False,
                category_dependent=False
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
            item=CaseMaterial.objects.get(dictionary_value_id=i['id'])

        except CaseMaterial.DoesNotExist:
            item= CaseMaterial.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10746',
                attribute_name='Основной материал корпуса',
                is_required=False,
                category_dependent=False
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
            item=OSMobile.objects.get(dictionary_value_id=i['id'])

        except OSMobile.DoesNotExist:
            item= OSMobile.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10889',
                attribute_name='Операционная система',
                is_required=False,
                category_dependent=False
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
            item=AndroidVersion.objects.get(dictionary_value_id=i['id'])

        except AndroidVersion.DoesNotExist:
            item= AndroidVersion.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10890',
                attribute_name='Версия Android',
                is_required=False,
                category_dependent=False
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
            item=Interface.objects.get(dictionary_value_id=i['id'])

        except Interface.DoesNotExist:
            item= Interface.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11298',
                attribute_name='Интерфейсы',
                is_required=False,
                category_dependent=False
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
            item=CommunicationStandard.objects.get(dictionary_value_id=i['id'])

        except CommunicationStandard.DoesNotExist:
            item= CommunicationStandard.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11375',
                attribute_name='Стандарты связи',
                is_required=False,
                category_dependent=False
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
            item=MicroSDSlot.objects.get(dictionary_value_id=i['id'])

        except MicroSDSlot.DoesNotExist:
            item= MicroSDSlot.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11448',
                attribute_name='Слот для карты памяти',
                is_required=False,
                category_dependent=True
            )
    
    return render (request, 'products.html')

def upload_special_features (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5584,
    #"attribute_id": 11449,
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
            item=SpecialFeature.objects.get(dictionary_value_id=i['id'])

        except SpecialFeature.DoesNotExist:
            item= SpecialFeature.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5584',
                #attribute_id='11449',
                attribute_name='Особенности',
                is_required=False,
                category_dependent=False
            )
    
    return render (request, 'products.html')

def upload_special_features_smartphone (request):
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
            item=SpecialFeatureSmartphone.objects.get(dictionary_value_id=i['id'])

        except SpecialFeatureSmartphone.DoesNotExist:
            item= SpecialFeatureSmartphone.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11449',
                attribute_name='Особенности',
                is_required=False,
                category_dependent=False
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
            item=ChargingFunction.objects.get(dictionary_value_id=i['id'])

        except ChargingFunction.DoesNotExist:
            item= ChargingFunction.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11450',
                attribute_name='Функция зарядки',
                is_required=False,
                category_dependent=False
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
            item=Stabilization.objects.get(dictionary_value_id=i['id'])

        except Stabilization.DoesNotExist:
            item= Stabilization.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11590',
                attribute_name='Стабилизация',
                is_required=False,
                category_dependent=False
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
            item=Authentication.objects.get(dictionary_value_id=i['id'])

        except Authentication.DoesNotExist:
            item= Authentication.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11591',
                attribute_name='Аутентификация',
                is_required=False,
                category_dependent=False
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
            item=CaseForm.objects.get(dictionary_value_id=i['id'])

        except CaseForm.DoesNotExist:
            item= CaseForm.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='12126',
                attribute_name='Тип корпуса',
                is_required=False,
                category_dependent=True
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
            item=IOSVersion.objects.get(dictionary_value_id=i['id'])

        except IOSVersion.DoesNotExist:
            item= IOSVersion.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='12958',
                attribute_name='Версия iOS',
                is_required=False,
                category_dependent=False
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
            item=EuroAsianCode.objects.get(dictionary_value_id=i['id'])

        except EuroAsianCode.DoesNotExist:
            item= EuroAsianCode.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22232',
                attribute_name='ТН ВЭД коды ЕАЭС',
                is_required=False,
                category_dependent=True
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
            item=SimCardQnty.objects.get(dictionary_value_id=i['id'])

        except SimCardQnty.DoesNotExist:
            item= SimCardQnty.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4407',
                attribute_name='Число физических SIM-карт',
                is_required=False,
                category_dependent=True
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
            item=ESimSupport.objects.get(dictionary_value_id=i['id'])

        except ESimSupport.DoesNotExist:
            item= ESimSupport.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22233',
                attribute_name='Поддержка eSim',
                is_required=False,
                category_dependent=False
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
            item=RamSmartphone.objects.get(dictionary_value_id=i['id'])

        except RamSmartphone.DoesNotExist:
            item= RamSmartphone.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22803',
                attribute_name='Оперативная память',
                is_required=False,
                category_dependent=False
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
            item=PublishingYear.objects.get(dictionary_value_id=i['id'])

        except PublishingYear.DoesNotExist:
            item= PublishingYear.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22808',
                attribute_name='Год аннонсирования',
                is_required=False,
                category_dependent=False
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
            item=SmartphoneVersion.objects.get(dictionary_value_id=i['id'])

        except SmartphoneVersion.DoesNotExist:
            item= SmartphoneVersion.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='22975',
                attribute_name='Версия смартфона',
                is_required=False,
                category_dependent=False
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
        item= VideoQuality.objects.create(
            value=i['value'],
            dictionary_value_id=i['id'],
            attribute_id='5200',
            attribute_name='Качество видео',
            is_required=False,
            category_dependent=True
        )
    
    return render (request, 'products.html')

def upload_json (request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 11524,
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
        item= Json.objects.create(
            value=i['value'],
            dictionary_value_id=i['id'],
            attribute_id='11254',
            attribute_name='Rich-контент JSON',
            is_required=False,
            category_dependent=False
        )
    
    return render (request, 'products.html')


def upload_tv_brands(request):
    pass

def delete_tables (request):
    tables=Brand.objects.all()
    for i in tables:
        i.delete()
    tables=Type.objects.all()
    for i in tables:
        i.delete()
    tables=HardDrive.objects.all()
    for i in tables:
        i.delete()
    tables=CountryOfManufacture.objects.all()
    for i in tables:
        i.delete()
    tables=MatrixType.objects.all()
    for i in tables:
        i.delete()
    tables=CardType.objects.all()
    for i in tables:
        i.delete()
    tables=BluetoothType.objects.all()
    for i in tables:
        i.delete()
    tables=NavigationType.objects.all()
    for i in tables:
        i.delete()
    tables=Sensor.objects.all()
    for i in tables:
        i.delete()
    tables=SimType.objects.all()
    for i in tables:
        i.delete()
    tables=WifiType.objects.all()
    for i in tables:
        i.delete()
    tables=WifiType.objects.all()
    for i in tables:
        i.delete()
    tables=VideoProcessorBrand.objects.all()
    for i in tables:
        i.delete()
    tables=ScreenResolution.objects.all()
    for i in tables:
        i.delete()
    tables=VideoQuality.objects.all()
    for i in tables:
        i.delete()
    tables=GadgetModel.objects.all()
    for i in tables:
        i.delete()
    tables=ProtectionGrade.objects.all()
    for i in tables:
        i.delete()
    tables=GadgetSerie.objects.all()
    for i in tables:
        i.delete()
    tables=CameraFunction.objects.all()
    for i in tables:
        i.delete()
    tables=HazardGrade.objects.all()
    for i in tables:
        i.delete()
    tables=Colour.objects.all()
    for i in tables:
        i.delete()
    tables=QntyOfBasicCamera.objects.all()
    for i in tables:
        i.delete()
    tables=Processor.objects.all()
    for i in tables:
        i.delete()
    tables=VideoProcessor.objects.all()
    for i in tables:
        i.delete()
    tables=ProcessorBrand.objects.all()
    for i in tables:
        i.delete()
    tables=ProcessorCoreQnty.objects.all()
    for i in tables:
        i.delete()
    tables=ProcessorModel.objects.all()
    for i in tables:
        i.delete()
    tables=WirelessInterface.objects.all()
    for i in tables:
        i.delete()
    tables=CaseMaterial.objects.all()
    for i in tables:
        i.delete()
    tables=OSMobile.objects.all()
    for i in tables:
        i.delete()
    tables=AndroidVersion.objects.all()
    for i in tables:
        i.delete()
    tables=Interface.objects.all()
    for i in tables:
        i.delete()
    tables=CommunicationStandard.objects.all()
    for i in tables:
        i.delete()
    tables=MicroSDSlot.objects.all()
    for i in tables:
        i.delete()
    tables=SpecialFeature.objects.all()
    for i in tables:
        i.delete()
    tables= ChargingFunction.objects.all()
    for i in tables:
        i.delete()
    tables= Stabilization.objects.all()
    for i in tables:
        i.delete()
    tables= Authentication.objects.all()
    for i in tables:
        i.delete()
    tables= CaseForm.objects.all()
    for i in tables:
        i.delete()
    tables= IOSVersion.objects.all()
    for i in tables:
        i.delete()
    tables= EuroAsianCode.objects.all()
    for i in tables:
        i.delete()
    tables= SimCardQnty.objects.all()
    for i in tables:
        i.delete()
    tables= ESimSupport.objects.all()
    for i in tables:
        i.delete()
    tables= RAM.objects.all()
    for i in tables:
        i.delete()
    tables= PublishingYear.objects.all()
    for i in tables:
        i.delete()
    tables= SmartphoneVersion.objects.all()
    for i in tables:
        i.delete()
    
    
    return render (request, 'products.html')

def upload_monitor(request):
    headers = {
        "Client-Id": "867100",
        "Api-Key": '6bbf7175-6585-4c35-8314-646f7253bef6'
    }
    task = {
    "attribute_id": 5592,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Resolution.objects.get(dictionary_value_id=i['id'])
        except Resolution.DoesNotExist:
            item= Resolution.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5592',
                attribute_name='Разрешение',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 8229,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=TypeMonitor.objects.get(dictionary_value_id=i['id'])
        except TypeMonitor.DoesNotExist:
            item= TypeMonitor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='8229',
                attribute_name='Тип',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 5727,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=USBPort.objects.get(dictionary_value_id=i['id'])
        except USBPort.DoesNotExist:
            item= USBPort.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5727',
                attribute_name='Количество USB портов',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 8992,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=BuiltinSpeaker.objects.get(dictionary_value_id=i['id'])
        except BuiltinSpeaker.DoesNotExist:
            item= BuiltinSpeaker.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='8992',
                attribute_name='Встроенные динамики',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 10760,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=CurvedDispaly.objects.get(dictionary_value_id=i['id'])
        except CurvedDispaly.DoesNotExist:
            item= CurvedDispaly.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10760',
                attribute_name='Изогнутый экран',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 11529,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HDR.objects.get(dictionary_value_id=i['id'])
        except HDR.DoesNotExist:
            item= HDR.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11529',
                attribute_name='Технология HDR',
                is_required=True,
                category_dependent=True
            )
    #========================================================
    task = {
    "attribute_id": 4457,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=LightningType.objects.get(dictionary_value_id=i['id'])
        except LightningType.DoesNotExist:
            item= LightningType.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4457',
                attribute_name='Тип подсветки',
                is_required=False,
                category_dependent=False
            )
    #=========================================================================
    task = {
    "attribute_id": 4458,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ScreenCoating.objects.get(dictionary_value_id=i['id'])
        except ScreenCoating.DoesNotExist:
            item= ScreenCoating.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='4458',
                attribute_name='Покрытие экрана',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 5482,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Adjustment.objects.get(dictionary_value_id=i['id'])
        except Adjustment.DoesNotExist:
            item= Adjustment.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5482',
                attribute_name='Регулировки',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 5568,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Ratio.objects.get(dictionary_value_id=i['id'])
        except Ratio.DoesNotExist:
            item= Ratio.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5568',
                attribute_name='Соотношение сторон',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 5574,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=LookAngle.objects.get(dictionary_value_id=i['id'])
        except LookAngle.DoesNotExist:
            item= LookAngle.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5574',
                attribute_name='Углы обзора (Г/В)',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 5758,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=VESAFixture.objects.get(dictionary_value_id=i['id'])
        except VESAFixture.DoesNotExist:
            item= VESAFixture.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='5758',
                attribute_name='Стандарт крепления VESA',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 10758,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MonitorInstallation.objects.get(dictionary_value_id=i['id'])
        except MonitorInstallation.DoesNotExist:
            item= MonitorInstallation.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10758',
                attribute_name='Установка монитора',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 10759,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=DesignFeature.objects.get(dictionary_value_id=i['id'])
        except DesignFeature.DoesNotExist:
            item= DesignFeature.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10759',
                attribute_name='Конструктивные особенности',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 11510,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MonitorMatrix.objects.get(dictionary_value_id=i['id'])
        except MonitorMatrix.DoesNotExist:
            item= MonitorMatrix.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11510',
                attribute_name='Матрица монитора',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 11511,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MonitorApplication.objects.get(dictionary_value_id=i['id'])
        except MonitorApplication.DoesNotExist:
            item= MonitorApplication.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11511',
                attribute_name='Назначение монитора',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 11515,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=MonitorConnector.objects.get(dictionary_value_id=i['id'])
        except MonitorConnector.DoesNotExist:
            item= MonitorConnector.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='11515',
                attribute_name='Разъёмы монитора',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 21031,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=HDRStandard.objects.get(dictionary_value_id=i['id'])
        except HDRStandard.DoesNotExist:
            item= HDRStandard.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='21031',
                attribute_name='Стандарты HDR',
                is_required=False,
                category_dependent=False
            )
    #===============================================================================
    task = {
    "attribute_id": 85,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=Brand_Monitor.objects.get(dictionary_value_id=i['id'])
        except Brand_Monitor.DoesNotExist:
            item= Brand_Monitor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='85',
                attribute_name='Бренд',
                is_required=True,
                category_dependent=True
            )
    #===============================================================================
    task = {
    "attribute_id": 22232,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=EuroAsianCodeMonitor.objects.get(dictionary_value_id=i['id'])
        except EuroAsianCodeMonitor.DoesNotExist:
            item= EuroAsianCodeMonitor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='222232',
                attribute_name='ТН ВЭД коды ЕАЭС',
                is_required=True,
                category_dependent=True
            )
    #===============================================================================
    task = {
    "attribute_id": 10096,
    "description_category_id": 17028926,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 5000,
    "type_id": 91494
    }
    response=requests.post('https://api-seller.ozon.ru/v1/description-category/attribute/values', json=task, headers=headers) 
    status_code=response.status_code
    json=response.json()
    array=json['result']
    for i in array:
        try:
            item=ColourMonitor.objects.get(dictionary_value_id=i['id'])
        except ColourMonitor.DoesNotExist:
            item= ColourMonitor.objects.create(
                value=i['value'],
                dictionary_value_id=i['id'],
                attribute_id='10096',
                attribute_name='Цвет товара',
                is_required=False,
                category_dependent=True
            )
    


    return render (request, 'products.html')