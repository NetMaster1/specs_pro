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
    OSMobile,
    AndroidVersion,
    Interface,
    CommunicationStandard,
    SpecialFeature,
    ChargingFunction,
    Stabilization,
    IOSVersion,
    ESimSupport,
    RamSmartphone,
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
    BrandSmartphone, 
    TypeSmartphone, 
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
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    #В справочнике Ozon отсутствуют такие бренды как, Xiaomi, Redmi, Honor, Honor, Poco
    #Есть такие бренды как, Samsung
    #brand = models.ForeignKey(BrandSmartphone, on_delete=models.DO_NOTHING, null=True)
    #=================================================================
    created = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(Name, on_delete=models.DO_NOTHING, null=True, blank=True)
    comms_standard = models.ManyToManyField(CommunicationStandard, blank=True)
    sim_type = models.ManyToManyField(SimType, blank=True)
    esim_support = models.ForeignKey(ESimSupport, on_delete=models.SET_NULL, null=True, blank=True)
    ram = models.ForeignKey(RamSmartphone, on_delete=models.SET_NULL, null=True, blank=True)
    hard_drive = models.ForeignKey(HardDrive, on_delete=models.SET_NULL, null=True)
    #Записывается только число. Десятичные цифры
    screen_size = models.ForeignKey(ScreenSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    qnty_of_basic_cameras = models.ForeignKey(QntyOfBasicCamera, on_delete=models.SET_NULL, null=True, blank=True)
    #===============================================================
    operation_system = models.ForeignKey(OSMobile, on_delete=models.SET_NULL, null=True, blank=True)
    android_version = models.ForeignKey(AndroidVersion, on_delete=models.SET_NULL, null=True, blank=True)
    ios_version = models.ForeignKey(IOSVersion, on_delete=models.SET_NULL, null=True, blank=True)
    #================================================================
    product_set = models.ForeignKey(ProductSet, on_delete=models.DO_NOTHING, null=True, blank=True)
    publishing_year = models.ForeignKey(PublishingYear, on_delete=models.SET_NULL, null=True, blank=True)
    country_of_manufacture = models.ManyToManyField(CountryOfManufacture, blank=True)

    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.DO_NOTHING, null=True)
    life_span = models.ForeignKey(LifeSpan, on_delete=models.DO_NOTHING, null=True, blank=True)
    sim_card_qnty = models.ForeignKey(SimCardQnty, on_delete=models.SET_NULL, null=True, blank=True)
    #=================================================================
    processor = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True, blank=True)
    processor_brand = models.ForeignKey(ProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    processor_model = models.ForeignKey(ProcessorModel, on_delete=models.SET_NULL, null=True, blank=True)
    processor_core_qnty = models.ForeignKey(ProcessorCoreQnty, on_delete=models.SET_NULL, null=True, blank=True)
    processor_frequency = models.ForeignKey(ProcessorFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_processor_brand = models.ForeignKey(VideoProcessorBrand, on_delete=models.SET_NULL, null=True, blank=True)
    video_processor = models.ForeignKey(VideoProcessor, on_delete=models.SET_NULL, null=True, blank=True)
    #=================================================================
    card_type = models.ManyToManyField(CardType, blank=True)
    microsd_slot = models.ForeignKey(MicroSDSlot, on_delete=models.SET_NULL, null=True, blank=True)
    max_card_volume = models.ForeignKey(MaxCardVolume, on_delete=models.SET_NULL, null=True, blank=True)#записывается только целое число
    #==================================================================
    #Записывается только число. Десятичные цифры
    battery_capacity = models.ForeignKey(BatteryCapacity, on_delete=models.DO_NOTHING, null=True, blank=True)
    charging_function = models.ManyToManyField(ChargingFunction, blank=True)
    #Записывается только число. Десятичные цифры
    standby_period = models.ForeignKey(StandByPeriod, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Записывается только число. Десятичные цифры
    work_period = models.ForeignKey(WorkPeriod, on_delete=models.DO_NOTHING, null=True, blank=True)
    #==================================================================
    matrix_type = models.ForeignKey(MatrixType, on_delete=models.SET_NULL, null=True, blank=True)
    screen_resolution = models.ForeignKey(ScreenResolution, on_delete=models.SET_NULL, null=True, blank=True)
    #==================================================================
    camera_function = models.ManyToManyField(CameraFunction, blank=True)
    stabilization = models.ManyToManyField(Stabilization, blank=True)
    #Записывается только число. Десятичные цифры
    basic_camera_resolution = models.ForeignKey(BasicCamerResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Записывается только число. Десятичные цифры
    front_camera_resolution = models.ForeignKey(FrontCamerResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Записывается только число. Десятичные цифры. Измеряется в кадр/сек
    record_max_speed = models.ForeignKey(RecordMaxSpeed, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_quality = models.ForeignKey(VideoQuality, on_delete=models.SET_NULL, null=True, blank=True)
    #==================================================================
    wifi = models.ManyToManyField(WifiType, blank=True)
    bluetooth = models.ForeignKey(BluetoothType, on_delete=models.SET_NULL, null=True, blank=True)
    wireless_interface = models.ManyToManyField(WirelessInterface, blank=True)
    interface = models.ManyToManyField(Interface, blank=True)
    #===================================================================
    sensor = models.ManyToManyField(Sensor, blank=True)
    navigation = models.ManyToManyField(NavigationType, blank=True)
    authentification = models.ManyToManyField(Authentication, blank=True)
    #====================================================================
    case_form = models.ForeignKey(CaseForm, on_delete=models.SET_NULL, null=True, blank=True)
    case_material = models.ManyToManyField(CaseMaterial, blank=True)
    #Размеры сторон товара без упаковки – длина х ширина х высота в миллиметрах (указывать через Х). 
    #Длина – самая большая сторона, высота – самая маленькая
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Вес товара без упаковки (нетто) в граммах в расчете на 1 SKU. Допустимо указывать только цифры
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, null=True, blank=True)
    colour = models.ManyToManyField(Colour, blank=True)
    special_feature = models.ManyToManyField(SpecialFeature, blank=True)
    #=====================================================================
    marketing_colour = models.ForeignKey(MarketingColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, null=True, blank=True)
    key_word = models.ForeignKey(KeyWord, on_delete=models.DO_NOTHING, null=True, blank=True)
    #=========================================================================
    #EAС (Ростест)
    smartphone_version = models.ForeignKey(SmartphoneVersion, on_delete=models.SET_NULL, null=True, blank=True)
    #(для объединения в одну карточку)
    #Укажите название модели товара. Не указывайте в этом поле тип и бренд.
    model_name = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)#9048
    gadget_model = models.ManyToManyField(GadgetModel, blank=True)#5219
    type = models.ForeignKey(TypeSmartphone, on_delete=models.SET_NULL, null=True)
    gadget_serie = models.ForeignKey(GadgetSerie, on_delete=models.SET_NULL, null=True, blank=True)
    #=====================================================================================
    #Каталожный номер изделия или детали. Is_required=True. Можно использовать EAN
    #Не можем использовать IMEI телефона, так как они разные у одного SKU
    part_number = models.ForeignKey(PartNumber, on_delete=models.DO_NOTHING, null=True)
    # Цифро-буквенный код товара для его учета, является уникальным среди товаров бренда. 
    # Не является EAN/серийным номером/штрихкодом, не равен названию модели товара - 
    # для этих параметров есть отдельные атрибуты. Артикул выводится в карточке товара на сайте 
    # и может использоваться при автоматическом формировании названия товара.
    #=============================================================================
    #seller_code = models.ForeignKey(SellerCode, on_delete=models.DO_NOTHING, null=True, blank=True)
    hazard_grade = models.ForeignKey(HazardGrade, on_delete=models.SET_NULL, null=True, blank=True)
    protection_grade = models.ManyToManyField(ProtectionGrade, blank=True)
    #euro_asian_code = models.ForeignKey(EuroAsianCode, on_delete=models.SET_NULL, null=True, blank=True)
    #======================dictionary_id > 0==================================================
    
    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'
