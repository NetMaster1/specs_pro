from django.db import models

class BrandTV(models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд')
    attribute_id = models.CharField(max_length=50, default='85')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVResolution(models.Model):
    attribute_name = models.CharField(max_length=50, default='Разрешение')
    attribute_id = models.CharField(max_length=50, default='5592')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TypeTV(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип')
    attribute_id = models.CharField(max_length=50, default='8229')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVHDRTechnology(models.Model):
    attribute_name = models.CharField(max_length=50, default='Технология HDR')
    attribute_id = models.CharField(max_length=50, default='11529')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVRAM(models.Model):
    attribute_name = models.CharField(max_length=50, default='Оперативная память')
    attribute_id = models.CharField(max_length=50, default='4443')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVDataStorage(models.Model):
    attribute_name = models.CharField(max_length=50, default='Объем встроенной памяти')
    attribute_id = models.CharField(max_length=50, default='4482')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVUsb(models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество разъемов USB')
    attribute_id = models.CharField(max_length=50, default='5523')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class SmartTV(models.Model):
    attribute_name = models.CharField(max_length=50, default='Smart TV')
    attribute_id = models.CharField(max_length=50, default='9579')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TVColour(models.Model):
    attribute_name = models.CharField(max_length=50, default='Цвет товара')
    attribute_id = models.CharField(max_length=50, default='10096')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class TVCurvedScreen(models.Model):
    attribute_name = models.CharField(max_length=50, default='Изогнутый экран')
    attribute_id = models.CharField(max_length=50, default='10760')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class Subwoofer(models.Model):
    attribute_name = models.CharField(max_length=50, default='Сабвуфер')
    attribute_id = models.CharField(max_length=50, default='11523')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class MediaPlayer(models.Model):
    attribute_name = models.CharField(max_length=50, default='Встроенный медиаплеер')
    attribute_id = models.CharField(max_length=50, default='11526')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class InteriorTVSet(models.Model):
    attribute_name = models.CharField(max_length=50, default='Интерьерный телевизор')
    attribute_id = models.CharField(max_length=50, default='20133')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    

