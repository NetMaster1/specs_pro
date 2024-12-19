from django.contrib import admin
from .models import (SmartphoneVersion, PublishingYear, RamSmartphone, ESimSupport, IOSVersion, Authentication, Stabilization, ChargingFunction, SpecialFeature, 
    Interface, AndroidVersion, OSMobile, CaseMaterial, WirelessInterface, ProcessorModel, ProcessorBrand, VideoProcessor, 
    HazardGrade, CameraFunction, GadgetSerie, VideoProcessorBrand, OzonCategory, HardDrive, CountryOfManufacture, MatrixType, CardType, BluetoothType, 
    NavigationType, Sensor, SimType, WifiType, WarrantyPeriod, ModelName, CardTitleModelName, CommunicationStandard, PartNumber, Size, Weight, ProductSet,
    FrontCamerResolution, BasicCamerResolution, BatteryCapacity, StandByPeriod, WorkPeriod, RecordMaxSpeed, LifeSpan, ScreenSize, SellerCode,
    MarketingColour, ProcessorFrequency, Name, Description, KeyWord, MaxCardVolume, Json, LightningType, ScreenCoating, HDMIPort, Adjustment,
    PixelSize, Ratio, MaxScreenFrequency, Brightness, Contrast, DynamicContrast, LookAngle, HorizontalFrequency, VerticalFrequency, WebCamera,
    StandAdjustment, PowerCapacity, VESAFixture, PixelPerInch, DesignFeature, ResponseTime, MonitorMatrix, MonitorApplication,
    MonitorConnector, HDRStandard, MonitorInstallation, SpecialFeatureSmartphone,
    )

class OzonCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'activated', 'type_name', 'type_id', 'category_name', 'description_category_id', 'group_category_name', 'group_description_category_id')
    list_filter = ('type_name',)
    ordering = ('type_name',)
    list_per_page=100
    search_fields = ('type_name', )
    list_editable=('activated', )

class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class PartNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BasicCameraResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BatteryCapacityAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ProductSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class FrontCameraResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class StandByPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WorkPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class RecordMaxSpeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class LifeSpanAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ScreenSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SellerCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MarketingColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ProcessorFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )


#======================================================
class SmartphoneVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class PublishingYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class RAMSmartphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ESimSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class IOSVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class StabilizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ChargingFunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SpecialFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SpecialFeatureSmartphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CommunicationStandardAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class AndroidVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class OSMobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CaseMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WirelessInterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ProcessorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ProcessorBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VideoProcessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HazardGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CameraFunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class GadgetSerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VideoProcessorBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WifiTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SimTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BluetoothTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )
   
class HardDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CountryOfManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MatrixTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NavigationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WarrantyPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name',  'value', 'equipment_type', 'equipment_brand', 'dictionary_value_id', 'is_required')  
    list_per_page=100
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', 'equipment_type', 'equipment_brand' )

class CardTitleModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MaxCardVolumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class JsonAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class LightningTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ScreenCoatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HDMIPortAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class AdjustmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class PixelSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class RatioAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MaxScreenFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BrightnessAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ContrastAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class DynamicContrastAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class LookAngleAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HorizontalFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VerticalFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class WebCameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class StandAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class PowerCapacityAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VESAFixtureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class PixelPerInchAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MonitorInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class DesignFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class ResponseTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MonitorMatrixAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MonitorApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MonitorConnectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HDRStandardAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

admin.site.register(VideoProcessorBrand, VideoProcessorBrandAdmin)
admin.site.register(WifiType, WifiTypeAdmin)
admin.site.register(SimType, SimTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(CardType, CardTypeAdmin)
admin.site.register(OzonCategory, OzonCategoryAdmin)
admin.site.register(HardDrive, HardDriveAdmin)
admin.site.register(CountryOfManufacture, CountryOfManufactureAdmin)
admin.site.register(MatrixType, MatrixTypeAdmin)
admin.site.register(BluetoothType, BluetoothTypeAdmin)
admin.site.register(NavigationType, NavigationTypeAdmin)
admin.site.register(GadgetSerie, GadgetSerieAdmin)
admin.site.register(CameraFunction, CameraFunctionAdmin)
admin.site.register(HazardGrade, HazardGradeAdmin)
admin.site.register(VideoProcessor, VideoProcessorAdmin)
admin.site.register(ProcessorBrand, ProcessorBrandAdmin)
admin.site.register(ProcessorModel, ProcessorModelAdmin)
admin.site.register(WirelessInterface, WirelessInterfaceAdmin)
admin.site.register(CaseMaterial, CaseMaterialAdmin)
admin.site.register(OSMobile, OSMobileAdmin)
admin.site.register(AndroidVersion, AndroidVersionAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(SpecialFeature, SpecialFeatureAdmin)
admin.site.register(SpecialFeatureSmartphone, SpecialFeatureSmartphoneAdmin)
admin.site.register(ChargingFunction, ChargingFunctionAdmin)
admin.site.register(Stabilization, StabilizationAdmin)
admin.site.register(Authentication, AuthenticationAdmin)
admin.site.register(IOSVersion, IOSVersionAdmin)
admin.site.register(ESimSupport, ESimSupportAdmin)
admin.site.register(RamSmartphone, RAMSmartphoneAdmin)
admin.site.register(PublishingYear, PublishingYearAdmin)
admin.site.register(SmartphoneVersion, SmartphoneVersionAdmin)
admin.site.register(WarrantyPeriod, WarrantyPeriodAdmin)
admin.site.register(ModelName, ModelNameAdmin)
admin.site.register(CardTitleModelName, CardTitleModelNameAdmin)
admin.site.register(CommunicationStandard, CommunicationStandardAdmin)
admin.site.register(PartNumber, PartNumberAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSet, ProductSetAdmin)
admin.site.register(FrontCamerResolution, FrontCameraResolutionAdmin)
admin.site.register(BasicCamerResolution, BasicCameraResolutionAdmin)
admin.site.register(BatteryCapacity, BatteryCapacityAdmin)
admin.site.register(StandByPeriod, StandByPeriodAdmin)
admin.site.register(WorkPeriod, WorkPeriodAdmin)
admin.site.register(RecordMaxSpeed, RecordMaxSpeedAdmin)
admin.site.register(LifeSpan, LifeSpanAdmin)
admin.site.register(ScreenSize, ScreenSizeAdmin)
admin.site.register(SellerCode, SellerCodeAdmin)
admin.site.register(MarketingColour, MarketingColourAdmin)
admin.site.register(ProcessorFrequency, ProcessorFrequencyAdmin)
admin.site.register(Name, NameAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(MaxCardVolume, MaxCardVolumeAdmin)
admin.site.register(Weight, WeightAdmin)
admin.site.register(Json, JsonAdmin)
admin.site.register(LightningType, LightningTypeAdmin)
admin.site.register(ScreenCoating, ScreenCoatingAdmin)
admin.site.register(HDMIPort, HDMIPortAdmin)
admin.site.register(Adjustment, AdjustmentAdmin)
admin.site.register(PixelSize, PixelSizeAdmin)
admin.site.register(Ratio, RatioAdmin)
admin.site.register(MaxScreenFrequency, MaxScreenFrequencyAdmin)
admin.site.register(Brightness, BrightnessAdmin)
admin.site.register(Contrast, ContrastAdmin)
admin.site.register(DynamicContrast, DynamicContrastAdmin)
admin.site.register(LookAngle, LookAngleAdmin)
admin.site.register(HorizontalFrequency, HorizontalFrequencyAdmin)
admin.site.register(VerticalFrequency, VerticalFrequencyAdmin)
admin.site.register(WebCamera, WebCameraAdmin)
admin.site.register(StandAdjustment, StandAdjustmentAdmin)
admin.site.register(PowerCapacity, PowerCapacityAdmin)
admin.site.register(VESAFixture, VESAFixtureAdmin)
admin.site.register(PixelPerInch, PixelPerInchAdmin)
admin.site.register(MonitorInstallation, MonitorInstallationAdmin)
admin.site.register(DesignFeature, DesignFeatureAdmin)
admin.site.register(ResponseTime, ResponseTimeAdmin)
admin.site.register(MonitorMatrix, MonitorMatrixAdmin)
admin.site.register(MonitorApplication, MonitorApplicationAdmin)
admin.site.register(MonitorConnector, MonitorConnectorAdmin)
admin.site.register(HDRStandard, HDRStandardAdmin)