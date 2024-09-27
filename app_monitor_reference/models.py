from django.db import models

# Create your models here.

class Resolution (models.Model):
    attribute_name = models.CharField(max_length=50, default='Разрешение')
    attribute_id = models.CharField(max_length=50, default='5592')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TypeMonitor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип')
    attribute_id = models.CharField(max_length=50, default='8229')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class USBPort (models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество USB портов')
    attribute_id = models.CharField(max_length=50, default='5727')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class BuiltinSpeaker (models.Model):
    attribute_name = models.CharField(max_length=50, default='Встроенные динамики')
    attribute_id = models.CharField(max_length=50, default='8992')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class CurvedDispaly (models.Model):
    attribute_name = models.CharField(max_length=50, default='Изогнутый экран')
    attribute_id = models.CharField(max_length=50, default='10760')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class HDR (models.Model):
    attribute_name = models.CharField(max_length=50, default='Технология HDR')
    attribute_id = models.CharField(max_length=50, default='11529')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value