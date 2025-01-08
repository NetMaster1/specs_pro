from django.contrib import admin
from . models import Smartphone, Monitor, Notebook, TV, VideoCardProduct


class VideoCardProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    search_fields = ('model_name', )

class TVAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    search_fields = ('model_name', )

class NotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    search_fields = ('model_name', )

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    search_fields = ('model_name', )

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  
    list_filter = ('brand_monitor__value',)
    #list_editable= ('processor', 'authentification', )
    #Для поиска по полю ForeignKey нужно ввести название поля затем двойной пробел и название поля в родительской моделе
    search_fields = ('model_name__value', 'brand_monitor__value' )

admin.site.register(VideoCardProduct, VideoCardProductAdmin)
admin.site.register(TV, TVAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Monitor, MonitorAdmin)

