from django.contrib import admin
from .models import (BrandNotebook, TypeNotebook, HDDQnty, RAMNotebook, NotebookRAMType, NotebookMaxRAM, RAMExtraSlot, SSDQnty, VideoRAM, 
    KeyboardColour, NotebookCaseMaterial, NotebookInterfacesConnector, BatteryElementQnty, NotebookScreenResolution, HDDFormFactor, 
    SSDFormFactor, StorageType, VideoCard, VRSupport, NotebookColour, TouchScreen, NotebookProcessorCoreQnty, KeyboardLightning, 
    MobileCommsModule, 
    )

class BrandNotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TypeNotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HDDQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class RAMNotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookRAMTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookMaxRAMAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class RAMExtraSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SSDQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VideoRAMAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class KeyboardColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookCaseMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookInterfacesConnectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BatteryElementQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookScreenResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HDDFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SSDFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class StorageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VideoCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class VRSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TouchScreenAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class NotebookProcessorCoreQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class KeyboardLightningAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MobileCommsModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

admin.site.register(BrandNotebook, BrandNotebookAdmin)
admin.site.register(TypeNotebook, TypeNotebookAdmin)
admin.site.register(HDDQnty, HDDQntyAdmin)
admin.site.register(RAMNotebook, RAMNotebookAdmin)
admin.site.register(NotebookRAMType, NotebookRAMTypeAdmin)
admin.site.register(NotebookMaxRAM, NotebookMaxRAMAdmin)
admin.site.register(RAMExtraSlot, RAMExtraSlotAdmin)
admin.site.register(SSDQnty, SSDQntyAdmin)
admin.site.register(VideoRAM, VideoRAMAdmin)
admin.site.register(KeyboardColour, KeyboardColourAdmin)
admin.site.register(NotebookCaseMaterial, NotebookCaseMaterialAdmin)
admin.site.register(NotebookInterfacesConnector, NotebookInterfacesConnectorAdmin)
admin.site.register(BatteryElementQnty, BatteryElementQntyAdmin)
admin.site.register(NotebookScreenResolution, NotebookScreenResolutionAdmin)
admin.site.register(HDDFormFactor, HDDFormFactorAdmin)
admin.site.register(SSDFormFactor, SSDFormFactorAdmin)
admin.site.register(StorageType, StorageTypeAdmin)
admin.site.register(VideoCard, VideoCardAdmin)
admin.site.register(VRSupport, VRSupportAdmin)
admin.site.register(NotebookColour, NotebookColourAdmin)
admin.site.register(TouchScreen, TouchScreenAdmin)
admin.site.register(NotebookProcessorCoreQnty, NotebookProcessorCoreQntyAdmin)
admin.site.register(KeyboardLightning, KeyboardLightningAdmin)
admin.site.register(MobileCommsModule, MobileCommsModuleAdmin)