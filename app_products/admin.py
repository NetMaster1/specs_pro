from django.contrib import admin
from . models import Smartphone, Monitor


# class NotebookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category_name',  'EAN')  
#     list_filter = ('name',)
#     #list_editable= ('processor', 'authentification', )
#     #search_fields = ('imei', )


class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    #search_fields = ('imei', )

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  
    #list_filter = ('name',)
    #list_editable= ('processor', 'authentification', )
    #search_fields = ('imei', )

# class TV_SetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category_name',  'EAN')  
#     list_filter = ('name',)
#     #list_editable= ('processor', 'authentification', )
#     #search_fields = ('imei', )

admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Monitor, MonitorAdmin)
# admin.site.register(Notebook, NotebookAdmin)
# admin.site.register(TV_Set, TV_SetAdmin)
