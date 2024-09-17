from django.contrib import admin
from .models import (SmartphoneVersion, PublishingYear, RAM, ESimSupport, IOSVersion, Authentication, Stabilization, ChargingFunction, SpecialFeature, 
    Interface, AndroidVersion, OperationSystem, CaseMaterial, WirelessInterface, ProcessorModel, ProcessorBrand, VideoProcessor, 
    HazardGrade, CameraFunction, GadgetSerie, VideoProcessorBrand, OzonCategory, HardDrive, CountryOfManufacture, MatrixType, CardType, BluetoothType, 
    NavigationType, Sensor, SimType, WifiType, WarrantyPeriod, ModelName, CommunicationStandard, PartNumber, Size, Weight, ProductSet,
    FrontCamerResolution, BasicCamerResolution, BatteryCapacity, StandByPeriod, WorkPeriod, RecordMaxSpeed, LifeSpan, ScreenSize, SellerCode,
    MarketingColour, ProcessorFrequency)

class OzonCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'type_id', 'category_name', 'description_category_id', 'group_category_name', 'group_description_category_id')
    list_filter = ('type_name',)
    ordering = ('type_name',)
    list_per_page=100
    search_fields = ('type_name', )

class PartNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class BasicCameraResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class BatteryCapacityAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProductSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class FrontCameraResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class WeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class StandByPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class WorkPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class RecordMaxSpeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class LifeSpanAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ScreenSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SellerCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class MarketingColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProcessorFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )


#======================================================
class SmartphoneVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class PublishingYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class RAMAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ESimSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class IOSVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class StabilizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ChargingFunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SpecialFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CommunicationStandardAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class AndroidVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class OperationSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CaseMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class WirelessInterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProcessorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProcessorBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class VideoProcessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class HazardGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CameraFunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class GadgetSerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class VideoProcessorBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required',)  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class WifiTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SimTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class BluetoothTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )
   
class HardDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CountryOfManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class MatrixTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class NavigationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class WarrantyPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

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
admin.site.register(OperationSystem, OperationSystemAdmin)
admin.site.register(AndroidVersion, AndroidVersionAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(SpecialFeature, SpecialFeatureAdmin)
admin.site.register(ChargingFunction, ChargingFunctionAdmin)
admin.site.register(Stabilization, StabilizationAdmin)
admin.site.register(Authentication, AuthenticationAdmin)
admin.site.register(IOSVersion, IOSVersionAdmin)
admin.site.register(ESimSupport, ESimSupportAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(PublishingYear, PublishingYearAdmin)
admin.site.register(SmartphoneVersion, SmartphoneVersionAdmin)
admin.site.register(WarrantyPeriod, WarrantyPeriodAdmin)
admin.site.register(ModelName, ModelNameAdmin)
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