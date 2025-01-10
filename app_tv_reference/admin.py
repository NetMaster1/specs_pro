from django.contrib import admin
from .models import (BrandTV,TVResolution,TypeTV,TVHDRTechnology,TVRAM,TVDataStorage,TVUsb,SmartTV,TVColour,TVCurvedScreen,
    Subwoofer,MediaPlayer,InteriorTVSet
    )

class InteriorTVSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class MediaPlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SubwooferAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVCurvedScreenAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class SmartTVAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVUsbAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVDataStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVRAMAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVHDRTechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TypeTVAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TVResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BrandTVAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required')  
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

admin.site.register(InteriorTVSet, InteriorTVSetAdmin)
admin.site.register(MediaPlayer, MediaPlayerAdmin)
admin.site.register(Subwoofer, SubwooferAdmin)
admin.site.register(TVCurvedScreen, TVCurvedScreenAdmin)
admin.site.register(TVColour, TVColourAdmin)
admin.site.register(SmartTV, SmartTVAdmin)
admin.site.register(TVUsb, TVUsbAdmin)
admin.site.register(TVDataStorage, TVDataStorageAdmin)
admin.site.register(TVRAM, TVRAMAdmin)
admin.site.register(TVHDRTechnology, TVHDRTechnologyAdmin)
admin.site.register(TypeTV, TypeTVAdmin)
admin.site.register(TVResolution, TVResolutionAdmin)
admin.site.register(BrandTV, BrandTVAdmin)