from django.db import models

# Create your models here.

class Brand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class SmartphoneModel (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Type (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
   
class ScreenResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class VideoQuality (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class GadgetModel (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class ProtectionGrade (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name

class Colour (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class QntyOfBasicCamera (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name

class Processor (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
 
class ProcessorCoreQnty (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)

    def __str__(self):
        return self.name
   
class MicroSDSlot (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class CaseForm (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
    
class EuroAsianCode (models.Model):
    attribute_name = models.TextField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.TextField()
    digital_code = models.CharField(max_length=300)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name
    
class SimCardQnty (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name