from django.db import models

class CameraResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Разрешение экрана")
    attribute_id = models.CharField(max_length=50, null=True, default='5186')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_collection = models.BooleanField(default=False)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class VideoFileFormat (models.Model):
    attribute_name = models.CharField(max_length=50, default='Форматы файлов видео' )
    attribute_id = models.CharField(max_length=50, default='6078')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_collection = models.BooleanField(default=True)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
    
class CameraSecurityGrade (models.Model):
    attribute_name = models.CharField(max_length=50, default='Степень защиты' )
    attribute_id = models.CharField(max_length=50, default='5269')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_collection = models.BooleanField(default=True)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.value
