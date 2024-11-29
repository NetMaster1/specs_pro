from django.shortcuts import render
from django.http import request
import time
import requests
import bs4
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from app_products.models import Smartphone, Monitor
from app_monitor_reference.models import (Brand_Monitor, ColourMonitor,Resolution, TypeMonitor, USBPort, BuiltinSpeaker, CurvedDispaly, HDR,
    EuroAsianCodeMonitor                                      
    )
from app_reference_shared.models import (OzonCategory,LightningType, Size, MonitorConnector, ScreenSize, WarrantyPeriod, ScreenCoating, HDMIPorts,
    Adjustment, PixelSize, Ratio, MaxScreenFrequency, Brightness, Contrast, DynamicContrast, LookAngle, HorizontalFrequency, 
    VerticalFrequency, WebCamera, StandAdjustment, PowerCapacity, SpecialFeature, DesignFeature, VESAFixture, PixelPerInch, MonitorInstallation,
    ResponseTime, MonitorMatrix, MonitorApplication, HDRStandard, Description, ProductSet, CountryOfManufacture, WorkPeriod, Weight, KeyWord,
    PartNumber, Name, ModelName, LifeSpan
    )
import datetime
import re
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options as ChromeOptions

#from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains

import undetected_chromedriver as uc

#эти импорты нужны нам для организации механизма ожидания формирования страницы
#для последующего получения html из нее
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_down(driver, deep):
    for _ in range(deep):
        driver.execute_script('window.scrollBy(0, 1500)')
        time.sleep(0.05)

def create_smartphone(request):
    headers={'User-Agent': UserAgent().chrome}
    url = 'https://nn.shop.megafon.ru/mobile/182129'
    megafon_response=requests.get(url, headers=headers)
    print(megafon_response.status_code)
    soupMEG=BeautifulSoup(megafon_response.content, "html.parser")
    key=soupMEG.find_all("div", {"class":"b-good-specs__head"})
    value=soupMEG.find_all("div", {"class":"b-good-specs__content"})
    specs={}
    for i, j in zip (key, value):   
        a=str(i.text)
        a=' '.join(a.split())#удаляем лишние пробелы
        a=a.rstrip("\n")#удаляем символ каретки'\n'
        head, sep, tail = a.partition(':')#удаляем часть строки после символа ":"
        b=str(j.text)
        b=' '.join(b.split())#удаляем лишние пробелы
        b=b.rstrip("\n")#удаляем символ каретки '\n'
        specs[head]=b#Добавляем пару (ключ : значение) в словарь
    for keys, values in specs.items():
        print(keys + ' : ' + values)

    # key=soupMEG.find_all("div", {"class":"b-good-specs__head"})
    # value=soupMEG.find_all("div", {"class":"b-good-specs__content"})
    # specs={}
    # for i, j in zip (key, value):   
    #     a=str(i.text)
    #     a=' '.join(a.split())#удаляем лишние пробелы
    #     a=a.rstrip("\n")#удаляем символ каретки'\n'
    #     head, sep, tail = a.partition(':')#удаляем часть строки после символа ":"
    #     b=str(j.text)
    #     b=' '.join(b.split())#удаляем лишние пробелы
    #     b=b.rstrip("\n")#удаляем символ каретки '\n'
    #     specs[head]=b#Добавляем пару (ключ : значение) в словарь
    # for keys, values in specs.items():
    #     print(keys + ' : ' + values)

def model_test(request):
    item_list={
        # "brand_monitor": "Бренд",
        # "resolution": "Разрешение",
        "screen_size": "Диагональ экрана, дюймы",
        "monitor_matrix": "Матрица монитора",
        "max_screen_frq": "Макс. частота обновления, Гц",
        "monitor_application": "Назначение монитора",
        "special_feature": "Особенности",
        "design_feature": "Конструктивные особенности",
        "power_capacity": "Потребляемая мощность, Вт",
        "curved_display": "Изогнутый экран",
        "brightness": "Яркость, кд/м2",
        "ratio": "Соотношение сторон",
        "screen_coating": "Покрытие экрана",
        "response_time": "Время отклика, мс",
        "dynamic_contrast" : "Динамическая контрастность",
        "contrast": "Контрастность",
        "look_angle": "Углы обзора (Г/В)",
        "hdr": "Технология HDR",
        "hdmi_ports": "Число портов HDMI",
        "hdr_standard": "Cтандарты HDR",
        "monitor_connector": "Разъёмы монитора",
        "vesa_fixture": "Стандарт крепления VESA",
        "adjustments": "Регулировки",
        "size": "Размеры, мм",
        "weight": "Вес, кг",
        "web_camera": "Web-камера",
        "builtin_speaker": "Встроенные динамики",
        "warranty_period": "Гарантийный срок",
        "country_of_manufacture": "Страна-изготовитель",
        "colour_monitor": "Цвет товара",
        "monitor_installation": "Установка монитора",
        "product_set":  "Комплектация",
        "lighting_type": "Тип подсветки",
        "pixel_size": "Размер пикселя, мм",
        "pixel_per_inch": "РПлотность пикселей, ppi",
        "horizontal_frequency": "Частота горизонтальной развертки, кГц",
        "vertical_frequency": "Частота вертикальной развертки, Гц",
        "stand_adjustment": "Уровни регулировки подставки",
        "usb_port": "Количество USB портов",
        "life_span": "Срок службы, лет",
    }

    model_name='x LF24T450FZIXCI'
    model_name=ModelName.objects.get(value=model_name)
    object=Monitor.objects.get(model_name=model_name)
    print('+++++++++++++++++++++++++++++++++++++')
    print(object.id)
    print(type(object))
    # for i in object.fields:
    #     print(i)
    all_fields = Monitor._meta.get_fields()
    #all_fields = object._meta.get_fields()
    #for i in all_fields:
    item=object.warranty_period.value
    print(item)
    print('+++++++++++++++++++++++++++++++++++++')
  
    for i in all_fields:
        #print(i.name)
        #f i.name != 'id' :

        #     if len(i) < 1:
        #if object.i.name is None:
        #if not i:

            #if object.get_field(i).value__isnull==True:
            #if object(i.value__isnull==True):
            #if object(i.value__isblank==True):
        #if object:
        #if object(i.related_model.value__isnull==True):
        #if object(i.value == None):
        if object(i == None):
            # if i.name__isnull == True:
            # if i__isnull == True:
            # if Monitor.objects.filter(i__isnull==True):
            #     print('ok')
            #     string=i.related_model.create(
            string=str(i.related_model)
            # print(string)
            string=string.split('.')
            if len(string) > 2:
                string=string[2]
                string=string.split("'")
                print(string[0])
        print('===================================')


    # for i in all_fields:
        #print(i.name)
        #print(i.model.name)
        #print(i.model)
    #table=Monitor._meta.getattribute('special_feature')
    # for i in all_fields:
    #     if i.value__isnull == True:
    #         item=item_list[i]
    #         try:
    #           f = Monitor._meta.get_field(i)
    #             usb_port=USBPort.objects.get(value=specs[item])
    #             monitor.usb_port=usb_port
    #         except:
    #             pass

def selenium_search_ozon_monitor(request):
    #driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.proxy = Proxy({ 'proxyType': ProxyType.MANUAL, 'httpProxy' : 'http.proxy:1234'})
    driver = webdriver.Chrome(options=options)
    
    #driver = webdriver.Firefox()
    #url="https://www.ozon.ru/category/monitory-15738/benq-26303024/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=brand&text=%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80"
    url="https://www.ozon.ru/category/monitory-15738/benq-26303024/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=brand&text=монитор"
    #url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=34.000%3B34.000&text=монитор"
    #url="https://www.ozon.ru/product/samsung-27-monitor-essential-monitor-ls27c310eaixci-chernyy-1646295308/features/"
    #url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=22.000%3B22.000&text=%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80"
    driver.get(url)
    #драйвер заходит на сайт со своими cookies. А сервер присваивает браузеру свои cookies, чтобы отличить его от бота.
    #Соответственно заходим на сайт в браузере Chrome, так как мы используем драйвер Chrome. Смотрим cookies Application/Storage/Cookies для браузера
    #Chrome. Обычно их 12 на ozon. Удаляем текущие cookie драйвера. Cookies для разных браузеров отличаются.
    #Присваиваем драйверу cookies браузера. 
    #заходим драйвером еще раз (для этого ничего делать не надо, драйвер сам изменится)
    # delete one cookie
    #driver.delete_cookie(cookie)    
    
    driver.delete_all_cookies
    cookies = [
        {
            "name": "ADDRESSBOOKBAR_WEB_CLARIFICATION",
            "value": "1731874909",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS013595b9",
            "value": "0187c00a18fb3344b2ddd225f8c59f01cd6f7d24bfc48e6dabcd02cfdeab840943dccfabdc6072c26a6fc1227d0d5b0f8f4c9fca16",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS013595b9",
            "value": "0187c00a18cabfeb2595eee7115f5ba7286551b75cfdad2732fbb0b4e7112c104e5b682f8220da7111ff732d1b4a058da2eaf9d437",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS015d2969",
            "value": "0187c00a18fb3344b2ddd225f8c59f01cd6f7d24bfc48e6dabcd02cfdeab840943dccfabdc6072c26a6fc1227d0d5b0f8f4c9fca16",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-ETC",
            "value": "5cd2f49f8837aee4e3d309804b978e68",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-ab-group",
            "value": "12",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-access-token",
            "value": "6.0.7EA6zUt4QnCv11NscAmcqw.12.AX9v8rYngc181zQoYyeV9FBuv9dRqcC41BAe4ZP8oA3d1vltKmfdvbiTuwcu68XCpA..20241117222147.1yoYwHJznF1LGShMvS2E6HF5sG_Wv6pxTTVpvMwwcj0.1265055a388a94db9",
            "domain": ".ozon.ru"
        },
        {
            "name": "__Secure-ext_xcid",
            "value": "eb6a2a001d00fdbfca04736ee64baef7",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-refresh-token",
            "value": "6.0.7EA6zUt4QnCv11NscAmcqw.12.AX9v8rYngc181zQoYyeV9FBuv9dRqcC41BAe4ZP8oA3d1vltKmfdvbiTuwcu68XCpA..20241117222147.MgtnpB2-Sze2IktVVXlQbpThxzH0xkWiCroP2tmYjWg.1c56b836a6692f83e",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-user-id",
            "value": "0",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.wvXWcaOplGpljUx0uKd5nHmDy5F3-yjT74mVwVwL2h5H0biBWosz0OOYTTVejux1ErOfBO7I88az-gNNdxxAKU7ufYOozpGwAIH3gnVa1k8YvYoLPR8w8YEz49vIdWVKyaNCL3LFksPbqsxxAjFqduRH5VFUXYaEZj4CZ2S80U17Dk__qCcMO887d7_iRo3eQHNwVz7q5ojiHky4sOtImmfHEhrwkLrwPuX4szmaG3eVPQOuH41jn7sHRCbUIQ1-pei64KWHOZi8xB_zQwQqMW2ls8B-75EwXP_0w5CmZr5T_7eYwEVXRJOtYQJD12mvRhywelBpgsq8JbOQ_WBm9ZMD5en9ztogyOLF7wScOc6mRlHhPBRRQtZMWRRmYZjFK4z-03LJ8gEkGbW5w4BTnCp1ZVhouhBY8aqGTWOwHDTY6Q0v8fIe5EedmUkUhG8ANp4DKayNog",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.5u6wADY-Mw_Kkwo459T4KAvZUCSEC55V0EE-u_bm4O6vu--HLgMnyUu0gpZeCLvuviAAQpJm7SEflFjdaLU9Wc1rZoBMlGtq8Gti4mbKY19F1o3h47Uedln-9TU5LIheG69LOnth__B7SCzo_s6mDlu3PyK2Uv0VybAItt5zqQ39WjZvK0Twntsby8OOBrQNc-PcNHPotVDdStbdNkxrs4kMxFpoNsei3Pehsok-4eNPCmr03x1KAoFlmeAs8Y_gb7B1WNJUS6eK4s3ZzlWvyx2qu24gAh9o8nO59Z8bGXGhetzO8I6vRS1v2pIjXcJa3pxoZ-F7XcZ6vFWRORWGiDNOA2uXvNT66DwI",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.PEetYJxJQQoGRnu376Lz1uW601-WIJLEIHvq6kLN8Co7LZZn67zXaf-r9hZaPrWp4gg_sfnd3LdkFDhifzlQfBl6We0z3lSSC4YV5G3TGdO_vJ0rtWKN-fJDENppAUQnfij-g9gTZBOl5jgXXJBV37e0co4DA_63EvsO0eAq58QD6hb58dW_1l_e90Ddiq7jX_FGiFs-WHae_kb7Fgch5JtRVxrtWuD2Wk1i6s1zaxGrHNXySfeXl3vFO01tZXbV6cdqKSLhvU-ZFSb4ek8GZSgsMbqIryV-nD1gMsKfzTF9o1nvrof_K647zm6AJkS6N64cL1LuDYka29bwxZnZwX-EDDMd6llbBlwEovFeD5L3pO7u_Bg",
            "domain": ".ozon.ru" 
        }, 
        {
            "name": "is_cookies_accepted",
            "value": "1",
            "domain": "www.ozon.ru" 
        },
        {
            "name": "rfuid",
            "value": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxMDQ0MjEyNTc2LC0xLC01NTczNTY4MSxXM3NpYm1GdFpTSTZJbEJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFsSUZCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxcGRXMGdVRVJHSUZacFpYZGxjaUlzSW1SbGMyTnlhWEIwYVc5dUlqb2lVRzl5ZEdGaWJHVWdSRzlqZFcxbGJuUWdSbTl5YldGMElpd2liV2x0WlZSNWNHVnpJanBiZXlKMGVYQmxJam9pWVhCd2JHbGpZWFJwYjI0dmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmU3g3SW5SNWNHVWlPaUowWlhoMEwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjFkZlN4N0ltNWhiV1VpT2lKTmFXTnliM052Wm5RZ1JXUm5aU0JRUkVZZ1ZtbGxkMlZ5SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpRYjNKMFlXSnNaU0JFYjJOMWJXVnVkQ0JHYjNKdFlYUWlMQ0p0YVcxbFZIbHdaWE1pT2x0N0luUjVjR1VpT2lKaGNIQnNhV05oZEdsdmJpOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5TEhzaWRIbHdaU0k2SW5SbGVIUXZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlYxOUxIc2libUZ0WlNJNklsZGxZa3RwZENCaWRXbHNkQzFwYmlCUVJFWWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDFkLFd5SnlkUzFTVlNKZCwwLDEsMCwyNCwxNDI3NSw4LDIyNzEyNjUyMCwwLDEsMCwtNDkxMjc1NTIzLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1YybHVNeklnTlM0d0lDaFhhVzVrYjNkeklFNVVJREV3TGpBN0lGZHBialkwT3lCNE5qUXBJRUZ3Y0d4bFYyVmlTMmwwTHpVek55NHpOaUFvUzBoVVRVd3NJR3hwYTJVZ1IyVmphMjhwSUVOb2NtOXRaUzh4TXpFdU1DNHdMakFnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmWDE5LDY1LC0xMjg1NTUxMywxLDEsLTEsMTY5OTk1NDg4NywxNjk5OTU0ODg3LDMzNjAwNzkzMywxMg==",
            "domain": ".ozon.ru" 
        },
        {
            "name": "xcid",
            "value": "eb6a2a001d00fdbfca04736ee64baef7",
            "domain": ".ozon.ru" 
        }, 
    ]
       
    #for cookie in cookies_chrome:
    for cookie in cookies:
        driver.add_cookie(cookies[0])
        driver.add_cookie(cookies[1])
        driver.add_cookie(cookies[2])
        driver.add_cookie(cookies[3])
        driver.add_cookie(cookies[4])
        driver.add_cookie(cookies[5])
        driver.add_cookie(cookies[6])
        driver.add_cookie(cookies[7])
        driver.add_cookie(cookies[8])
        driver.add_cookie(cookies[9])
        driver.add_cookie(cookies[10])
        driver.add_cookie(cookies[11])
        driver.add_cookie(cookies[12])
        driver.add_cookie(cookies[13])
        driver.add_cookie(cookies[14])
        driver.add_cookie(cookies[15])
    # time.sleep(3)
    driver.get(url)
    #driver.get_cookies()

    # session_id = driver.get_cookie("session_id")["value"]
    # driver.add_cookie({"name": "session_id", "value": session_id})


    print('++++++++++++++++++++++++++++')
    print('Current session is {0}'.format(driver.session_id))
    session=driver.session_id
    webdriver_version = driver.capabilities['chrome']['chromedriverVersion']
    print('Chrome driver version: ' + webdriver_version)
    #driver.implicitly_wait(10) 
    scroll_down(driver, 80)
    #time.sleep(10)
   
    #driver.refresh()
    #driver.execute_script("return document.documentElement.outerHTML")
    driver.execute_script("return document.documentElement.innerHTML")
    #driver = uc.Chrome(headless=True,use_subprocess=False)
    #html= driver.page_source
    #item=driver.find_element(By.CSS_SELECTOR, 'body')
    item=driver.find_element(By.ID, 'paginatorContent')
    items=item.find_elements(By.XPATH, '*')
 
    # Store the ID of the original window
    original_window = driver.current_window_handle
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    time.sleep(5)
    general_counter=0
    for i in items:
        item=i.find_element(By.XPATH, 'div[1]')
        #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
        scroll_down(driver, 10)
        items = item.find_elements(By.XPATH, "*")
        
        for k in items:
            item=k.find_element(By.XPATH, "div[1]")
            item=item.find_element(By.XPATH, "div[1]")
            #item.find_element(By.XPATH, "a").click()
            link_item=item.find_element(By.XPATH, "a")
            #driver.execute_script("link_item.set_attribute('target: _blank')")
            #driver.execute_script("link_item.set_attribute('target= _blank')")
            actions = ActionChains(driver)
            actions.move_to_element(link_item).perform()
            #actions.click(target).perform()
            link_item.click()
            general_counter+=1
            # window_after = driver.window_handles[1]
            #driver.switch_to.window(window_after)

            # Click the link which opens in a new window
            #driver.find_element(By.LINK_TEXT, "new window").click()

            # Wait for the new window or tab
            # wait = WebDriverWait(driver, 10)
            # driver.wait.until(EC.number_of_windows_to_be(2))


            # Loop through until we find a new window handle
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
            try:
                # window_handle_after=driver.current_window_handle
                # window_after = driver.window_handles[1]
                # driver.switch_to.window(window_handle_after)
                driver.execute_script("return document.documentElement.innerHTML")
                #scroll_down(driver, 10)
                print()
                print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
                print('Here comes item # ' + str(general_counter))
                print('------------------------------------')
                #parsing links to image & video files
                image_files=[]
                try:
                    img_item = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "l9t_27"))
                    )
                    #img_item=driver.find_element(By.CLASS_NAME, 'l9t_27')
                    image_items = img_item.find_elements(By.XPATH, "*")
                    for k in image_items[1:5]:
                        img_item=k.find_element(By.XPATH, "div")
                        actions = ActionChains(driver)
                        #actions.move_to_element(img_item).perform()
                        actions.click(img_item).perform()
                        #img_item.click()

                        try:
                            # video = WebDriverWait(driver, 20).until(
                            # EC.presence_of_element_located((By.CLASS_NAME, "rk7_27"))
                            #     )
                            video=driver.find_element(By.CLASS_NAME, 'rk7_27')
                            video=video.find_element(By.XPATH, "video-player")
                            url_file = video.get_attribute("src")
                            image_files.append(url_file)  
                        except:
                            try:
                                item=driver.find_element(By.CLASS_NAME, 't0l_27')
                                item=item.find_element(By.XPATH, "div")
                                item=item.find_element(By.XPATH, "div")
                                image=item.find_element(By.XPATH, "img")
                                url_file = image.get_attribute("src")
                                image_files.append(url_file)
                            except:
                                pass
                except:
                    item = driver.find_element(By.CLASS_NAME, 't0l_27')
                    item=item.find_element(By.XPATH, "div")
                    item=item.find_element(By.XPATH, "div")
                    image=item.find_element(By.XPATH, "img")
                    url_file = image.get_attribute("src")
                    image_files.append(url_file)
                print('Image files: ')
                for i in image_files:
                    print(i)
                #driver.forward()
                #driver.refresh()
                #driver.execute_script("return document.documentElement.outerHTML")
                item_keys=driver.find_elements(By.CLASS_NAME, 'yk4_27')
                item_values=driver.find_elements(By.CLASS_NAME, 'y4k_27')
                specs={}
                #формирует словарь с тех характеристикам
                for m, n in zip (item_keys, item_values):
                    specs[m.text]=n.text
                #=========================================================================================
                #парсим product_set отдельно от остальных характеристик, так как на странице ozon он стоит отдельно
                #и иногда отсутствует
                try:
                    product_set = driver.find_element(By.CLASS_NAME, 'RA-a1')
                    h3 = product_set.find_elements(By.TAG_NAME,"h3")
                    p = product_set.find_elements(By.TAG_NAME,"p")
                    for k, p in zip (h3, p):
                        specs[k.text]=p.text
                        
                except:
                    print('No product_set data provided')
                for keys, values in specs.items():
                    print(keys + ' : ' + values)

                #LOOKING FOR HEADING
                heading_item = driver.find_element(By.CLASS_NAME,"tm8_27")
                heading = heading_item.find_element(By.TAG_NAME,"h1")

                #===========================Required Attributes================================
                #вычленяем название модели из названия товара, так как в характеристиках на странице ozon её нет
                #и вносим в словарь (обязательный атрибут)
                #input_string='Samsung 27" Монитор ViewFinity S8 LS27B800PXIXCI, черный'
                input_string=heading.text
                #удляем запятые из строки
                #input_string.replace(',','')
                #input_string = ' '.join(input_string.split())
                print('-----------------------------')
                print('Here comes heading text: ')
                print('-----------------------------')
                print("Heading: " + heading.text)#Samsung 34" Монитор S34C650VAI, черный
                #print(input_string)#Samsung 34" Монитор S34C650VAI, черный
                #делим строку на две части по слову "Монитор" и преобразуем её в список (list)
                string=input_string.split('Монитор ')
                #берём вторую часть списка и преобразуем её в строку
                string=str(string[1])
                print("String after word 'monitor': " + string)#S34C650VAI, черный
                try:
                    #и делаем из неё ещё один список, разделив его по "," 
                    model_card_list=string.split(',', 1)
                    model_card_string=str(model_card_list[0])
                    print("Converting the string into list splitting it by ',': " + model_card_string)#['S34C650VAI', ' черный']
                    #берём первую часть и преобразуем эту часть в строку
                except:
                    if '/' in string:
                        #и делаем из неё ещё один список, разделив его по "/" 
                        model_card_list=string.split('/', 1)
                        model_card_string=str(model_card_list[0])
                        print("Converting the string into list splitting it by '/': " + model_card_string)#['S34C650VAI', ' черный']
                    else:
                        model_card_list=string.split(' ', 1)
                        model_card_string=str(model_card_list[0])
                        print("Converting the string into list splitting it by ' ': " + model_card_string)#['S34C650VAI', ' черный']
                        #берём первую часть и преобразуем эту часть в строку
                specs['Название модели (для объединения в одну карточку)']=model_card_string

                #Берем значение бренда из словаря. Если оно отсутствует, вычленяем название бренда из названия модели,
                #и добавляем в Название товара и в словарь
                try: 
                    #brand=specs['Бренд']
                    specs['Бренд'] = "BenQ"
                    brand=specs['Бренд']
                except:
                    brand=input_string.split(' ')
                    brand=str(brand[0])
                    specs['Бренд']=brand

                #формируем название (name) товара
                specs['Тип']='Монитор'
                type_brand_string=[
                    specs['Тип'],
                    #specs['Бренд'],
                    brand,
                    str(specs['Диагональ экрана, дюймы'] + '"'),
                    specs['Название модели (для объединения в одну карточку)'],
                ]
                #transforming list to string
                type_brand_string=' '.join(type_brand_string)
                print(type_brand_string)#Монитор Samsung 34" S34C650VAI
                #если в словаре есть значение цвета, добавляем его название в название товара из heading.text
                #цвет необязательный атрибут
                if 'Цвет' in specs:
                    name_string=[
                        type_brand_string,
                        str(specs['Цвет']).lower()
                        ]
                else:
                    name_string=[
                    type_brand_string,
                    ]
               
                #transforming list to string with commas
                name_string=', '.join(name_string)#Монитор Samsung 34" S34C650VAI, черный
                print('Monitor Name: ' + name_string)

                #Название, которое выводится в качестве основного название товара
                #specs['Название']=name_string
                #===============================================================
                #checking if the sku exists in my DB
                try:
                    model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
                    item=Monitor.objects.get(model_name=model_name)
                    print("It's a duplicate")
                    #checking if the field is Null or Blank
                    #if item.screen_size is None and specs['Диагональ экрана, дюймы'] is not None:
                    #===========editing items with dictionary = 0 ======================================
                    if item.screen_size is None and 'Диагональ экрана, дюймы' in specs:
                        print('ScreenSize ok')
                        if ScreenSize.objects.filter(value=specs['Диагональ экрана, дюймы']).exists():
                            screen_size=ScreenSize.objects.get(value=specs['Диагональ экрана, дюймы'])
                        else:
                            screen_size=ScreenSize.objects.create(
                                value=specs['Диагональ экрана, дюймы']
                            )
                        item.screen_size=screen_size
                    if item.pixel_size is None and 'Размер пикселя, мм' in specs:
                        print('pixel ok')
                        if PixelSize.objects.filter(value=specs['Размер пикселя, мм']).exists():
                            pixel_size=PixelSize.objects.get(value=specs['Размер пикселя, мм'])
                        else:
                            pixel_size=PixelSize.objects.create(
                                value=str(specs['Размер пикселя, мм'])
                            )
                        item.pixel_size=pixel_size
                    if item.warranty_period is None and 'Гарантийный срок' in specs:
                        if WarrantyPeriod.objects.filter(value=specs['Гарантийный срок']).exists():
                            warranty_period=WarrantyPeriod.objects.get(value=specs['Гарантийный срок']) 
                        else:
                            warranty_period=WarrantyPeriod.objects.create(
                                value=str(specs['Гарантийный срок'])
                            )
                        item.warranty_period=warranty_period
                    if item.hdmi_ports is None and 'Число портов HDMI' in specs:
                        if HDMIPorts.objects.filter(value=specs['Число портов HDMI']).exists():
                            hdmi_ports=HDMIPorts.objects.get(value=specs['Число портов HDMI'])
                        else:
                            hdmi_ports=HDMIPorts.objects.create(
                                value=str(specs['Число портов HDMI'])
                            )
                        item.hdmi_ports=hdmi_ports
                    if item.max_screen_frq is None and 'Макс. частота обновления, Гц' in specs:
                        if MaxScreenFrequency.objects.filter(value=specs['Макс. частота обновления, Гц']).exists():
                            max_screen_frq=MaxScreenFrequency.objects.get(value=specs['Макс. частота обновления, Гц'])
                        else:
                            max_screen_frq=MaxScreenFrequency.objects.create(
                                value=str(specs['Макс. частота обновления, Гц'])
                            )
                        item.max_screen_frq=max_screen_frq
                    if item.brightness is None and 'Яркость, кд/м2' in specs:
                        if Brightness.objects.filter(value=specs['Яркость, кд/м2']).exists():
                            brightness=Brightness.objects.get(value=specs['Яркость, кд/м2'])
                        else:
                            brightness=Brightness.objects.create(
                                value=str(specs['Яркость, кд/м2'])
                            )
                        item.brightness=brightness
                    if item.contrast is None and 'Контрастность' in specs:
                        if Contrast.objects.filter(value=specs['Контрастность']).exists():
                            contrast=Contrast.objects.get(value=specs['Контрастность'])
                        else:
                            contrast=Contrast.objects.create(
                                value=str(specs['Контрастность'])
                            )
                        item.contrast=contrast
                    if item.dynamic_contrast is None and 'Динамическая контрастность' in specs:
                        if DynamicContrast.objects.filter(value=specs['Динамическая контрастность']).exists():
                            dynamic_contrast=DynamicContrast.objects.get(value=specs['Динамическая контрастность'])
                        else:
                            dynamic_contrast=DynamicContrast.objects.create(
                                value=str(specs['Динамическая контрастность'])
                            )
                        item.dynamic_contrast=dynamic_contrast
                    if item.vertical_frequency is None and 'Частота вертикальной развертки, Гц' in specs:
                        if VerticalFrequency.objects.filter(value=specs['Частота вертикальной развертки, Гц']).exists():
                            vertical_frequency=VerticalFrequency.objects.get(value=specs['Частота вертикальной развертки, Гц'])
                        else:
                            vertical_frequency=VerticalFrequency.objects.create(
                                value=str(specs['Частота вертикальной развертки, Гц'])
                            )
                        item.vertical_frequency=vertical_frequency
                    if item.horizontal_frequency is None and 'Частота горизонтальной развертки, кГц' in specs:
                        if HorizontalFrequency.objects.filter(value=specs['Частота горизонтальной развертки, кГц']).exists():
                            horizontal_frequency=HorizontalFrequency.objects.get(value=specs['Частота горизонтальной развертки, кГц'])
                        else:
                            horizontal_frequency=HorizontalFrequency.objects.create(
                                value=str(specs['Частота горизонтальной развертки, кГц'])
                            )
                        item.horizontal_frequency=horizontal_frequency
                    if item.web_camera is None and 'Web-камера' in specs:
                        if WebCamera.objects.filter(value=specs['Web-камера']).exists():
                            web_camera=WebCamera.objects.get(value=specs['Web-камера'])
                        else:
                            web_camera=WebCamera.objects.create(
                                value=str(specs['Web-камера'])
                            )
                        item.web_camera=web_camera
                    if item.stand_adjustment is None and 'Уровни регулировки подставки' in specs:
                        if StandAdjustment.objects.filter(value=specs['Уровни регулировки подставки']).exists():
                            stand_adjustment=StandAdjustment.objects.get(value=specs['Уровни регулировки подставки'])
                        else:
                            stand_adjustment=StandAdjustment.objects.create(
                                value=str(specs['Уровни регулировки подставки'])
                            )
                        item.stand_adjustment=stand_adjustment
                    if item.power_capacity is None and 'Потребляемая мощность, Вт' in specs:
                        if PowerCapacity.objects.filter(value=specs['Потребляемая мощность, Вт']).exists():
                            power_capacity=PowerCapacity.objects.get(value=specs['Потребляемая мощность, Вт'])
                        else:
                            power_capacity=PowerCapacity.objects.create(
                                value=str(specs['Потребляемая мощность, Вт'])
                            )
                        item.power_capacity=power_capacity
                    if item.pixel_per_inch is None and 'Плотность пикселей, ppi' in specs:
                        if PixelPerInch.objects.filter(value=specs['Плотность пикселей, ppi']).exists():
                            pixel_per_inch=PixelPerInch.objects.get(value=specs['Плотность пикселей, ppi'])
                        else:
                            pixel_per_inch=PixelPerInch.objects.create(
                                value=str(specs['Плотность пикселей, ppi'])
                            )
                        item.pixel_per_inch=pixel_per_inch
                    if item.response_time is None and 'Время отклика, мс' in specs:
                        if ResponseTime.objects.filter(value=specs['Время отклика, мс']).exists():
                            response_time=ResponseTime.objects.get(value=specs['Время отклика, мс'])
                        else:
                            response_time=ResponseTime.objects.create(
                                value=str(specs['Время отклика, мс'])
                            )
                        item.response_time=response_time
                    if item.description is None and 'Аннотация' is specs:
                        if Description.objects.filter(value=specs['Аннотация']).exists():
                            description=Description.objects.get(value=specs['Аннотация'])
                        else:
                            description=Description.objects.create(
                                value=str(specs['Аннотация'])
                            )
                        item.description=description
                    if item.size is None and 'Размеры, мм' in specs:
                        if Size.objects.filter(value=specs['Размеры, мм']).exists():
                            size=Size.objects.get(value=specs['Размеры, мм'])
                        else:
                            size=Size.objects.create(
                                value=str(specs['Размеры, мм'])
                            )
                        item.size=size
                    if item.product_set is None and 'Комплектация' in specs:
                        if ProductSet.objects.filter(value=specs['Комплектация']).exists():
                            product_set=ProductSet.objects.get(value=specs['Комплектация'])
                        else:
                            product_set=ProductSet.objects.create(
                                value=str(specs['Комплектация'])
                            )
                        item.product_set=product_set
                    if item.life_span is None and 'Срок службы, лет' in specs:
                        if LifeSpan.objects.filter(value=specs['Срок службы, лет']).exists():
                            work_period=LifeSpan.objects.get(value=specs['Срок службы, лет'])
                        else:
                            work_period=LifeSpan.objects.create(
                                value=str(specs['Срок службы, лет'])
                            )
                        item.life_span=life_span
                    if item.weight is None and 'Вес, кг' in specs:
                        if Weight.objects.filter(value=specs['Вес, кг']).exists():
                            weight=Weight.objects.get(value=specs['Вес, кг'])
                        else:
                            weight=Weight.objects.create(
                                value=str(specs['Вес, кг'])
                            )
                        item.weight=weight
                    if item.key_word is None and 'Ключевые слова' in specs:      
                        if KeyWord.objects.filter(value=specs['Ключевые слова']).exists():
                            key_word=KeyWord.objects.get(value=specs['Ключевые слова'])
                        else:
                            key_word=KeyWord.objects.create(
                                value=str(specs['Ключевые слова'])
                            )
                        item.key_word=key_word 
                    if item.part_number is None and 'Партномер' in specs:  
                        if PartNumber.objects.filter(value=specs['Партномер']).exists():
                            part_number=PartNumber.objects.get(value=specs['Партномер'])
                        else:
                            part_number=PartNumber.objects.create(
                                value=str(specs['Партномер'])
                            )
                        item.part_number=part_number
                    #=========================editing items with dictionary > 0=======================================
                    if item.usb_prot is None and 'Количество USB портов' in specs:  
                        if USBPort.objects.get(value=specs['Количество USB портов']).exists():
                            usb_port=USBPort.objects.get(value=specs['Количество USB портов'])
                            item.part_number=usb_port
                    if item.builtin_speaker is None and 'Встроенные динамики' in specs:  
                        if USBPort.objects.get(value=specs['Количество USB портов']).exists():
                            builtin_speaker=BuiltinSpeaker.objects.get(value=specs['Встроенные динамики'])
                            item.builtin_speaker=builtin_speaker
                    if item.curved_display is None and 'Изогнутый экран' in specs:
                        if CurvedDispaly.objects.get(value=specs['Изогнутый экран']).exists():
                            curved_display=CurvedDispaly.objects.get(value=specs['Изогнутый экран'])
                            item.curved_display=curved_display
                    if item.hdr is None and 'Изогнутый экран' in specs:
                        if HDR.objects.get(value=specs['Технология HDR']).exists():
                            hdr=HDR.objects.get(value=specs['Технология HDR'])
                            item.hdr=hdr
                    if item.screen_coating is None and 'Покрытие экрана' in specs:
                        if ScreenCoating.objects.get(value=specs['Покрытие экрана']).exists():
                            screen_coating=ScreenCoating.objects.get(value=specs['Покрытие экрана'])
                            item.screen_coating=screen_coating
                    if item.ratio is None and 'Соотношение сторон' in specs:
                        if Ratio.objects.get(value=specs['Соотношение сторон']).exists():
                            ratio=Ratio.objects.get(value=specs['Соотношение сторон'])
                            item.ratio=ratio
                    if item.look_angle is None and 'Углы обзора (Г/В)' in specs:
                        if LookAngle.objects.get(value=specs['Углы обзора (Г/В)']).exists():
                            look_angle=LookAngle.objects.get(value=specs['Углы обзора (Г/В)'])
                            item.look_angle=look_angle
                    if item.monitor_matrix is None and 'Матрица монитора' in specs:
                        if MonitorMatrix.objects.get(value=specs['Матрица монитора']).exists():
                            monitor_matrix=MonitorMatrix.objects.get(value=specs['Матрица монитора'])
                            item.monitor_matrix=monitor_matrix
                    if item.euro_asian_code_monitor is None and 'ТН ВЭД коды ЕАЭС' in specs:
                        if EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС']).exists():
                            monitor_matrix=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                            item.euro_asian_code_monitor=euro_asian_code_monitor
                    #========================editing is_collection items========================================
                    if item.colour_monitor.count() == 0 and 'Цвет' in specs:
                        string=specs['Цвет']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if ColourMonitor.objects.filter(value=i).exists():
                                    colour_monitor=ColourMonitor.objects.get(value=i)
                                    item.colour_monitor.add(colour_monitor)
                            except:
                                pass
                    if item.monitor_connector.count() == 0 and 'Разъёмы монитора' in specs:
                        string=specs['Разъёмы монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if MonitorConnector.objects.filter(value=i).exists():
                                    monitor_connector=MonitorConnector.objects.get(value=i)
                                    item.monitor_connector.add(monitor_connector)
                            except:
                                pass
                    if item.adjustments.count() == 0 and 'Регулировки' in specs:
                        string=specs['Регулировки']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if Adjustment.objects.filter(value=i).exists():
                                    adjustments=Adjustment.objects.get(value=i)
                                    item.adjustments.add(adjustments)
                            except:
                                pass
                    if item.design_feature.count() == 0 and 'Конструктивные особенности' in specs:
                        string=specs['Конструктивные особенности']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if DesignFeature.objects.filter(value=i).exists():
                                    design_feature=DesignFeature.objects.get(value=i)
                                    item.design_feature.add(design_feature)
                            except:
                                pass
                    if item.vesa_fixture.count() == 0 and 'Стандарт крепления VESA' in specs:
                        string=specs['Стандарт крепления VESA']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if VESAFixture.objects.filter(value=i).exists():
                                    vesa_fixture=VESAFixture.objects.get(value=i)
                                    item.vesa_fixture.add(vesa_fixture)
                            except:
                                pass
                    if item.monitor_installation.count() == 0 and 'Установка монитора' in specs:
                        string=specs['Установка монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if MonitorInstallation.objects.filter(value=i).exists():
                                    monitor_installation=MonitorInstallation.objects.get(value=i)
                                    item.monitor_installation.add(monitor_installation)
                            except:
                                pass
                    if item.monitor_application.count() == 0 and 'Назначение монитора' in specs:
                        string=specs['Назначение монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if MonitorApplication.objects.filter(value=i).exists():
                                    monitor_application=MonitorApplication.objects.get(value=i)
                                    item.monitor_application.add(monitor_application)
                            except:
                                pass
                    if item.hdr_standard.count() == 0 and 'Cтандарты HDR' in specs:
                        string=specs['Cтандарты HDR']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if HDRStandard.objects.filter(value=i).exists():
                                    hdr_standard=HDRStandard.objects.get(value=i)
                                    item.hdr_standard.add(hdr_standard)
                            except:
                                pass
                    if item.country_of_manufacture.count() == 0 and 'Страна-изготовитель' in specs:
                        string=specs['Страна-изготовитель']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if CountryOfManufacture.objects.filter(value=i).exists():
                                    country_of_manufacture=CountryOfManufacture.objects.get(value=i)
                                    item.country_of_manufacture.add(country_of_manufacture)
                            except:
                                pass
                    if item.lighting_type.count() == 0 and 'Тип подсветки' in specs:
                        string=specs['Тип подсветки']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if LightningType.objects.filter(value=i).exists():
                                    lighting_type=LightningType.objects.get(value=i)
                                    item.lighting_type.add(lighting_type)
                            except:
                                pass
                    if item.special_feature.count() == 0 and 'Особенности' in specs:
                        string=specs['Особенности']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            try:
                                if SpecialFeature.objects.filter(value=i).exists():
                                    special_feature=SpecialFeature.objects.get(value=i)
                                    item.special_feature.add(special_feature)
                            except:
                                pass
                            
                    item.save()
                    print('Item Edited')

                #except Monitor.DoesNotExist:
                except Exception as e:
                    print('-------------------------------')
                    print('Error: ')
                    print (e)
                    print('--------------------------------')
                    print('Missing parameters')

                    #=============is_required=======================
                    category_name=OzonCategory.objects.get(type_name='Монитор')
                    #resolution=Resolution.objects.get(value=specs['Разрешение'])
                    try:
                        model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
                    except:
                        model_name=ModelName.objects.create(value=specs['Название модели (для объединения в одну карточку)'])
                    try:
                        name=Name.objects.get(value=name_string)
                    except:
                        name=Name.objects.create(value=name_string)
                    try:
                        type_monitor=TypeMonitor.objects.get(value=specs['Тип'])
                    except:
                        type_monitor=TypeMonitor.objects.get(value='Монитор')
                    try:
                        resolution=Resolution.objects.get(value=specs['Разрешение'])
                    except:
                        resolution=Resolution.objects.get(value='1920x1080 Full HD')
                    try:
                        brand=Brand_Monitor.objects.get(value=specs['Бренд'])
                    except:
                        brand=Brand_Monitor.objects.get(value='Нет бренда')
                    #=============dictionnay id = 0 =====================================
                    try:
                        if ModelName.objects.filter(value=specs['Название модели (для объединения в одну карточку)']).exists():
                            model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
                        else:
                            model_name=ModelName.objects.create(value=str(specs['Название модели (для объединения в одну карточку)']))
                    except:
                        print('smth went wrong with the model_name')                 
                    item=Monitor.objects.create(
                        category_name=category_name,
                        type=type_monitor,
                        resolution=resolution,
                        brand_monitor=brand,
                        model_name=model_name,
                        name=name

                        #part_number=part_number,
                    )
                    list_length=len(image_files)
                    if list_length>1:
                        counter=0
                        for i in image_files:
                            if counter<1:
                                #if i.endswith('mp4'):
                                if '.mp4' in i:
                                    item.video_url=i
                                else:
                                    item.image_1=i
                            elif counter==1:
                                if not item.image_1:
                                    item.image_1=i
                                else:
                                    item.image_2=i
                            elif counter==2:
                                if not item.image_2:
                                    item.image_2=i
                                else:
                                    item.image_3=i
                            elif counter==3:
                                if not item.image_3:
                                    item.image_3=i
                                else:
                                    item.image_4=i
                            counter+=1
                        item.save()
                    #===============attributes with dictionary_id >0=========================
                    try:
                        usb_port=USBPort.objects.get(value=specs['Количество USB портов'])
                        item.usb_port=usb_port
                    except:
                        print('No usb data provided')
                    try:
                        builtin_speaker=BuiltinSpeaker.objects.get(value=specs['Встроенные динамики'])
                        item.builtin_speaker=builtin_speaker
                    except:
                        print('No builtin speakers data provided')
                    try:
                        curved_display=CurvedDispaly.objects.get(value=specs['Изогнутый экран'])
                        item.curved_display=curved_display
                    except:
                        print('No curved display data provided')
                    try:
                        hdr=HDR.objects.get(value=specs['Технология HDR'])
                        item.hdr=hdr
                    except:
                        print('No hdr data provided')
                    try:
                        screen_coating=ScreenCoating.objects.get(value=specs['Покрытие экрана'])
                        item.screen_coating=screen_coating
                    except:
                        print('No screen_coating data provided')
                    try:
                        ratio=Ratio.objects.get(value=specs['Соотношение сторон'])
                        item.ratio=ratio
                    except:
                        print('No ratio data provided')
                    try:
                        look_angle=LookAngle.objects.get(value=specs['Углы обзора (Г/В)'])
                        item.look_angle=look_angle
                    except:
                        print('No look_angle data provided')
                    try:
                        monitor_matrix=MonitorMatrix.objects.get(value=specs['Матрица монитора'])
                        item.monitor_matrix=monitor_matrix
                    except:
                        print('No monitor_matrix data provided')
                    try:
                        euro_asian_code_monitor=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                        item.euro_asian_code_monitor=euro_asian_code_monitor
                    except:
                        print('No euro_asian_code_monitor data provided')

                    #==========================is_collection (Many)=========================================
                    try:
                        string=specs['Цвет']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if ColourMonitor.objects.filter(value=i).exists():
                                colour_monitor=ColourMonitor.objects.get(value=i)
                                item.colour_monitor.add(colour_monitor)
                    except:
                        print('No colour_monitor data provided')
                    try:
                        string=specs['Разъёмы монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if MonitorConnector.objects.filter(value=i).exists():
                                monitor_connector=MonitorConnector.objects.get(value=i)
                                item.monitor_connector.add(monitor_connector)
                    except:
                        print('No monitor connectors data provided')
                    try:
                        string=specs['Регулировки']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if Adjustment.objects.filter(value=i).exists():
                                adjustments=Adjustment.objects.get(value=i)
                                item.adjustments.add(adjustments)
                    except:
                        print('No adjustments data provided')
                    try:
                        string=specs['Конструктивные особенности']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if DesignFeature.objects.filter(value=i).exists():
                                design_feature=DesignFeature.objects.get(value=i)
                                item.design_feature.add(design_feature)
                    except:
                        print('No design_feature data provided')
                    try:
                        string=specs['Стандарт крепления VESA']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if VESAFixture.objects.filter(value=i).exists():
                                vesa_fixture=VESAFixture.objects.get(value=i)
                                item.vesa_fixture.add(vesa_fixture)
                    except:
                        print('No vesa_fixture data provided')
                    try:
                        string=specs['Установка монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if MonitorInstallation.objects.filter(value=i).exists():
                                monitor_installation=MonitorInstallation.objects.get(value=i)
                                item.monitor_installation.add(monitor_installation)
                    except:
                        print('No monitor_installation data provided')
                    try:
                        string=specs['Назначение монитора']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if MonitorApplication.objects.filter(value=i).exists():
                                monitor_application=MonitorApplication.objects.get(value=i)
                                item.monitor_application.add(monitor_application)
                    except:
                        print('No monitor_application data provided')
                    try:
                        string=specs['Cтандарты HDR']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if HDRStandard.objects.filter(value=i).exists():
                                hdr_standard=HDRStandard.objects.get(value=i)
                                item.hdr_standard.add(hdr_standard)
                    except:
                        print('No hdr_standard data provided')
                    try:
                        string=specs['Страна-изготовитель']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if CountryOfManufacture.objects.filter(value=i).exists():
                                country_of_manufacture=CountryOfManufacture.objects.get(value=i)
                                item.country_of_manufacture.add(country_of_manufacture)
                    except:
                        print('No country_of_manufacture data provided')
                    try:
                        string=specs['Тип подсветки']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if LightningType.objects.filter(value=i).exists():
                                lighting_type=LightningType.objects.get(value=i)
                                item.lighting_type.add(lighting_type)
                    except:
                        print('No lighting_type data provided')
                    try:
                        string=specs['Особенности']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if SpecialFeature.objects.filter(value=i).exists():
                                special_feature=SpecialFeature.objects.get(value=i)
                                item.special_feature.add(special_feature)
                    except:
                        print('No special_feature data provided')
                    
                    #======================Model with dictionary_id=0=========================
                    try:
                        if ScreenSize.objects.filter(value=specs['Диагональ экрана, дюймы']).exists():
                            screen_size=ScreenSize.objects.get(value=specs['Диагональ экрана, дюймы'])
                        else:
                            screen_size=ScreenSize.objects.create(
                                value=specs['Диагональ экрана, дюймы']
                            )
                        item.screen_size=screen_size
                    except:
                        print('no screen_size data provided')
                    try:
                        if PixelSize.objects.filter(value=specs['Размер пикселя, мм']).exists():
                            pixel_size=PixelSize.objects.get(value=specs['Размер пикселя, мм'])
                        else:
                            pixel_size=PixelSize.objects.create(
                                value=str(specs['Размер пикселя, мм'])
                            )
                        item.pixel_size=pixel_size
                    except:
                        print('no pixel size data provided')
                    try:
                        if WarrantyPeriod.objects.filter(value=specs['Гарантийный срок']).exists():
                            warranty_period=WarrantyPeriod.objects.get(value=specs['Гарантийный срок']) 
                        else:
                            warranty_period=WarrantyPeriod.objects.create(
                                value=str(specs['Гарантийный срок'])
                            )
                        item.warranty_period=warranty_period
                    except:
                        print('no warranty period data provided')
                    try:
                        if HDMIPorts.objects.filter(value=specs['Число портов HDMI']).exists():
                            hdmi_ports=HDMIPorts.objects.get(value=specs['Число портов HDMI'])
                        else:
                            hdmi_ports=HDMIPorts.objects.create(
                                value=str(specs['Число портов HDMI'])
                            )
                        item.hdmi_ports=hdmi_ports
                    except:
                        print('no hdmi_ports data provided')
                    try:
                        if MaxScreenFrequency.objects.filter(value=specs['Макс. частота обновления, Гц']).exists():
                            max_screen_frq=MaxScreenFrequency.objects.get(value=specs['Макс. частота обновления, Гц'])
                        else:
                            max_screen_frq=MaxScreenFrequency.objects.create(
                                value=str(specs['Макс. частота обновления, Гц'])
                            )
                        item.max_screen_frq=max_screen_frq
                    except:
                        print('no max_screen_frq data provided')
                    try:
                        if Brightness.objects.filter(value=specs['Яркость, кд/м2']).exists():
                            brightness=Brightness.objects.get(value=specs['Яркость, кд/м2'])
                        else:
                            brightness=Brightness.objects.create(
                                value=str(specs['Яркость, кд/м2'])
                            )
                        item.brightness=brightness
                    except:
                        print('no brightness data provided')
                    try:
                        if Contrast.objects.filter(value=specs['Контрастность']).exists():
                            contrast=Contrast.objects.get(value=specs['Контрастность'])
                        else:
                            contrast=Contrast.objects.create(
                                value=str(specs['Контрастность'])
                            )
                        item.contrast=contrast
                    except:
                        print('no contrast data provided')
                    try:
                        if DynamicContrast.objects.filter(value=specs['Динамическая контрастность']).exists():
                            dynamic_contrast=DynamicContrast.objects.get(value=specs['Динамическая контрастность'])
                        else:
                            dynamic_contrast=DynamicContrast.objects.create(
                                value=str(specs['Динамическая контрастность'])
                            )
                        item.dynamic_contrast=dynamic_contrast
                    except:
                        print('no dynamic contrast data provided')
                    try:
                        if VerticalFrequency.objects.filter(value=specs['Частота вертикальной развертки, Гц']).exists():
                            vertical_frequency=VerticalFrequency.objects.get(value=specs['Частота вертикальной развертки, Гц'])
                        else:
                            vertical_frequency=VerticalFrequency.objects.create(
                                value=str(specs['Частота вертикальной развертки, Гц'])
                            )
                        item.vertical_frequency=vertical_frequency
                    except:
                        print('no vertical frequency data provided')
                    try:
                        if HorizontalFrequency.objects.filter(value=specs['Частота горизонтальной развертки, кГц']).exists():
                            horizontal_frequency=HorizontalFrequency.objects.get(value=specs['Частота горизонтальной развертки, кГц'])
                        else:
                            horizontal_frequency=HorizontalFrequency.objects.create(
                                value=str(specs['Частота горизонтальной развертки, кГц'])
                            )
                        item.horizontal_frequency=horizontal_frequency
                    except:
                        print('no horizontal_frequency data provided')
                    try:
                        if WebCamera.objects.filter(value=specs['Web-камера']).exists():
                            web_camera=WebCamera.objects.get(value=specs['Web-камера'])
                        else:
                            web_camera=WebCamera.objects.create(
                                value=str(specs['Web-камера'])
                            )
                        item.web_camera=web_camera
                    except:
                        print('no web camera data provided')
                    try:
                        if StandAdjustment.objects.filter(value=specs['Уровни регулировки подставки']).exists():
                            stand_adjustment=StandAdjustment.objects.get(value=specs['Уровни регулировки подставки'])
                        else:
                            stand_adjustment=StandAdjustment.objects.create(
                                value=str(specs['Уровни регулировки подставки'])
                            )
                        item.stand_adjustment=stand_adjustment
                    except:
                        print('no stand_adustment data provided')
                    try:
                        if PowerCapacity.objects.filter(value=specs['Потребляемая мощность, Вт']).exists():
                            power_capacity=PowerCapacity.objects.get(value=specs['Потребляемая мощность, Вт'])
                        else:
                            power_capacity=PowerCapacity.objects.create(
                                value=str(specs['Потребляемая мощность, Вт'])
                            )
                        item.power_capacity=power_capacity
                    except:
                        print('no power_capacity data provided')
                    try:
                        if PixelPerInch.objects.filter(value=specs['Плотность пикселей, ppi']).exists():
                            pixel_per_inch=PixelPerInch.objects.get(value=specs['Плотность пикселей, ppi'])
                        else:
                            pixel_per_inch=PixelPerInch.objects.create(
                                value=str(specs['Плотность пикселей, ppi'])
                            )
                        item.pixel_per_inch=pixel_per_inch
                    except:
                        print('no pixel_per_inch data provided')
                    try:
                        if ResponseTime.objects.filter(value=specs['Время отклика, мс']).exists():
                            response_time=ResponseTime.objects.get(value=specs['Время отклика, мс'])
                        else:
                            response_time=ResponseTime.objects.create(
                                value=str(specs['Время отклика, мс'])
                            )
                        item.response_time=response_time
                    except:
                        print('no response_time data provided')
                    try:
                        if Description.objects.filter(value=specs['Аннотация']).exists():
                            description=Description.objects.get(value=specs['Аннотация'])
                        else:
                            description=Description.objects.create(
                                value=str(specs['Аннотация'])
                            )
                        item.description=description
                    except:
                        print('no description data provided')
                    try:
                        if Size.objects.filter(value=specs['Размеры, мм']).exists():
                            size=Size.objects.get(value=specs['Размеры, мм'])
                        else:
                            size=Size.objects.create(
                                value=str(specs['Размеры, мм'])
                            )
                        item.size=size
                    except:
                        print('no size data provided')
                    try:
                        if ProductSet.objects.filter(value=specs['Комплектация']).exists():
                            product_set=ProductSet.objects.get(value=specs['Комплектация'])
                        else:
                            product_set=ProductSet.objects.create(
                                value=str(specs['Комплектация'])
                            )
                        item.product_set=product_set
                    except:
                        print('no product_set data provided')
                    try:
                        if LifeSpan.objects.filter(value=specs['Срок службы, лет']).exists():
                            life_span=LifeSpan.objects.get(value=specs['Срок службы, лет'])
                        else:
                            life_span=LifeSpan.objects.create(
                                value=str(specs['Срок службы, лет'])
                            )
                        item.life_span=life_span
                    except:
                        print('no life_span data provided')
                    try:
                        if Weight.objects.filter(value=specs['Вес, кг']).exists():
                            weight=Weight.objects.get(value=specs['Вес, кг'])
                        else:
                            weight=Weight.objects.create(
                                value=str(specs['Вес, кг'])
                            )
                        item.weight=weight
                    except:
                        print('no weight data provided')
                    try:
                        if KeyWord.objects.filter(value=specs['Ключевые слова']).exists():
                            key_word=KeyWord.objects.get(value=specs['Ключевые слова'])
                        else:
                            key_word=KeyWord.objects.create(
                                value=str(specs['Ключевые слова'])
                            )
                        item.key_word=key_word
                    except:
                        print('no key_word data provided')
                    try:
                        if PartNumber.objects.filter(value=specs['Партномер']).exists():
                            part_number=PartNumber.objects.get(value=specs['Партномер'])
                        else:
                            part_number=PartNumber.objects.create(
                                value=str(specs['Партномер'])
                            )
                        item.part_number=part_number
                    except:
                        print('no part_number data provided')

                    print('ITEM CREATED')
                    item.save()
               
                print('==============================')
                #time.sleep(10)
                #driver.back()
            
                #Close the tab or window
                driver.close()
                #driver.get(url)
                #driver.session_id=session
                #Switch back to the old tab or window
                driver.switch_to.window(original_window)
            except:
                driver.close()
                #driver.get(url)
                #driver.session_id=session
                #Switch back to the old tab or window
                driver.switch_to.window(original_window)

    driver.quit()

    return render (request, 'products.html')


 

