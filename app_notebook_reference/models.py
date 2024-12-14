from django.db import models

class BrandNotebook(models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд')
    attribute_id = models.CharField(max_length=50, default='85')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class TypeNotebook(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип')
    attribute_id = models.CharField(max_length=50, default='8229')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class HDDQnty(models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество HDD')
    attribute_id = models.CharField(max_length=50, default='4438')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class RAMNotebook(models.Model):
    attribute_name = models.CharField(max_length=50, default='Оперативная память')
    attribute_id = models.CharField(max_length=50, default='4443')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value
    
class NotebookRAMType(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип памяти')
    attribute_id = models.CharField(max_length=50, default='4444')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class NotebookMaxRAM(models.Model):
    attribute_name = models.CharField(max_length=50, default='Возможность расширения RAM, до')
    attribute_id = models.CharField(max_length=50, default='4445')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default='1')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
   
    def __str__(self):
        return self.value