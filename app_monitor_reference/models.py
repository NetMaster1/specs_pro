from django.db import models

# Create your models here.

class BrandMonitor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд')
    attribute_id = models.CharField(max_length=50, default='85')
    value = models.CharField(max_length=100, blank=True)
    #default = '1' means that this attribute has a table to choose from
    #default = '0' means that we have to create the model ourselves
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
class Resolution (models.Model):
    attribute_name = models.CharField(max_length=50, default='Разрешение')
    attribute_id = models.CharField(max_length=50, default='5592')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TypeMonitor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип')
    attribute_id = models.CharField(max_length=50, default='8229')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class USBPort (models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество USB портов')
    attribute_id = models.CharField(max_length=50, default='5727')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class BuiltinSpeaker (models.Model):
    attribute_name = models.CharField(max_length=50, default='Встроенные динамики')
    attribute_id = models.CharField(max_length=50, default='8992')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class CurvedDispaly (models.Model):
    attribute_name = models.CharField(max_length=50, default='Изогнутый экран')
    attribute_id = models.CharField(max_length=50, default='10760')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class HDR (models.Model):
    attribute_name = models.CharField(max_length=50, default='Технология HDR')
    attribute_id = models.CharField(max_length=50, default='11529')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class ColourMonitor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Цвет товара')
    attribute_id = models.CharField(max_length=50, default='10096')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class EuroAsianCodeMonitor (models.Model):
    attribute_name = models.CharField(max_length=50, default='ТН ВЭД коды ЕАЭС')
    attribute_id = models.CharField(max_length=50, default='22232')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value