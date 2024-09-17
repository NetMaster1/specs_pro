from django.db import models
from app_reference_shared.models import (
    OzonCategory, 
    Authentication, 
    HardDrive, 
    CountryOfManufacture, 
    MatrixType, 
    CardType, 
    BluetoothType, 
    NavigationType, 
    Sensor,
    SimType,
    WifiType,
    VideoProcessorBrand,
    GadgetSerie,
    CameraFunction,
    HazardGrade,
    VideoProcessor,
    ProcessorBrand,
    ProcessorModel,
    WirelessInterface,
    CaseMaterial,
    OperationSystem,
    AndroidVersion,
    Interface,
    CommunicationStandard,
    SpecialFeature,
    ChargingFunction,
    Stabilization,
    IOSVersion,
    ESimSupport,
    RAM,
    PublishingYear,
    SmartphoneVersion,
    WarrantyPeriod,
    ModelName
)
from app_reference_smartphones.models import (
    Brand, 
    Type, 
    ScreenResolution, 
    VideoQuality, 
    GadgetModel, 
    ProtectionGrade, 
    Colour, 
    QntyOfBasicCamera, 
    Processor,
    ProcessorCoreQnty,
    MicroSDSlot,
    CaseForm,
    EuroAsianCode,
    SimCardQnty
)


class Smartphone (models.Model):
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=160)
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)
    part_number = models.CharField(max_length=15, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.DO_NOTHING, null=True)
    model_name = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)
    hard_drive = models.ForeignKey(HardDrive, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    marketing_text = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)#Без упаковки; в мм; длина х ширина х высота; длина самая большая, высота - самая маленькая
    weight = models.CharField(max_length=50, null=True, blank=True)#вес в г
    product_set = models.CharField(max_length=100, null=True, blank=True)#перечислить, что входит в товар
    country_of_manufacture = models.ForeignKey(CountryOfManufacture, on_delete=models.SET_NULL, null=True, blank=True)
    matrix_type = models.ForeignKey(MatrixType, on_delete=models.SET_NULL, null=True, blank=True)
    sim_card_qnty = models.ForeignKey(SimCardQnty, on_delete=models.SET_NULL, null=True, blank=True)
    card_type = models.ForeignKey(CardType, on_delete=models.SET_NULL, null=True, blank=True)
    card_max_volume = models.CharField(max_length=15, null=True, blank=True)#записывается только целое число
    bluetooth = models.ForeignKey(BluetoothType, on_delete=models.SET_NULL, null=True, blank=True)
    navigation = models.ForeignKey(NavigationType, on_delete=models.SET_NULL, null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True, blank=True)
    front_camera_resolution = models.CharField(max_length=25, null=True, blank=True)
    basic_camera_resolution = models.CharField(max_length=25, null=True, blank=True)
    battery_capacity = models.CharField(max_length=25, null=True, blank=True)
    sim_type = models.ForeignKey(SimType, on_delete=models.SET_NULL, null=True, blank=True)
    standby_period = models.CharField(max_length=25, null=True, blank=True)
    wifi = models.ForeignKey(WifiType, on_delete=models.SET_NULL, null=True, blank=True)
    video_processor_brand = models.ForeignKey(VideoProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    screen_resolution = models.ForeignKey(ScreenResolution, on_delete=models.SET_NULL, null=True, blank=True)
    video_quality = models.ForeignKey(VideoQuality, on_delete=models.SET_NULL, null=True, blank=True)
    gadget_model = models.ForeignKey(GadgetModel, on_delete=models.SET_NULL, null=True, blank=True)
    protection_grade = models.ForeignKey(ProtectionGrade, on_delete=models.SET_NULL, null=True, blank=True)
    work_period = models.CharField(max_length=25, null=True, blank=True)
    record_max_speed = models.CharField(max_length=25, null=True, blank=True)
    life_span = models.CharField(max_length=25, null=True, blank=True)
    screen_size = models.CharField(max_length=25, null=True, blank=True)
    seller_code = models.CharField(max_length=25, null=True, blank=True)
    gadget_serie = models.ForeignKey(GadgetSerie, on_delete=models.SET_NULL, null=True, blank=True)
    camera_function = models.ForeignKey(CameraFunction, on_delete=models.SET_NULL, null=True, blank=True)
    hazard_grade = models.ForeignKey(HazardGrade, on_delete=models.SET_NULL, null=True, blank=True)
    colour = models.ForeignKey(Colour, on_delete=models.SET_NULL, null=True, blank=True)
    marketing_colour = models.CharField(max_length=50, null=True, blank=True)
    qnty_of_basic_cameras = models.ForeignKey(QntyOfBasicCamera, on_delete=models.SET_NULL, null=True, blank=True)
    processor = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True, blank=True)
    video_processor = models.ForeignKey(VideoProcessor, on_delete=models.SET_NULL, null=True, blank=True)
    processor_brand = models.ForeignKey(ProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    processor_frequency = models.CharField(max_length=15, null=True, blank=True)
    processor_core_qnty = models.ForeignKey(ProcessorCoreQnty, on_delete=models.SET_NULL, null=True, blank=True)
    processor_model = models.ForeignKey(ProcessorModel, on_delete=models.SET_NULL, null=True, blank=True)
    wireless_interface = models.ForeignKey(WirelessInterface, on_delete=models.SET_NULL, null=True, blank=True)
    case_material = models.ForeignKey(CaseMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    operation_system = models.ForeignKey(OperationSystem, on_delete=models.SET_NULL, null=True, blank=True)
    android_version = models.ForeignKey(AndroidVersion, on_delete=models.SET_NULL, null=True, blank=True)
    interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, null=True, blank=True)
    comms_standard = models.ForeignKey(CommunicationStandard, on_delete=models.SET_NULL, null=True)
    microsd_slot = models.ForeignKey(MicroSDSlot, on_delete=models.SET_NULL, null=True, blank=True)
    special_feature = models.ForeignKey(SpecialFeature, on_delete=models.SET_NULL, null=True, blank=True)
    charging_function = models.ForeignKey(ChargingFunction, on_delete=models.SET_NULL, null=True, blank=True)
    Stabilization = models.ForeignKey(Stabilization, on_delete=models.SET_NULL, null=True, blank=True)
    authentification = models.ForeignKey(Authentication, on_delete=models.SET_NULL, null=True, blank=True)
    case_form = models.ForeignKey(CaseForm, on_delete=models.SET_NULL, null=True, blank=True)
    ios_version = models.ForeignKey(IOSVersion, on_delete=models.SET_NULL, null=True, blank=True)
    euro_asian_code = models.ForeignKey(EuroAsianCode, on_delete=models.SET_NULL, null=True, blank=True)
    esim_support = models.ForeignKey(ESimSupport, on_delete=models.SET_NULL, null=True, blank=True)
    ram = models.ForeignKey(RAM, on_delete=models.SET_NULL, null=True, blank=True)
    publishing_year = models.ForeignKey(PublishingYear, on_delete=models.SET_NULL, null=True, blank=True)
    smartphone_version = models.ForeignKey(SmartphoneVersion, on_delete=models.SET_NULL, null=True, blank=True)
    EAN = models.CharField(max_length=15, null=True)
    
    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'
