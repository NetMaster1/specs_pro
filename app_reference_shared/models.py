from django.db import models

# Create your models here.
class OzonCategory (models.Model):
    type_name = models.CharField(max_length=100, null=True)
    type_id = models.CharField(max_length=50, null=True)
    description_category_id = models.CharField(max_length=80, null=True)
    category_name = models.CharField(max_length=80, null=True)
    group_description_category_id = models.CharField(max_length=80, null=True)
    group_category_name = models.CharField(max_length=80, null=True)
   
    def __str__(self):
        return self.type_name

class SmartphoneVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class ModelName (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class WarrantyPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class PublishingYear (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class RAM (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ESimSupport (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
   
    def __str__(self):
        return self.name

class IOSVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Authentication (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
 
class Stabilization (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ChargingFunction (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class SpecialFeature (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Interface (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    

class CommunicationStandard (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class AndroidVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False) 
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class OperationSystem (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class CaseMaterial (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class WirelessInterface (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ProcessorModel (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class VideoProcessor (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class HazardGrade (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class CameraFunction (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class GadgetSerie (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class VideoProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class WifiType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class SimType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Sensor (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class NavigationType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class BluetoothType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class HardDrive (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class CountryOfManufacture (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class MatrixType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class CardType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    digital_code = models.CharField(max_length=20)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
