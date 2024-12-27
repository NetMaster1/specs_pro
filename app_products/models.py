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
    CardTitleModelName,
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
    MaxCardVolume,
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
    SpecialFeatureSmartphone,
    ProcessorModelNotebook,
    PortQntyUSB,
    PowerOffWorkTime,
    NotebookBatteryCapacity,
    PortQntyUSB3Gen1,
    NotebookFormFactor,
    Chipset,
    RAMFormFactor,
    PortQntyUSB3Gen2,
    DVDrive,
    VideoCardType,
    SoundConfig,
    ManualInputDevice,
    ManualInputDeviceFeature,
    LANCard,
    BuiltInDevice,
    WebCamResolution,
    CaseCoating,
    PortQntyThunderbolt,
    DisplayPort,
    BatteryType,
    PowerSupplyVoltage,
    MaxScreenFrequency,
    CardReader,
    NotebookWeight,
    TotalDiskVolume,
    TotalHDDVolume,
    TotalSSDVolume,
    ScreenSize,
    PortQntyTypeC,
    Configuration,
    NotebookProcessor,
    NotebookProcessorBrand,
    NotebookVideoProcessorBrand,
    OperationSystem,
    VideoProcessorFamily,
    NotebookMatrixType,
    WindowsVersion,
    MacOSVersion,
    KeyboardLayout,
    WebCamShutter
    
)

from app_notebook_reference.models import (BrandNotebook, HDDQnty, RAMNotebook, NotebookRAMType, NotebookMaxRAM, RAMExtraSlot, SSDQnty,
    VideoRAM, KeyboardColour, NotebookCaseMaterial, NotebookInterfacesConnector, BatteryElementQnty, NotebookScreenResolution,
    HDDFormFactor, SSDFormFactor, StorageType, VideoCard, VRSupport, NotebookColour, TouchScreen, NotebookProcessorCoreQnty,
    KeyboardLightning, MobileCommsModule, TypeNotebook,
    )

from app_reference_smartphones.models import (BrandSmartphone, TypeSmartphone, ScreenResolution, VideoQuality, GadgetModel, ProtectionGrade,
    Colour, QntyOfBasicCamera, Processor, ProcessorCoreQnty, MicroSDSlot, CaseForm, EuroAsianCode, SimCardQnty,

    )

from app_monitor_reference.models import(Resolution, TypeMonitor, USBPort, BuiltinSpeaker, CurvedDispaly, HDR, ColourMonitor, Brand_Monitor,
    EuroAsianCodeMonitor,
    )

class Notebook (models.Model):
    #Дополнительное поле. Не входит в attributes for notebook. Использую просто для связи с таблицей категории.
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now=True)
    #В справочнике Ozon отсутствуют такие бренды как, Xiaomi, Redmi, Honor, Honor, Poco
    #Есть такие бренды как, Samsung
    brand_notebook = models.ForeignKey(BrandNotebook, on_delete=models.DO_NOTHING, null=True)
    #Выберите наиболее подходящий тип товара. По типам товары распределяются по категориям на сайте Ozon. 
    #Если тип указан неправильно, товар попадет в неверную категорию.
    type_notebook = models.ForeignKey(TypeNotebook, on_delete=models.SET_NULL, null=True)
    #name = models.ForeignKey(Name, on_delete=models.DO_NOTHING, null=True, blank=True)#4180
    #(для объединения в одну карточку)
    #Укажите название модели товара. Не указывайте в этом поле тип и бренд.
    #Заполните данное поле любым одинаковым значением у товаров, которые хотите объединить. 
    #И по разному, чтобы разъединить. Объединение через данный атрибут произойдет только если товары имеют одинаковый Тип и Бренд
    model_name_notebook = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)#9048
    notebook_processor_model = models.ForeignKey(ProcessorModelNotebook, on_delete=models.SET_NULL, null=True, blank=True)
    product_set = models.ForeignKey(ProductSet, on_delete=models.DO_NOTHING, null=True, blank=True)
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.DO_NOTHING, null=True)
    country_of_manufacture = models.ManyToManyField(CountryOfManufacture, blank=True)
    bluetooth = models.ForeignKey(BluetoothType, on_delete=models.SET_NULL, null=True, blank=True)
    port_qnty_USB = models.ForeignKey(PortQntyUSB, on_delete=models.SET_NULL, null=True, blank=True)
    power_off_work_time = models.ForeignKey(PowerOffWorkTime, on_delete=models.SET_NULL, null=True, blank=True)
    battery_capacity = models.ForeignKey(BatteryCapacity, on_delete=models.DO_NOTHING, null=True, blank=True)#4429
    port_usb3_gen1 = models.ForeignKey(PortQntyUSB3Gen1, on_delete=models.DO_NOTHING, null=True, blank=True)
    hdd_qnty = models.ForeignKey(HDDQnty, on_delete=models.DO_NOTHING, null=True, blank=True)
    notebook_form_factor = models.ForeignKey(NotebookFormFactor, on_delete=models.DO_NOTHING, null=True, blank=True)
    chipset = models.ForeignKey(Chipset, on_delete=models.DO_NOTHING, null=True, blank=True)
    notebook_ram = models.ForeignKey(RAMNotebook, on_delete=models.DO_NOTHING, null=True, blank=True)
    notebook_ram_type = models.ForeignKey(NotebookRAMType, on_delete=models.DO_NOTHING, null=True, blank=True)
    notebook_max_ram= models.ForeignKey(NotebookMaxRAM, on_delete=models.DO_NOTHING, null=True, blank=True)
    port_usb3_gen2 = models.ForeignKey(PortQntyUSB3Gen2, on_delete=models.DO_NOTHING, null=True, blank=True)
    ram_form_factor= models.ForeignKey(RAMFormFactor, on_delete=models.DO_NOTHING, null=True, blank=True)
    ram_extra_slot= models.ForeignKey(RAMExtraSlot, on_delete=models.DO_NOTHING, null=True, blank=True)
    ssd_qnty= models.ForeignKey(SSDQnty, on_delete=models.DO_NOTHING, null=True, blank=True)
    dvd_drive= models.ForeignKey(DVDrive, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_card_type= models.ForeignKey(VideoCardType, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_ram= models.ForeignKey(VideoRAM, on_delete=models.DO_NOTHING, null=True, blank=True)
    lightning_type= models.ForeignKey(LightningType, on_delete=models.DO_NOTHING, null=True, blank=True)
    screen_coating= models.ForeignKey(ScreenCoating, on_delete=models.DO_NOTHING, null=True, blank=True)
    sound_config= models.ForeignKey(SoundConfig, on_delete=models.DO_NOTHING, null=True, blank=True)
    manual_input_device= models.ForeignKey(ManualInputDevice, on_delete=models.DO_NOTHING, null=True, blank=True)
    manual_input_device_feature= models.ForeignKey(ManualInputDeviceFeature, on_delete=models.DO_NOTHING, null=True, blank=True)
    keyboard_colour= models.ForeignKey(KeyboardColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    wifi_type= models.ForeignKey(WifiType, on_delete=models.DO_NOTHING, null=True, blank=True)
    lan_card= models.ForeignKey(LANCard, on_delete=models.DO_NOTHING, null=True, blank=True)
    builtin_device= models.ForeignKey(BuiltInDevice, on_delete=models.DO_NOTHING, null=True, blank=True)
    web_cam_resolution= models.ForeignKey(WebCamResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_case_material= models.ForeignKey(NotebookCaseMaterial, on_delete=models.DO_NOTHING, null=True, blank=True)
    case_coating= models.ForeignKey(CaseCoating, on_delete=models.DO_NOTHING, null=True, blank=True)
    interface_connector= models.ForeignKey(NotebookInterfacesConnector, on_delete=models.DO_NOTHING, null=True, blank=True)
    port_qnty_thunderbolt= models.ForeignKey(PortQntyThunderbolt, on_delete=models.DO_NOTHING, null=True, blank=True)
    port_hdmi= models.ForeignKey(HDMIPort, on_delete=models.DO_NOTHING, null=True, blank=True)
    display_port= models.ForeignKey(DisplayPort, on_delete=models.DO_NOTHING, null=True, blank=True)
    battery_element_qnty= models.ForeignKey(BatteryElementQnty, on_delete=models.DO_NOTHING, null=True, blank=True)
    battery_type= models.ForeignKey(BatteryType, on_delete=models.DO_NOTHING, null=True, blank=True)
    power_supply_voltage= models.ForeignKey(PowerSupplyVoltage, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_screen_resolution= models.ForeignKey(NotebookScreenResolution, on_delete=models.DO_NOTHING, null=True, blank=True)
    max_screen_frequency= models.ForeignKey(MaxScreenFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    card_reader= models.ForeignKey(CardReader, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_weight= models.ForeignKey(NotebookWeight, on_delete=models.DO_NOTHING, null=True, blank=True)
    life_span= models.ForeignKey(LifeSpan, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_disk_volume= models.ForeignKey(TotalDiskVolume, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_hdd_volume= models.ForeignKey(TotalHDDVolume, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_ssd_volume= models.ForeignKey(TotalSSDVolume, on_delete=models.DO_NOTHING, null=True, blank=True)
    screen_size= models.ForeignKey(ScreenSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    port_TypeC= models.ForeignKey(PortQntyTypeC, on_delete=models.DO_NOTHING, null=True, blank=True)
    hdd_form_factor= models.ForeignKey(HDDFormFactor, on_delete=models.DO_NOTHING, null=True, blank=True)
    ssd_form_factor= models.ForeignKey(SSDFormFactor, on_delete=models.DO_NOTHING, null=True, blank=True)
    storage_type= models.ForeignKey(StorageType, on_delete=models.DO_NOTHING, null=True, blank=True)
    configuration= models.ForeignKey(Configuration, on_delete=models.DO_NOTHING, null=True, blank=True)
    hazard_grade= models.ForeignKey(HazardGrade, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_processor= models.ForeignKey(NotebookProcessor, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_card= models.ForeignKey(VideoCard, on_delete=models.DO_NOTHING, null=True, blank=True)
    vr_support= models.ForeignKey(VRSupport, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_colour= models.ForeignKey(NotebookColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    marketing_colour= models.ForeignKey(MarketingColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    touch_screen= models.ForeignKey(TouchScreen, on_delete=models.DO_NOTHING, null=True, blank=True)
    processor_frequency= models.ForeignKey(ProcessorFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_processor_core_qnty= models.ForeignKey(NotebookProcessorCoreQnty, on_delete=models.DO_NOTHING, null=True, blank=True)
    case_material= models.ForeignKey(CaseMaterial, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_processor_brand= models.ForeignKey(NotebookProcessorBrand, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_video_processor_brand= models.ForeignKey(NotebookVideoProcessorBrand, on_delete=models.DO_NOTHING, null=True, blank=True)
    operation_system= models.ForeignKey(OperationSystem, on_delete=models.DO_NOTHING, null=True, blank=True)
    video_processor_family= models.ForeignKey(VideoProcessorFamily, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_matrix_type= models.ForeignKey(NotebookMatrixType, on_delete=models.DO_NOTHING, null=True, blank=True)
    windows_version= models.ForeignKey(WindowsVersion, on_delete=models.DO_NOTHING, null=True, blank=True)
    mac_os_version= models.ForeignKey(MacOSVersion, on_delete=models.DO_NOTHING, null=True, blank=True)
    keyboard_lightning= models.ForeignKey(KeyboardLightning, on_delete=models.DO_NOTHING, null=True, blank=True)
    mobile_comms_module= models.ForeignKey(MobileCommsModule, on_delete=models.DO_NOTHING, null=True, blank=True)
    keyboard_layout= models.ForeignKey(KeyboardLayout, on_delete=models.DO_NOTHING, null=True, blank=True)
    web_cam_shutter= models.ForeignKey(WebCamShutter, on_delete=models.DO_NOTHING, null=True, blank=True)
    key_word = models.ForeignKey(KeyWord, on_delete=models.DO_NOTHING, null=True, blank=True)
    nb_battery_capacity = models.ForeignKey(NotebookBatteryCapacity, on_delete=models.DO_NOTHING, null=True, blank=True)
   
    # #=====================MODEL NAMES=====================================
    # #Выберите одно значение из выпадающего списка
    # gadget_model = models.ManyToManyField(GadgetModel, blank=True)#5219
    # #(для объединения в одну карточку)
    # #Укажите название модели товара. Не указывайте в этом поле тип и бренд.
    # #Заполните данное поле любым одинаковым значением у товаров, которые хотите объединить. 
    # #И по разному, чтобы разъединить. Объединение через данный атрибут произойдет только если товары имеют одинаковый Тип и Бренд
    # model_name_smartphone = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)#9048
    # #Только краткое название модели, без типа, бренда и характеристик товара. Будет использовано в шаблонизаторе 
    # #для составления названия карточки для сайта.
    # card_title_model_name = models.ForeignKey(CardTitleModelName, on_delete=models.DO_NOTHING, null=True)#11241
    
    # #=====================================================================================
    # #Каталожный номер изделия или детали. Is_required=True. Можно использовать EAN
    # #Не можем использовать IMEI телефона, так как они разные у одного SKU
    # part_number = models.ForeignKey(PartNumber, on_delete=models.DO_NOTHING, null=True)
    # # Цифро-буквенный код товара для его учета, является уникальным среди товаров бренда. 
    # # Не является EAN/серийным номером/штрихкодом, не равен названию модели товара - 
    # # для этих параметров есть отдельные атрибуты. Артикул выводится в карточке товара на сайте 
    # # и может использоваться при автоматическом формировании названия товара.
    # #seller_code = models.ForeignKey(SellerCode, on_delete=models.DO_NOTHING, null=True, blank=True)
    # euro_asian_code_monitor = models.ForeignKey(EuroAsianCodeMonitor, on_delete=models.SET_NULL, null=True, blank=True)
    #======================dictionary_id > 0==================================================
    image_1 = models.URLField(blank=True)
    image_2 = models.URLField(blank=True)
    image_3 = models.URLField(blank=True)
    image_4 = models.URLField(blank=True)
    image_5 = models.URLField(blank=True)

    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'notebook'
        verbose_name_plural = 'notebooks'

class Smartphone (models.Model):
    #Дополнительное поле. Не входит в attributes for smartphone. Использую просто для связи с таблицей категории.
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    #В справочнике Ozon отсутствуют такие бренды как, Xiaomi, Redmi, Honor, Honor, Poco
    #Есть такие бренды как, Samsung
    brand = models.ForeignKey(BrandSmartphone, on_delete=models.DO_NOTHING, null=True)
    #Выберите наиболее подходящий тип товара. По типам товары распределяются по категориям на сайте Ozon. 
    #Если тип указан неправильно, товар попадет в неверную категорию.
    type_smartphone = models.ForeignKey(TypeSmartphone, on_delete=models.SET_NULL, null=True)
    #=================================================================
    created = models.DateTimeField(auto_now=True)
    #Название пишется по принципу:\nТип + Бренд + Модель (серия + пояснение) + Артикул производителя + , 
    #(запятая) + Атрибут\nНазвание не пишется большими буквами (не используем caps lock).\n
    #Перед атрибутом ставится запятая. Если атрибутов несколько, они так же разделяются запятыми.\n
    # Если какой-то составной части названия нет - пропускаем её.\nАтрибутом может быть: цвет, вес, объём, 
    # количество штук в упаковке и т.д.\nЦвет пишется с маленькой буквы, в мужском роде, единственном числе.\n
    # Слово цвет в названии не пишем.\nТочка в конце не ставится.\nНикаких знаков препинания, кроме запятой, не используем.\n
    # Кавычки используем только для названий на русском языке.\nПримеры корректных названий:\nСмартфон Apple iPhone XS MT572RU/A, 
    # space black \nКеды Dr. Martens Киноклассика, бело-черные, размер 43\nСтиральный порошок Ariel Магия белого с мерной ложкой, 
    # 15 кг\nСоус Heinz Xtreme Tabasco суперострый, 10 мл\nИгрушка для животных Четыре лапы \"Бегающая мышка\" БММ, белый
    name = models.ForeignKey(Name, on_delete=models.DO_NOTHING, null=True, blank=True)#4180
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
    special_feature = models.ManyToManyField(SpecialFeatureSmartphone, blank=True)
    #=====================================================================
    marketing_colour = models.ForeignKey(MarketingColour, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, null=True, blank=True)
    key_word = models.ForeignKey(KeyWord, on_delete=models.DO_NOTHING, null=True, blank=True)
    #=========================================================================
    #EAС (Ростест)
    smartphone_version = models.ForeignKey(SmartphoneVersion, on_delete=models.SET_NULL, null=True, blank=True)
    #=====================MODEL NAMES=====================================
    #Выберите одно значение из выпадающего списка
    gadget_model = models.ManyToManyField(GadgetModel, blank=True)#5219
    #(для объединения в одну карточку)
    #Укажите название модели товара. Не указывайте в этом поле тип и бренд.
    #Заполните данное поле любым одинаковым значением у товаров, которые хотите объединить. 
    #И по разному, чтобы разъединить. Объединение через данный атрибут произойдет только если товары имеют одинаковый Тип и Бренд
    model_name_smartphone = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)#9048
    #Только краткое название модели, без типа, бренда и характеристик товара. Будет использовано в шаблонизаторе 
    #для составления названия карточки для сайта.
    card_title_model_name = models.ForeignKey(CardTitleModelName, on_delete=models.DO_NOTHING, null=True)#11241
    #===========================================================================================
    #линейка мобильный устройств
    gadget_serie = models.ForeignKey(GadgetSerie, on_delete=models.SET_NULL, null=True, blank=True)#9225
    #=====================================================================================
    #Каталожный номер изделия или детали. Is_required=True. Можно использовать EAN
    #Не можем использовать IMEI телефона, так как они разные у одного SKU
    part_number = models.ForeignKey(PartNumber, on_delete=models.DO_NOTHING, null=True)
    # Цифро-буквенный код товара для его учета, является уникальным среди товаров бренда. 
    # Не является EAN/серийным номером/штрихкодом, не равен названию модели товара - 
    # для этих параметров есть отдельные атрибуты. Артикул выводится в карточке товара на сайте 
    # и может использоваться при автоматическом формировании названия товара.
    #seller_code = models.ForeignKey(SellerCode, on_delete=models.DO_NOTHING, null=True, blank=True)
    hazard_grade = models.ForeignKey(HazardGrade, on_delete=models.SET_NULL, null=True, blank=True)
    protection_grade = models.ManyToManyField(ProtectionGrade, blank=True)
    euro_asian_code_monitor = models.ForeignKey(EuroAsianCodeMonitor, on_delete=models.SET_NULL, null=True, blank=True)
    #======================dictionary_id > 0==================================================
    image_1 = models.URLField(blank=True)
    image_2 = models.URLField(blank=True)
    image_3 = models.URLField(blank=True)
    image_4 = models.URLField(blank=True)
    image_5 = models.URLField(blank=True)

   
    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'

class Monitor (models.Model):
    #Дополнительное поле. Не входит в attributes for smartphone. Использую просто для связи с таблицей категории.
    category_name = models.ForeignKey(OzonCategory, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now=True)
    #В справочнике Ozon отсутствуют такие бренды как, Xiaomi, Redmi, Honor, Honor, Poco
    #Есть такие бренды как, Samsung
    #=================================================================
    #Каталожный номер изделия или детали. Is_required=True. Можно использовать EAN
    #Не можем использовать IMEI телефона, так как они разные у одного SKU
    brand_monitor = models.ForeignKey(Brand_Monitor, on_delete=models.DO_NOTHING, null=True)
    part_number = models.ForeignKey(PartNumber, on_delete=models.DO_NOTHING, null=True)
    resolution = models.ForeignKey(Resolution, on_delete=models.DO_NOTHING, null=True, blank=True)#5592
    #Выберите наиболее подходящий тип товара. По типам товары распределяются по категориям на сайте Ozon. 
    #Если тип указан неправильно, товар попадет в неверную категорию. Чтобы правильно указать тип, найдите
    #на сайте Ozon товары, похожие на ваш, и посмотрите, какой тип у них указан. 8229; is_required,
    type = models.ForeignKey(TypeMonitor, on_delete=models.SET_NULL, null=True)
    #(для объединения в одну карточку)
    #Укажите название модели товара. Не указывайте в этом поле тип и бренд.
    #Заполните данное поле любым одинаковым значением у товаров, которые хотите объединить. 
    #И по разному, чтобы разъединить. Объединение через данный атрибут произойдет только если товары имеют одинаковый Тип и Бренд
    model_name = models.ForeignKey(ModelName, on_delete=models.DO_NOTHING, null=True)#9048
    #Название пишется по принципу:\nТип + Бренд + Модель (серия + пояснение) + Артикул производителя + , 
    #(запятая) + Атрибут\nНазвание не пишется большими буквами (не используем caps lock).\n
    #Перед атрибутом ставится запятая. Если атрибутов несколько, они так же разделяются запятыми.\n
    # Если какой-то составной части названия нет - пропускаем её.\nАтрибутом может быть: цвет, вес, объём, 
    # количество штук в упаковке и т.д.\nЦвет пишется с маленькой буквы, в мужском роде, единственном числе.\n
    # Слово цвет в названии не пишем.\nТочка в конце не ставится.\nНикаких знаков препинания, кроме запятой, не используем.\n
    # Кавычки используем только для названий на русском языке.\nПримеры корректных названий:\nСмартфон Apple iPhone XS MT572RU/A, 
    # space black \nКеды Dr. Martens Киноклассика, бело-черные, размер 43\nСтиральный порошок Ariel Магия белого с мерной ложкой, 
    # 15 кг\nСоус Heinz Xtreme Tabasco суперострый, 10 мл\nИгрушка для животных Четыре лапы \"Бегающая мышка\" БММ, белый
    name = models.ForeignKey(Name, on_delete=models.DO_NOTHING, null=True, blank=True)#4180
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Размеры сторон товара без упаковки – длина х ширина х высота в миллиметрах (указывать через Х). 
    #Длина – самая большая сторона, высота – самая маленькая
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, null=True, blank=True)
    product_set = models.ForeignKey(ProductSet, on_delete=models.DO_NOTHING, null=True, blank=True)
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.DO_NOTHING, null=True)
    country_of_manufacture = models.ManyToManyField(CountryOfManufacture, blank=True)
    lighting_type = models.ManyToManyField(LightningType, blank=True)
    screen_coating = models.ForeignKey(ScreenCoating, on_delete=models.DO_NOTHING, null=True, blank=True)
    hdmi_ports = models.ForeignKey(HDMIPort, on_delete=models.DO_NOTHING, null=True, blank=True)
    adjustments = models.ManyToManyField(Adjustment, blank=True)
    pixel_size = models.ForeignKey(PixelSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    ratio = models.ForeignKey(Ratio, on_delete=models.DO_NOTHING, null=True, blank=True)
    max_screen_frq = models.ForeignKey(MaxScreenFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    brightness = models.ForeignKey(Brightness, on_delete=models.DO_NOTHING, null=True, blank=True)
    contrast = models.ForeignKey(Contrast, on_delete=models.DO_NOTHING, null=True, blank=True)
    dynamic_contrast = models.ForeignKey(DynamicContrast, on_delete=models.DO_NOTHING, null=True, blank=True)
    look_angle = models.ForeignKey(LookAngle, on_delete=models.DO_NOTHING, null=True, blank=True)
    horizontal_frequency = models.ForeignKey(HorizontalFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    vertical_frequency = models.ForeignKey(VerticalFrequency, on_delete=models.DO_NOTHING, null=True, blank=True)
    web_camera = models.ForeignKey(WebCamera, on_delete=models.DO_NOTHING, null=True, blank=True)
    stand_adjustment = models.ForeignKey(StandAdjustment, on_delete=models.DO_NOTHING, null=True, blank=True)
    power_capacity = models.ForeignKey(PowerCapacity, on_delete=models.DO_NOTHING, null=True, blank=True)
    special_feature = models.ManyToManyField(SpecialFeature, blank=True)
    usb_port = models.ForeignKey(USBPort, on_delete=models.DO_NOTHING, null=True, blank=True)
    vesa_fixture = models.ManyToManyField(VESAFixture, blank=True)
    life_span = models.ForeignKey(LifeSpan, on_delete=models.DO_NOTHING, null=True, blank=True)
    screen_size = models.ForeignKey(ScreenSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    #seller_code = models.ForeignKey(SellerCode, on_delete=models.DO_NOTHING, null=True, blank=True)
    builtin_speaker = models.ForeignKey(BuiltinSpeaker, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Вес товара без упаковки (нетто) в граммах в расчете на 1 SKU. Допустимо указывать только цифры
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, null=True, blank=True)
    pixel_per_inch = models.ForeignKey(PixelPerInch, on_delete=models.DO_NOTHING, null=True, blank=True)
    colour_monitor = models.ManyToManyField(ColourMonitor, blank=True)
    monitor_installation = models.ManyToManyField(MonitorInstallation, blank=True)
    design_feature = models.ManyToManyField(DesignFeature, blank=True)
    curved_display = models.ForeignKey(CurvedDispaly, on_delete=models.DO_NOTHING, null=True, blank=True)
    response_time = models.ForeignKey(ResponseTime, on_delete=models.DO_NOTHING, null=True, blank=True)
    monitor_matrix = models.ForeignKey(MonitorMatrix, on_delete=models.DO_NOTHING, null=True, blank=True)
    monitor_application = models.ManyToManyField(MonitorApplication, blank=True)
    monitor_connector = models.ManyToManyField(MonitorConnector, blank=True)
    hdr = models.ForeignKey(HDR, on_delete=models.DO_NOTHING, null=True, blank=True)
    #Только краткое название модели, без типа, бренда и характеристик товара. Будет использовано в шаблонизаторе 
    #для составления названия карточки для сайта.
    card_title_model_name = models.ForeignKey(CardTitleModelName, on_delete=models.DO_NOTHING, null=True)#11241
    hdr_standard = models.ManyToManyField(HDRStandard, blank=True)
    key_word = models.ForeignKey(KeyWord, on_delete=models.DO_NOTHING, null=True, blank=True)
    #линейка мобильный устройств
    gadget_serie = models.ForeignKey(GadgetSerie, on_delete=models.SET_NULL, null=True, blank=True)#9225
    #======================dictionary_id > 0==================================================
    video_url = models.URLField(blank=True)
    image_1 = models.URLField(blank=True)
    image_2 = models.URLField(blank=True)
    image_3 = models.URLField(blank=True)
    image_4 = models.URLField(blank=True)
    image_5 = models.URLField(blank=True)

   
    class Meta:
        # ordering = ('created',)  # sorting by date
        verbose_name = 'monitor'
        verbose_name_plural = 'monitors'