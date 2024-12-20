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
    
class RAMExtraSlot (models.Model):
    attribute_name = models.CharField(max_length=50, default='Доп. слоты RAM памяти')
    attribute_id = models.CharField(max_length=50, null=True, default='4448')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class SSDQnty (models.Model):
    attribute_name = models.CharField(max_length=50, default='Количество SSD')
    attribute_id = models.CharField(max_length=50, null=True, default='4451')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VideoRAM (models.Model):
    attribute_name = models.CharField(max_length=50, default='Видеопамять')
    attribute_id = models.CharField(max_length=50, null=True, default='4455')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class KeyboardColour (models.Model):
    attribute_name = models.CharField(max_length=50, default='Цвет клавиатуры')
    attribute_id = models.CharField(max_length=50, null=True, default='4463')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class NotebookCaseMaterial (models.Model):
    attribute_name = models.CharField(max_length=50, default='Материал корпуса')
    attribute_id = models.CharField(max_length=50, null=True, default='4469')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class NotebookInterfacesConnectors (models.Model):
    attribute_name = models.CharField(max_length=50, default='Интерфейсы и разъемы')
    attribute_id = models.CharField(max_length=50, null=True, default='4471')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class BatteryElementQnty (models.Model):
    attribute_name = models.CharField(max_length=50, default='Кол-во элементов аккумулятора')
    attribute_id = models.CharField(max_length=50, null=True, default='4479')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookScreenResolution (models.Model):
    attribute_name = models.CharField(max_length=50, default='Разрешение экрана')
    attribute_id = models.CharField(max_length=50, null=True, default='5186')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class HDDFormFactor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Форм-фактор HDD')
    attribute_id = models.CharField(max_length=50, null=True, default='9141')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class SSDFormFactor (models.Model):
    attribute_name = models.CharField(max_length=50, default='Форм-фактор SSD')
    attribute_id = models.CharField(max_length=50, null=True, default='9142')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class StorageType (models.Model):
    attribute_name = models.CharField(max_length=50, default='Тип накопителя')
    attribute_id = models.CharField(max_length=50, null=True, default='9221')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class VideoCard (models.Model):
    attribute_name = models.CharField(max_length=50, default='Видеокарта')
    attribute_id = models.CharField(max_length=50, null=True, default='9786')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class VRSupport (models.Model):
    attribute_name = models.CharField(max_length=50, default='Поддержка VR')
    attribute_id = models.CharField(max_length=50, null=True, default='9923')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookColour (models.Model):
    attribute_name = models.CharField(max_length=50, default='Цвет товара')
    attribute_id = models.CharField(max_length=50, null=True, default='10096')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class TouchScreen (models.Model):
    attribute_name = models.CharField(max_length=50, default='Сенсорный экран')
    attribute_id = models.CharField(max_length=50, null=True, default='10294')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class NotebookProcessorCoreQnty (models.Model):
    attribute_name = models.CharField(max_length=50, default='Число ядер процессора')
    attribute_id = models.CharField(max_length=50, null=True, default='10318')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class KeyboardLightning (models.Model):
    attribute_name = models.CharField(max_length=50, default='Подсветка клавиатуры')
    attribute_id = models.CharField(max_length=50, null=True, default='10294')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
class MobileCommsModule (models.Model):
    attribute_name = models.CharField(max_length=50, default='Модуль сотовой связи')
    attribute_id = models.CharField(max_length=50, null=True, default='20102')
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=1)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=True)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    
