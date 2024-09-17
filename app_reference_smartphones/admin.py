from django.contrib import admin
from .models import SimCardQnty,Brand, EuroAsianCode, CaseForm, MicroSDSlot, ProcessorCoreQnty, Processor, QntyOfBasicCamera, Colour, ProtectionGrade, GadgetModel, VideoQuality, ScreenResolution, SmartphoneModel, Type

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )
    
class SmartphoneModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )
    
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ScreenResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class VideoQualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class GadgetModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProtectionGradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class QntyOfBasicCameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )
    
class ProcessorCoreQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent') 
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class MicroSDSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')   
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class CaseFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )
   
class EuroAsianCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

class SimCardQntyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'name', 'digital_code', 'is_required', 'category_dependent')  
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page=100
    search_fields = ('name', )

# Register your models here.
admin.site.register(SmartphoneModel, SmartphoneModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(ScreenResolution, ScreenResolutionAdmin)
admin.site.register(VideoQuality, VideoQualityAdmin)
admin.site.register(GadgetModel, GadgetModelAdmin)
admin.site.register(ProtectionGrade, ProtectionGradeAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(QntyOfBasicCamera, QntyOfBasicCameraAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(ProcessorCoreQnty, ProcessorCoreQntyAdmin)
admin.site.register(MicroSDSlot, MicroSDSlotAdmin)
admin.site.register(CaseForm, CaseFormAdmin)
admin.site.register(EuroAsianCode, EuroAsianCodeAdmin)
admin.site.register(SimCardQnty, SimCardQntyAdmin)