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
#========================================================Values========================
class Size (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Размеры, мм')
    attribute_id = models.CharField(max_length=50, null=True, default='4382')
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Weight (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Вес товара, г')
    attribute_id = models.CharField(max_length=50, null=True, default='4383')
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

#I use as EAN
class PartNumber (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Партномер')
    attribute_id = models.CharField(max_length=50, null=True, default="4381")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class ProductSet (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Комплектация')
    attribute_id = models.CharField(max_length=50, null=True, default="4384")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class FrontCamerResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Разрешение фронтальной (селфи) камеры, Мпикс')
    attribute_id = models.CharField(max_length=50, null=True, default="4421")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class BasicCamerResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Разрешение основной камеры, Мпикс')
    attribute_id = models.CharField(max_length=50, null=True, default="4422")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class BatteryCapacity (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Емкость аккумулятора, мАч')
    attribute_id = models.CharField(max_length=50, null=True, default="4429")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class StandByPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Работа в режиме ожидания, ч')
    attribute_id = models.CharField(max_length=50, null=True, default="4439")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class WorkPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Время работы в режиме разговора, ч')
    attribute_id = models.CharField(max_length=50, null=True, default="5786")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class RecordMaxSpeed (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Макс. скорость видеосъемки, кадр/с')
    attribute_id = models.CharField(max_length=50, null=True, default="5920")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class LifeSpan (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Срок службы, лет')
    attribute_id = models.CharField(max_length=50, null=True, default="5920")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class ScreenSize (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Диагональ экрана, дюймы')
    attribute_id = models.CharField(max_length=50, null=True, default="8587")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class SellerCode (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Код продавца')
    attribute_id = models.CharField(max_length=50, null=True, default="9024")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class MarketingColour (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Название цвета')
    attribute_id = models.CharField(max_length=50, null=True, default="10097")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class ProcessorFrequency (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Частота процессора, ГГц')
    attribute_id = models.CharField(max_length=50, null=True, default="10317")
    name = models.CharField(max_length=100, blank=True)
    digital_code = models.CharField(max_length=20, default='0')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    def __str__(self):
        return self.name

#==========================dictionary_value_id > 0==========================================
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
