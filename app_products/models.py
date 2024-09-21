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
    ModelName,
    PartNumber,
    Weight,
    Size,
    ProductSet,
    FrontCamerResolution,
    BasicCamerResolution,
    BatteryCapacity,
    StandByPeriod,
    WorkPeriod,
    RecordMaxSpeed,
    LifeSpan,
    ScreenSize,
    SellerCode,
    MarketingColour,
    ProcessorFrequency,
    Name,
    Description,
    KeyWord,
    MaxCardVolume

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
    SimCardQnty,
    
)

class Smartphone (models.Model):
    created = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(Name, on_delete=models.DO_NOTHING, null=True, blank=True)
    part_number = models.ForeignKey(PartNumber, on_delete=models.DO_NOTHING, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, null=True, blank=True)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, null=True, blank=True)
    product_set = models.ForeignKey(ProductSet, on_delete=models.DO_NOTHING, null=True, blank=True)
    front_camera_resolution = models.ForeignKey(FrontCamerResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    basic_camera_resolution = models.ForeignKey(BasicCamerResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    battery_capacity = models.ForeignKey(BatteryCapacity, on_delete=models.DO_NOTHING, null=True, blank=True)
    standby_period = models.ForeignKey(StandByPeriod, on_delete=models.DO_NOTHING, null=True, blank=True)
    work_period = models.ForeignKey(WorkPeriod, on_delete=models.DO_NOTHING, null=True, blank=True)
    life_span = models.ForeignKey(LifeSpan, on_delete=models.DO_NOTHING, null=True, blank=True)
    record_max_speed = models.ForeignKey(RecordMaxSpeed, on_delete=models.DO_NOTHING, null=True, blank=True)
    screen_size = models.ForeignKey(ScreenSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    seller_code = models.ForeignKey(SellerCode, on_delete=models.DO_NOTHING, null=True, blank=True)
    processor_frequency = models.ForeignKey(ProcessorFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    marketing_colour = models.ForeignKey(MarketingColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, null=True, blank=True)
    key_word = models.ForeignKey(KeyWord, on_delete=models.DO_NOTHING, null=True, blank=True)
    #======================dictionary_id > 0==================================================
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.DO_NOTHING, null=True)
    model_name = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)
    hard_drive = models.ForeignKey(HardDrive, on_delete=models.SET_NULL, null=True)
    country_of_manufacture = models.ManyToManyField(CountryOfManufacture, blank=True)
    matrix_type = models.ForeignKey(MatrixType, on_delete=models.SET_NULL, null=True, blank=True)
    sim_card_qnty = models.ForeignKey(SimCardQnty, on_delete=models.SET_NULL, null=True, blank=True)
    card_type = models.ManyToManyField(CardType, blank=True)
    max_card_volume = models.ForeignKey(MaxCardVolume, on_delete=models.SET_NULL, null=True, blank=True)#записывается только целое число
    bluetooth = models.ForeignKey(BluetoothType, on_delete=models.SET_NULL, null=True, blank=True)
    navigation = models.ManyToManyField(NavigationType, blank=True)
    sensor = models.ManyToManyField(Sensor, blank=True)
    sim_type = models.ManyToManyField(SimType, blank=True)
    wifi = models.ManyToManyField(WifiType, blank=True)
    video_processor_brand = models.ForeignKey(VideoProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    screen_resolution = models.ForeignKey(ScreenResolution, on_delete=models.SET_NULL, null=True, blank=True)
    video_quality = models.ForeignKey(VideoQuality, on_delete=models.SET_NULL, null=True, blank=True)
    #gadget_model = models.ForeignKey(GadgetModel, on_delete=models.SET_NULL, null=True, blank=True)
    gadget_model = models.ManyToManyField(GadgetModel, blank=True)
    protection_grade = models.ManyToManyField(ProtectionGrade, blank=True)
    #protection_grade = models.ForeignKey(ProtectionGrade, on_delete=models.SET_NULL, null=True, blank=True)
    gadget_serie = models.ForeignKey(GadgetSerie, on_delete=models.SET_NULL, null=True, blank=True)
    camera_function = models.ManyToManyField(CameraFunction, blank=True)
    hazard_grade = models.ForeignKey(HazardGrade, on_delete=models.SET_NULL, null=True, blank=True)
    colour = models.ManyToManyField(Colour, blank=True)
    qnty_of_basic_cameras = models.ForeignKey(QntyOfBasicCamera, on_delete=models.SET_NULL, null=True, blank=True)
    processor = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True, blank=True)
    video_processor = models.ForeignKey(VideoProcessor, on_delete=models.SET_NULL, null=True, blank=True)
    processor_brand = models.ForeignKey(ProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    processor_core_qnty = models.ForeignKey(ProcessorCoreQnty, on_delete=models.SET_NULL, null=True, blank=True)
    processor_model = models.ForeignKey(ProcessorModel, on_delete=models.SET_NULL, null=True, blank=True)
    wireless_interface = models.ManyToManyField(WirelessInterface, blank=True)
    case_material = models.ManyToManyField(CaseMaterial, blank=True)
    operation_system = models.ForeignKey(OperationSystem, on_delete=models.SET_NULL, null=True, blank=True)
    android_version = models.ForeignKey(AndroidVersion, on_delete=models.SET_NULL, null=True, blank=True)
    interface = models.ManyToManyField(Interface, blank=True)
    comms_standard = models.ManyToManyField(CommunicationStandard, blank=True)
    microsd_slot = models.ForeignKey(MicroSDSlot, on_delete=models.SET_NULL, null=True, blank=True)
    special_feature = models.ManyToManyField(SpecialFeature, blank=True)
    charging_function = models.ManyToManyField(ChargingFunction, blank=True)
    stabilization = models.ManyToManyField(Stabilization, blank=True)
    authentification = models.ManyToManyField(Authentication, blank=True)
    case_form = models.ForeignKey(CaseForm, on_delete=models.SET_NULL, null=True, blank=True)
    ios_version = models.ForeignKey(IOSVersion, on_delete=models.SET_NULL, null=True, blank=True)
    euro_asian_code = models.ForeignKey(EuroAsianCode, on_delete=models.SET_NULL, null=True, blank=True)
    esim_support = models.ForeignKey(ESimSupport, on_delete=models.SET_NULL, null=True, blank=True)
    ram = models.ForeignKey(RAM, on_delete=models.SET_NULL, null=True, blank=True)
    publishing_year = models.ForeignKey(PublishingYear, on_delete=models.SET_NULL, null=True, blank=True)
    smartphone_version = models.ForeignKey(SmartphoneVersion, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'
