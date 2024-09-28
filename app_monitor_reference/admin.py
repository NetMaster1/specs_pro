from django.contrib import admin
from .models import (Resolution, TypeMonitor, USBPort, BuiltinSpeaker, CurvedDispaly, HDR)

class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class TypeMonitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class USBPortAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class BuiltinSpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class CurverdDisplayAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

class HDRAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_name', 'attribute_id', 'value', 'dictionary_value_id', 'is_required', 'category_dependent')
    list_filter = ('value',)
    ordering = ('value',)
    list_per_page=100
    search_fields = ('value', )

admin.site.register(Resolution, ResolutionAdmin)
admin.site.register(TypeMonitor, TypeMonitorAdmin)
admin.site.register(USBPort, USBPortAdmin)
admin.site.register(BuiltinSpeaker, BuiltinSpeakerAdmin)
admin.site.register(CurvedDispaly, CurverdDisplayAdmin)
admin.site.register(HDR, HDRAdmin)
