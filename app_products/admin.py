from django.contrib import admin
from . models import Smartphone, Monitor, Notebook


# class NotebookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category_name',  'EAN')  
#     list_filter = ('name',)
#     #list_editable= ('processor', 'authentification', )
#     #search_fields = ('imei', )


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

# class TV_SetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category_name',  'EAN')  
#     list_filter = ('name',)
#     #list_editable= ('processor', 'authentification', )
#     #search_fields = ('imei', )

admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Monitor, MonitorAdmin)
# admin.site.register(Notebook, NotebookAdmin)
# admin.site.register(TV_Set, TV_SetAdmin)
