from django.db import models

# Create your models here.
class OzonCategory (models.Model):
    activated = models.BooleanField(default=False)
    type_name = models.CharField(max_length=100, null=True)
    type_id = models.CharField(max_length=50, null=True)
    description_category_id = models.CharField(max_length=80, null=True)
    category_name = models.CharField(max_length=80, null=True)
    group_description_category_id = models.CharField(max_length=80, null=True)
    group_category_name = models.CharField(max_length=80, null=True)
    
    def __str__(self):
        return self.type_name

class ProcessorModelNotebook (models.Model):
    attribute_name = models.CharField(max_length=50, default='Модель процессора' )
    attribute_id = models.CharField(max_length=50, default='10316')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class PortQntyUSB (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов USB 2.0')
    attribute_id = models.CharField(max_length=50, null=True, default='4416')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class PowerOffWorkTime (models.Model):
    attribute_name = models.CharField(max_length=50, default='Время автономной работы, ч')
    attribute_id = models.CharField(max_length=50, null=True, default='4428')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class PortQntyUSB3Gen1 (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов USB Type-A  3.2 Gen 1')
    attribute_id = models.CharField(max_length=50, null=True, default='4432')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookFormFactor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Форм-фактор ноутбука')
    attribute_id = models.CharField(max_length=50, null=True, default='4441')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Chipset (models.Model):
    attribute_name = models.CharField(max_length=50, default='Чипсет')
    attribute_id = models.CharField(max_length=50, null=True, default='4442')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class PortQntyUSB3Gen2 (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов USB Type-A 3.2 Gen 2')
    attribute_id = models.CharField(max_length=50, null=True, default='4446')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class RAMFormFactor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Форм-фактор RAM')
    attribute_id = models.CharField(max_length=50, null=True, default='4447')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class DVDrive (models.Model):
    attribute_name = models.CharField(max_length=50, default='Оптический привод')
    attribute_id = models.CharField(max_length=50, null=True, default='4452')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VideoCardType (models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип видеокарты')
    attribute_id = models.CharField(max_length=50, null=True, default='4454')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class SoundConfig (models.Model):
    attribute_name = models.CharField(max_length=50, default='Конфигурация звука')
    attribute_id = models.CharField(max_length=50, null=True, default='4459')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class ManualInputDevice (models.Model):
    attribute_name = models.CharField(max_length=50, default='Устройства ручного ввода')
    attribute_id = models.CharField(max_length=50, null=True, default='4461')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class ManualInputDeviceFeature (models.Model):
    attribute_name = models.CharField(max_length=50, default='Особенности устройств ручного ввода')
    attribute_id = models.CharField(max_length=50, null=True, default='4462')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class LANCard (models.Model):
    attribute_name = models.CharField(max_length=50, default='Сетевая карта')
    attribute_id = models.CharField(max_length=50, null=True, default='4466')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class WebCamResolution (models.Model):
    attribute_name = models.CharField(max_length=50, default='Разрешение Web-камеры')
    attribute_id = models.CharField(max_length=50, null=True, default='4468')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class PortQntyThunderbolt (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов Thunderbolt')
    attribute_id = models.CharField(max_length=50, null=True, default='4473')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class DisplayPort (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов DisplayPort')
    attribute_id = models.CharField(max_length=50, null=True, default='4475')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
       
class PowerSupplyVoltage (models.Model):
    attribute_name = models.CharField(max_length=50, default='Напряжение адаптера питания')
    attribute_id = models.CharField(max_length=50, null=True, default='4481')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    

class NotebookWeight (models.Model):
    attribute_name = models.CharField(max_length=50, default='Вес, кг')
    attribute_id = models.CharField(max_length=50, null=True, default='5825')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class TotalDiskVolume (models.Model):
    attribute_name = models.CharField(max_length=50, default='Суммарный объем всех дисков, ГБ')
    attribute_id = models.CharField(max_length=50, null=True, default='6079')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class TotalHDDVolume (models.Model):
    attribute_name = models.CharField(max_length=50, default='Общий объем HDD, ГБ')
    attribute_id = models.CharField(max_length=50, null=True, default='8574')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class TotalSSDVolume (models.Model):
    attribute_name = models.CharField(max_length=50, default='Общий объем SSD, ГБ')
    attribute_id = models.CharField(max_length=50, null=True, default='8575')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class PortQntyTypeC (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число портов USB Type-C')
    attribute_id = models.CharField(max_length=50, null=True, default='9140')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookProcessor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Процессор')
    attribute_id = models.CharField(max_length=50, null=True, default='9785')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class BatteryType(models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип аккумулятора')
    attribute_id = models.CharField(max_length=50, null=True, default='4480')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class BuiltInDevice (models.Model):
    attribute_name = models.CharField(max_length=50, default='Встроенные устройства')
    attribute_id = models.CharField(max_length=50, null=True, default='4467')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class CardReader (models.Model):
    attribute_name = models.CharField(max_length=50, default='Картридер')
    attribute_id = models.CharField(max_length=50, null=True, default='5580')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class CaseCoating (models.Model):
    attribute_name = models.CharField(max_length=50, default='Покрытие корпуса')
    attribute_id = models.CharField(max_length=50, null=True, default='4470')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class Configuration (models.Model):
    attribute_name = models.CharField(max_length=50, default='Конфигурация')
    attribute_id = models.CharField(max_length=50, null=True, default='9511')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='11362')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookVideoProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, default='Бренд процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='11363')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class OperationSystem (models.Model):
    attribute_name = models.CharField(max_length=50, default='Операционная система')
    attribute_id = models.CharField(max_length=50, null=True, default='11377')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VideoProcessorFamily (models.Model):
    attribute_name = models.CharField(max_length=50, default='Серия графического процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='11379')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookMatrixType (models.Model):
    attribute_name = models.CharField(max_length=50, default='Технология матрицы')
    attribute_id = models.CharField(max_length=50, null=True, default='11380')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class WindowsVersion (models.Model):
    attribute_name = models.CharField(max_length=50, default='Версия Windows')
    attribute_id = models.CharField(max_length=50, null=True, default='12454')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MacOSVersion (models.Model):
    attribute_name = models.CharField(max_length=50, default='Версия MacOS')
    attribute_id = models.CharField(max_length=50, null=True, default='12455')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class KeyboardLayout (models.Model):
    attribute_name = models.CharField(max_length=50, default='Раскладка клавиатуры')
    attribute_id = models.CharField(max_length=50, null=True, default='21988')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class WebCamShutter (models.Model):
    attribute_name = models.CharField(max_length=50, default='Шторка для веб-камеры')
    attribute_id = models.CharField(max_length=50, null=True, default='22288')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookBatteryCapacity (models.Model):
    attribute_name = models.CharField(max_length=50, default='Емкость аккумулятора, Втч')
    attribute_id = models.CharField(max_length=50, null=True, default='23007')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#========================================================Values========================
class Size (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Размеры, мм')
    attribute_id = models.CharField(max_length=50, null=True, default='4382')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Weight (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Вес товара, г')
    attribute_id = models.CharField(max_length=50, null=True, default='4383')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#I use as EAN
class PartNumber (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Партномер')
    attribute_id = models.CharField(max_length=50, null=True, default="4381")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=True)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class ProductSet (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Комплектация')
    attribute_id = models.CharField(max_length=50, null=True, default="4384")
    value = models.CharField(max_length=250, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class FrontCamerResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Разрешение фронтальной (селфи) камеры, Мпикс')
    attribute_id = models.CharField(max_length=50, null=True, default="4421")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class BasicCamerResolution (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Разрешение основной камеры, Мпикс')
    attribute_id = models.CharField(max_length=50, null=True, default="4422")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#Smartphone
class BatteryCapacity (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Емкость аккумулятора, мАч')
    attribute_id = models.CharField(max_length=50, null=True, default="4429")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class StandByPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Работа в режиме ожидания, ч')
    attribute_id = models.CharField(max_length=50, null=True, default="4439")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class WorkPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Время работы в режиме разговора, ч')
    attribute_id = models.CharField(max_length=50, null=True, default="5786")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class RecordMaxSpeed (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Макс. скорость видеосъемки, кадр/с')
    attribute_id = models.CharField(max_length=50, null=True, default="5920")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class LifeSpan (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Срок службы, лет')
    attribute_id = models.CharField(max_length=50, null=True, default="6036")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class ScreenSize (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Диагональ экрана, дюймы')
    attribute_id = models.CharField(max_length=50, null=True, default="8587")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class SellerCode (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Код продавца')
    attribute_id = models.CharField(max_length=50, null=True, default="9024")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MarketingColour (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Название цвета')
    attribute_id = models.CharField(max_length=50, null=True, default="10097")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)

    def __str__(self):
        return self.value
    
class ProcessorFrequency (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Частота процессора, ГГц')
    attribute_id = models.CharField(max_length=50, null=True, default="10317")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Name (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Название")
    attribute_id = models.CharField(max_length=50, null=True, default="4180")
    value = models.CharField(max_length=75, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#text for seo
class Description (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Аннотация")
    attribute_id = models.CharField(max_length=50, null=True, default="4191")
    value = models.TextField(null=True, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class KeyWord (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Ключевые слова")
    attribute_id = models.CharField(max_length=50, null=True, default="22336")
    value = models.CharField(max_length=500, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MaxCardVolume (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Макс. объём карты памятиб ГБ")
    attribute_id = models.CharField(max_length=50, null=True, default="4412")
    value = models.CharField(max_length=500, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Json (models.Model):
    attribute_name = models.CharField(max_length=100, null=True, default="Rich-контент JSON")
    attribute_id = models.CharField(max_length=50, null=True, default="11254")
    value = models.TextField(blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
       

#==========================dictionary_value_id > 0==========================================
class SmartphoneVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Версия смартфона')
    attribute_id = models.CharField(max_length=50, null=True, default='22975')
    value = models.CharField(max_length=100, null=True, default='Ростест (ЕАС)')
    dictionary_value_id = models.CharField(max_length=20, null=True, default='971992309')
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#used to unite different items in one card   
class ModelName (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Название модели (для объединения в одну карточку)")
    attribute_id = models.CharField(max_length=50, null=True, default='9048')
    value = models.CharField(max_length=50, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    equipment_type = models.CharField(max_length=50, null=True, blank=True)
    equipment_brand = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.value
    
class CardTitleModelName (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Название модели для шаблона наименования")
    attribute_id = models.CharField(max_length=50, null=True, default='12141')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
#==================================Monitor Section============================ 
class LightningType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Тип подсветки")
    attribute_id = models.CharField(max_length=50, null=True, default='4457')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class ScreenCoating (models.Model):
    attribute_name = models.CharField(max_length=50, default="Покрытие экрана")
    attribute_id = models.CharField(max_length=50, default='4458')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class HDMIPort (models.Model):
    attribute_name = models.CharField(max_length=50, default="Число портов HDMI")
    attribute_id = models.CharField(max_length=50, default='4474')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Adjustment (models.Model):
    attribute_name = models.CharField(max_length=50, default="Регулировки")
    attribute_id = models.CharField(max_length=50, default='5482')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class PixelSize (models.Model):
    attribute_name = models.CharField(max_length=50, default="Размер пикселя, мм")
    attribute_id = models.CharField(max_length=50, default='5559')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Ratio (models.Model):
    attribute_name = models.CharField(max_length=50, default="Соотношение сторон")
    attribute_id = models.CharField(max_length=50, default='5568')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MaxScreenFrequency (models.Model):
    attribute_name = models.CharField(max_length=50, default="Макс. частота обновления, Гц")
    attribute_id = models.CharField(max_length=50, default='5570')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Brightness (models.Model):
    attribute_name = models.CharField(max_length=50, default="Яркость, кд/м2")
    attribute_id = models.CharField(max_length=50, default='5571')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class Contrast (models.Model):
    attribute_name = models.CharField(max_length=50, default="Контрастность")
    attribute_id = models.CharField(max_length=50, default='5572')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class DynamicContrast (models.Model):
    attribute_name = models.CharField(max_length=50, default="Динамическая контрастность")
    attribute_id = models.CharField(max_length=50, default='5573')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class LookAngle (models.Model):
    attribute_name = models.CharField(max_length=50, default="Углы обзораб (Г/В)")
    attribute_id = models.CharField(max_length=50, default='5574')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class HorizontalFrequency (models.Model):
    attribute_name = models.CharField(max_length=50, default="Частота горизонтальной развертки, кГц")
    attribute_id = models.CharField(max_length=50, default='5575')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VerticalFrequency (models.Model):
    attribute_name = models.CharField(max_length=50, default="Частота вертикальной развертки, Гц")
    attribute_id = models.CharField(max_length=50, default='5576')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class WebCamera (models.Model):
    attribute_name = models.CharField(max_length=50, default="Записываются характеристики web-камеры")
    attribute_id = models.CharField(max_length=50, default='5579')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class StandAdjustment (models.Model):
    attribute_name = models.CharField(max_length=50, default="Уровни регулировки подставки")
    attribute_id = models.CharField(max_length=50, default='5582')
    value = models.CharField(max_length=250, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class PowerCapacity (models.Model):
    attribute_name = models.CharField(max_length=50, default="Потребляемая мощность")
    attribute_id = models.CharField(max_length=50, default='5583')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VESAFixture (models.Model):
    attribute_name = models.CharField(max_length=50, default="Стандарт крепления VESA")
    attribute_id = models.CharField(max_length=50, default='5758')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class PixelPerInch (models.Model):
    attribute_name = models.CharField(max_length=50, default="Плотность пикселей, ppi")
    attribute_id = models.CharField(max_length=50, default='5758')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MonitorInstallation (models.Model):
    attribute_name = models.CharField(max_length=50, default="Установка монитора")
    attribute_id = models.CharField(max_length=50, default='10758')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class DesignFeature (models.Model):
    attribute_name = models.CharField(max_length=50, default="Конструктивные особенности")
    attribute_id = models.CharField(max_length=50, default='10759')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class ResponseTime (models.Model):
    attribute_name = models.CharField(max_length=50, default="Время отклика")
    attribute_id = models.CharField(max_length=50, default='10761')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MonitorMatrix (models.Model):
    attribute_name = models.CharField(max_length=50, default="Матрица монитора")
    attribute_id = models.CharField(max_length=50, default='11510')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MonitorApplication (models.Model):
    attribute_name = models.CharField(max_length=50, default="Назначение монитора")
    attribute_id = models.CharField(max_length=50, default='11511')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class MonitorConnector (models.Model):
    attribute_name = models.CharField(max_length=50, default="Разъёмы монитора")
    attribute_id = models.CharField(max_length=50, default='11515')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
        
class HDRStandard (models.Model):
    attribute_name = models.CharField(max_length=50, default="Стандарты HDR")
    attribute_id = models.CharField(max_length=50, default='21031')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
#======================================End of Monitor Section====================================

#used to create card title   
# class ModelName (models.Model):
#     attribute_name = models.CharField(max_length=50, null=True, default="Название модели для шаблона наименования")
#     attribute_id = models.CharField(max_length=50, null=True, default='12141')
#     value = models.CharField(max_length=100, blank=True)
#     dictionary_value_id = models.CharField(max_length=20, default=0)
#     is_required = models.BooleanField(default=False)
#     category_dependent = models.BooleanField(default=False)
#     is_collection = models.BooleanField(default=False)
#     def __str__(self):
#         return self.value


class WarrantyPeriod (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Гарантийный срок")
    attribute_id = models.CharField(max_length=50, null=True, default="4385")
    value = models.CharField(max_length=100, null=True, default="1 год с момента покупки")
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class PublishingYear (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class RamSmartphone (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class ESimSupport (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
   
    def __str__(self):
        return self.value

class IOSVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class Authentication (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
 
class Stabilization (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class ChargingFunction (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class SpecialFeature (models.Model):
    attribute_name = models.CharField(max_length=50, null=True,default="Особенности" )
    attribute_id = models.CharField(max_length=50, null=True,default="5584" )
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class SpecialFeatureSmartphone (models.Model):
    attribute_name = models.CharField(max_length=50, null=True,default="Особенности" )
    attribute_id = models.CharField(max_length=50, null=True,default="11449" )
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class Interface (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class CommunicationStandard (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class AndroidVersion (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False) 
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class OSMobile (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Операционная система')
    attribute_id = models.CharField(max_length=50, null=True, default='10889')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class CaseMaterial (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Основной материал корпуса')
    attribute_id = models.CharField(max_length=50, null=True, default='10746')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class WirelessInterface (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

#Smartphone
class ProcessorModel (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Модель процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='10320')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#Smartphone
class ProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Бренд процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='10315')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class VideoProcessor (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class HazardGrade (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True, default="9782")
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class CameraFunction (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class GadgetSerie (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

#Smartphone
class VideoProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Бренд графического процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='5142')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class WifiType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Модуль связи WiFi')
    attribute_id = models.CharField(max_length=50, null=True, default='4465')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class SimType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class Sensor (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    
    def __str__(self):
        return self.value

class NavigationType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value

class BluetoothType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Модуль связи Bluetooth')
    attribute_id = models.CharField(max_length=50, null=True, default='4414')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class HardDrive (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class CountryOfManufacture (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default='Страна-изготовитель')
    attribute_id = models.CharField(max_length=50, null=True, default='4389')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class MatrixType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True, default="Технология матрицы")
    attribute_id = models.CharField(max_length=50, null=True, default='4406')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class CardType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
