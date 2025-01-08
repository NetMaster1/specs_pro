from django.db import models

class VideoCardStorage(models.Model):
    attribute_name = models.CharField(max_length=50, default='Объем памяти')
    attribute_id = models.CharField(max_length=50, default='5146')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class VideoCardBrand(models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд')
    attribute_id = models.CharField(max_length=50, default='85')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class NumberOfFans(models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество вентиляторов')
    attribute_id = models.CharField(max_length=50, default='5416')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class VideoCardColour(models.Model):
    attribute_name = models.CharField(max_length=50, default='Цвет товара')
    attribute_id = models.CharField(max_length=50, default='10096')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class VideoCardInterface(models.Model):
    attribute_name = models.CharField(max_length=50, default='Интерфейсы')
    attribute_id = models.CharField(max_length=50, default='4526')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class VideoCardStorageType(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип памяти')
    attribute_id = models.CharField(max_length=50, default='22490')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class NumberOfSlots(models.Model):
    attribute_name = models.CharField(max_length=50, default='Кол-во занимаемых слотов')
    attribute_id = models.CharField(max_length=50, default='5153')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TypeVideoCard(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип')
    attribute_id = models.CharField(max_length=50, default='82')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value