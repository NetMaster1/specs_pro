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
    value = models.CharField(max_length=100, blank=True)
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
    attribute_id = models.CharField(max_length=50, null=True, default="5920")
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
    
class HDMIPorts (models.Model):
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
    attribute_name = models.CharField(max_length=50, default="Макс. частота обнровления, Гц")
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
    value = models.CharField(max_length=100, blank=True)
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
    attribute_id = models.CharField(max_length=50, null=True, default="9048")
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
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class CaseMaterial (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
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

class ProcessorModel (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class ProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
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
    attribute_id = models.CharField(max_length=50, null=True)
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

class VideoProcessorBrand (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=False)
    def __str__(self):
        return self.value

class WifiType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
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
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
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
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=100, blank=True)
    dictionary_value_id = models.CharField(max_length=20, default=0)
    is_required = models.BooleanField(default=False)
    category_dependent = models.BooleanField(default=False)
    is_collection = models.BooleanField(default=True)
    def __str__(self):
        return self.value
    
class MatrixType (models.Model):
    attribute_name = models.CharField(max_length=50, null=True)
    attribute_id = models.CharField(max_length=50, null=True)
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
