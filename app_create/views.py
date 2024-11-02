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
    PartNumber, Name, ModelName,
    )
import datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains

import undetected_chromedriver as uc

#эти импорты нужны нам для организации механизма ожидания формирования страницы
#для последующего получения html из нее
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_down(driver, deep):
    for _ in range(deep):
        driver.execute_script('window.scrollBy(0, 500)')
        time.sleep(0.1)

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

def parsing_images(request):
    driver = webdriver.Chrome()
    url="https://www.ozon.ru/product/samsung-24-monitor-f24t450fzi-chernyy-1684508045/?asb=wSHDDg03QNzF7ktrlBFeZZ5yl4FxB9Ff32p%252B4ZzPKb8%253D&asb2=i83IqHQ0enhMnJJ1mrMLhxgryJD5B646_y3oHpiPcYL4p1Li_HlCF98BTpLxtdnEhYvsuaxxYAgKtEJoo69F_g&avtc=1&avte=2&avts=1729114623&keywords=монитор"
    driver.get(url)
    driver.delete_all_cookies
    cookies = [
        {
            "name": "__Secure-ab-group",
            "value": "72",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-access-token",
            "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241006094133.rRmYwP9swyojNhBNwVlgdzOQil1f4QYs9p4uO6tXu4A.1c4842a1fef265339"
        },
        {
            "name": "__Secure-ETC",
            "value": "123b9d32ba83f8578c9b01168e62fb9f",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-ext_xcid",
            "value": "3f6546900374dcf91a0ac97122c8cb06",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-refresh-token",
            "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241006094133.Mf4O5RYN1lZxytjGRHEZSlCocAIGKI28-KrRR8OOOq8.145286da3eec0b29e",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-user-id",
            "value": "0",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.-5gn7M_xyh7eg7S29jtqs8FzXYAEH6-Apt8m9A-ufn2kMNF91HMg1VJU_BKmwnGXgHW2TXF8Q-kwbl3qUkOpstCsmiqQVlD5nJjc8FiGwlNb_DuRLG4GjikCCM9XjeXSZAHusPSNaKsZUvolxEoBEBUWeVNhd0DxrWVXa-fsZqgClXu_dc1nEkCJc5KezRJ2HPhRM1rBACNO8tfeZgyRdPNvUYSHKPd50dZtpUiryQ-d4M-yixOhGAG4-Tqhqkohb1rpzLBHKEwIZ4wkQGEpxFplNyi7D9f-tCZjWYkgRt6vlVDCelYYCybXeNdVpIGL4LrNwheRqOlK3WcoCz9CZMvotUQ69-MRQt4gcBTj0J2C8WbYONcuh4L6oHLxWx9HeKVfyse1y-HDEkRfx3uas7Fm1Uukvt9ErhlJryID8TchmLEfF0VIc5DghyVR58mRXNGsQ1FLAD4wgi7X9H5UR07_71e40-x8Bc_0",
            "domain": ".ozon.ru" 
        },
        {
            "name": "ADDRESSBOOKBAR_WEB_CLARIFICATION",
            "value": "1727608766",
            "domain": ".ozon.ru" 
        },
        {
            "name": "feedbacklds",
            "value": "[199]",
            "domain": ".ozon.ru" 
        },
        {
            "name": "is_cookies_accepted",
            "value": "1",
            "domain": "www.ozon.ru" 
        },
        {
            "name": "guest",
            "value": "true",
            "domain": "www.ozon.ru" 
        },
        {
            "name": "rfuid",
            "value": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxMDQ0MjEyNTc2LC0xLC0xMTI5MzU3NTU4LFczc2libUZ0WlNJNklsQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMWxJRkJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFwZFcwZ1VFUkdJRlpwWlhkbGNpSXNJbVJsYzJOeWFYQjBhVzl1SWpvaVVHOXlkR0ZpYkdVZ1JHOWpkVzFsYm5RZ1JtOXliV0YwSWl3aWJXbHRaVlI1Y0dWeklqcGJleUowZVhCbElqb2lZWEJ3YkdsallYUnBiMjR2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZTeDdJblI1Y0dVaU9pSjBaWGgwTDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMWRmU3g3SW01aGJXVWlPaUpOYVdOeWIzTnZablFnUldSblpTQlFSRVlnVm1sbGQyVnlJaXdpWkdWelkzSnBjSFJwYjI0aU9pSlFiM0owWVdKc1pTQkViMk4xYldWdWRDQkdiM0p0WVhRaUxDSnRhVzFsVkhsd1pYTWlPbHQ3SW5SNWNHVWlPaUpoY0hCc2FXTmhkR2x2Ymk5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlMSHNpZEhsd1pTSTZJblJsZUhRdmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmVjE5TEhzaWJtRnRaU0k2SWxkbFlrdHBkQ0JpZFdsc2RDMXBiaUJRUkVZaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMWQsV3lKeWRTMVNWU0pkLDAsMSwwLDI0LDE0Mjc1LDgsMjI3MTI2NTIwLDAsMSwwLC00OTEyNzU1MjMsUjI5dloyeGxJRWx1WXk0Z1RtVjBjMk5oY0dVZ1IyVmphMjhnVjJsdU16SWdOUzR3SUNoWGFXNWtiM2R6SUU1VUlERXdMakE3SUZkcGJqWTBPeUI0TmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTOHhNamt1TUM0d0xqQWdVMkZtWVhKcEx6VXpOeTR6TmlBeU1EQXpNREV3TnlCTmIzcHBiR3hoLGV5SmphSEp2YldVaU9uc2lZWEJ3SWpwN0ltbHpTVzV6ZEdGc2JHVmtJanBtWVd4elpTd2lTVzV6ZEdGc2JGTjBZWFJsSWpwN0lrUkpVMEZDVEVWRUlqb2laR2x6WVdKc1pXUWlMQ0pKVGxOVVFVeE1SVVFpT2lKcGJuTjBZV3hzWldRaUxDSk9UMVJmU1U1VFZFRk1URVZFSWpvaWJtOTBYMmx1YzNSaGJHeGxaQ0o5TENKU2RXNXVhVzVuVTNSaGRHVWlPbnNpUTBGT1RrOVVYMUpWVGlJNkltTmhibTV2ZEY5eWRXNGlMQ0pTUlVGRVdWOVVUMTlTVlU0aU9pSnlaV0ZrZVY5MGIxOXlkVzRpTENKU1ZVNU9TVTVISWpvaWNuVnVibWx1WnlKOWZYMTksNjUsLTEyODU1NTEzLDEsMSwtMSwxNjk5OTU0ODg3LDE2OTk5NTQ4ODcsMzM2MDA3OTMzLDEy=",
            "domain": ".ozon.ru" 
        },
        {
            "name": "xcid",
            "value": "9e1c92a0daffe531242b1315d16efe45",
            "domain": ".ozon.ru" 
        },  
    ]
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
    driver.get(url)
    scroll_down(driver, 10)
    time.sleep(5)
    driver.execute_script("return document.documentElement.innerHTML")
    item=driver.find_element(By.XPATH, "//div[@data-widget='webGallery']")
    print('====================================')
    print(item)

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
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=27.000%3B27.000&text=монитор"
    url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=34.000%3B34.000&text=монитор"
    #url="https://www.ozon.ru/product/samsung-27-monitor-essential-monitor-ls27c310eaixci-chernyy-1646295308/features/"
    #url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=22.000%3B22.000&text=%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80"
    driver.get(url)
    #драйвер заходит на сайт со своими cookies. А сервер присваивает браузеру свои cookies, чтобы отличить его от бота.
    #Соответственно заходим на сайт в браузере Chrome, так как мы используем драйвер Chrome. Смотрим cookies Application/Storage/Cookies для браузера
    #Chrome. Обычно их 12 на ozon. Удаляем текущие cookie драйвера. Cookies для разных браузеров отличаются.
    #Присваиваем драйверу cookies браузера. 
    #заходим драйвером еще раз (для этого ничего делать не надо, драйвер сам изменится)
    driver.delete_all_cookies
    cookies = [
        {
            "name": "ADDRESSBOOKBAR_WEB_CLARIFICATION",
            "value": "1730581984",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS013595b9",
            "value": "0187c00a185a6f307e70ecbc2354b4119556ee8f0b92d258a3327a21ab247951c79209e445393b7e1e806c46adf2fa7dec20468a32",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS015d2969",
            "value": "0187c00a185a6f307e70ecbc2354b4119556ee8f0b92d258a3327a21ab247951c79209e445393b7e1e806c46adf2fa7dec20468a32",
            "domain": ".ozon.ru" 
        },
        {
            "name": "TS01f9fe57",
            "value": "0187c00a185a6f307e70ecbc2354b4119556ee8f0b92d258a3327a21ab247951c79209e445393b7e1e806c46adf2fa7dec20468a32",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-ETC",
            "value": "0d98d7bab9500abdc03430ad09ad71cf",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-ab-group",
            "value": "72",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-access-token",
            "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241102231303.saYkVlCnzElPQtrMy5CG2t4QvMK5HmVt8UC1FOc5UXk.1a79985dbeafb1015"
        },
        {
            "name": "__Secure-ext_xcid",
            "value": "3f6546900374dcf91a0ac97122c8cb06",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-refresh-token",
            "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241102125858.rLuGb-x98glelAOcauscE5OOSuKDoyRWw_xk0slSk1U.12bef4f14c2ed878e",
            "domain": ".ozon.ru" 
        },
        {
            "name": "__Secure-user-id",
            "value": "0",
            "domain": ".ozon.ru" 
        },
        # {
        #     "name": "_yasc",
        #     "value": "OrOOmv3yO7Xfg/GLIHYoP45hZmIyUE1+fQVglZbxb1tJbe82ffb0WV48uKHG/Xg22w==",
        #     "domain": ".ozon.ru" 
        # },
        {
            "name": "abt_data",
            "value": "7.ohr6H-55ieN4V500K-3KgDCtBmn8tHcC_NvGPF8GKedRp7nQ_3rOCwyudB4l-VZjI9QP3JzDDdw2jl-nUq7lJN5kkqc3PFFupChKgVnOtVp2yhC2apTcPSyZJUmwPsd8L3Y3YESr8NxnmVfjlXhYHGMKy_vhJn1Ksoe6l2lzFudolnJsxEg0yhrOZO_gK0myFu95SVoG_P6EG-F3JBu3XorFQqNPG9u65h7VQclFWFEctdXHfaBhDBO7OIK1cFMzPdRcP9_UwYri-ihX_9FLgWCjXdot8j_3oh54rRv2TMiB6tJnYrmYAkWFAAxfap-ICcttfCfE0bVvPDuAQtvXRl2XCrgadPDeDmq6rKIcSQNVXKHoDAJUlTWDDbkLViBKMM9r_RGjTDEiXzdzi9Us6Zq1ISYwlrSw2-BFwKNEiqg7NFjJeFFlUvfeeEK5fRVoWc2T7hiWVIE7sdUSVIdXASLjywYDCE6yFmwljVSYz5hzgl15TV_yvBdAUhgMudehAR4tSvBJH2JnM1YVjhHpPiFMW3YUWERL9EnLw31YYrt4liQe5kfm",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.1NpVu84O1t9uQeqYjTz0yFZu0wbL_AGLBCDvw1i22lNbGoIczg2KGrHmy9AkFSK27yQj1kA9KO6SScTyzhCoKTvV9xXlhE8zS2kkoUuq8Q2BobCty7_rzdn48Pt-LYGMW4Tan8i1diRelyQh5oREhX4TiUKwpob7F5MFfvFYILON7wk0-TGwakxucvSYv6wnfaQK43YnpLFhw2jXwToUbscr_NbjeaNXhHyjwPz2s5FpMWimtR4cXW4foFucpWE3wDvymzfDJXa1BC1fMIMB_QI5QHYkZT-HN8ABQEup4V_HjX3ELZFO4pTg_eBIFsEOtD1TFKJ7bTJxA2sNl85O_eKB6Iu7TY9-mGFyk_yVsBavGJNOUQ",
            "domain": ".ozon.ru" 
        },
        {
            "name": "abt_data",
            "value": "7.dQgljXo81xZcn_4jxa_7vQuNhpNsTTd7sWsVWflVfZg7T1GhxHq5Fh0pwMRkR5f82dl4WR74nKZCrRRO4X-dozp_7o75cmhEe-AmtHSNg8nKHG2e-faWppmsdo-dze_M-dKAHU3FoZvn8L47GPthdiMX3B3nP3bogCE1jQfPSc9J-So17zTZHEntUcxplWegnDaT3tqgOXdkBh6-RQK1uFCkV6jvswww5ijAucDsJQWbMW_X4IhLcdXQ1PQDorXiPsO8OgrYbGg9c2CLzcCTNBueHq19qUNYEzkIrfM0ahgA58iBTJxQnhD_gLc89zCuocCukvxP67NztlGwPDsFh0YB0DlNku7AspY",
            "domain": ".ozon.ru" 
        },
        {
            "name": "bacntid",
            "value": "",
            "domain": ".ozon.ru" 
        },
        # {
        #     "name": "contentId",
        #     "value": "867100",
        #     "domain": ".ozon.ru" 
        # },
        # {
        #     "name": "is_cookies_accepted",
        #     "value": "1",
        #     "domain": "www.ozon.ru" 
        # },
        # {
        #     "name": "is_gdpr",
        #     "value": "0",
        #     "domain": "www.ozon.ru" 
        # },
        # {
        #     "name": "is_gdpr_b",
        #     "value": "CNa0CBDXjgI=",
        #     "domain": "www.ozon.ru" 
        # },
        # {
        #     "name": "ob_theme",
        #     "value": "SYSTEM",
        #     "domain": "www.ozon.ru" 
        # },
        {
            "name": "rfuid",
            "value": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxMDQ0MjEyNTc2LC0xLC01NTczNTY4MSxXM3NpYm1GdFpTSTZJbEJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFsSUZCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxcGRXMGdVRVJHSUZacFpYZGxjaUlzSW1SbGMyTnlhWEIwYVc5dUlqb2lVRzl5ZEdGaWJHVWdSRzlqZFcxbGJuUWdSbTl5YldGMElpd2liV2x0WlZSNWNHVnpJanBiZXlKMGVYQmxJam9pWVhCd2JHbGpZWFJwYjI0dmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmU3g3SW5SNWNHVWlPaUowWlhoMEwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjFkZlN4N0ltNWhiV1VpT2lKTmFXTnliM052Wm5RZ1JXUm5aU0JRUkVZZ1ZtbGxkMlZ5SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpRYjNKMFlXSnNaU0JFYjJOMWJXVnVkQ0JHYjNKdFlYUWlMQ0p0YVcxbFZIbHdaWE1pT2x0N0luUjVjR1VpT2lKaGNIQnNhV05oZEdsdmJpOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5TEhzaWRIbHdaU0k2SW5SbGVIUXZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlYxOUxIc2libUZ0WlNJNklsZGxZa3RwZENCaWRXbHNkQzFwYmlCUVJFWWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDFkLFd5SnlkUzFTVlNKZCwwLDEsMCwyNCwyMzc0MTU5MzAsOCwyMjcxMjY1MjAsMCwxLDAsLTQ5MTI3NTUyMyxSMjl2WjJ4bElFbHVZeTRnVG1WMGMyTmhjR1VnUjJWamEyOGdWMmx1TXpJZ05TNHdJQ2hYYVc1a2IzZHpJRTVVSURFd0xqQTdJRmRwYmpZME95QjROalFwSUVGd2NHeGxWMlZpUzJsMEx6VXpOeTR6TmlBb1MwaFVUVXdzSUd4cGEyVWdSMlZqYTI4cElFTm9jbTl0WlM4eE16QXVNQzR3TGpBZ1UyRm1ZWEpwTHpVek55NHpOaUF5TURBek1ERXdOeUJOYjNwcGJHeGgsZXlKamFISnZiV1VpT25zaVlYQndJanA3SW1selNXNXpkR0ZzYkdWa0lqcG1ZV3h6WlN3aVNXNXpkR0ZzYkZOMFlYUmxJanA3SWtSSlUwRkNURVZFSWpvaVpHbHpZV0pzWldRaUxDSkpUbE5VUVV4TVJVUWlPaUpwYm5OMFlXeHNaV1FpTENKT1QxUmZTVTVUVkVGTVRFVkVJam9pYm05MFgybHVjM1JoYkd4bFpDSjlMQ0pTZFc1dWFXNW5VM1JoZEdVaU9uc2lRMEZPVGs5VVgxSlZUaUk2SW1OaGJtNXZkRjl5ZFc0aUxDSlNSVUZFV1Y5VVQxOVNWVTRpT2lKeVpXRmtlVjkwYjE5eWRXNGlMQ0pTVlU1T1NVNUhJam9pY25WdWJtbHVaeUo5ZlgxOSw2NSwtMTI4NTU1MTMsMSwxLC0xLDE2OTk5NTQ4ODcsMTY5OTk1NDg4NywxMTY0MjQ2OTU5LDEy",
            "domain": ".ozon.ru" 
        },
        # {
        #     "name": "sc_company_id",
        #     "value": "867100",
        #     "domain": ".ozon.ru" 
        # },
        {
            "name": "xcid",
            "value": "016969c4e64bda81b2d875f627e9db3f",
            "domain": ".ozon.ru" 
        },
    ]
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
    driver.get(url)
    #driver.implicitly_wait(10) 
    scroll_down(driver, 10)
    time.sleep(3)
    # Store the ID of the original window
    original_window = driver.current_window_handle
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    #driver.refresh()
    #driver.execute_script("return document.documentElement.outerHTML")
    driver.execute_script("return document.documentElement.innerHTML")
    #driver = uc.Chrome(headless=True,use_subprocess=False)
    #html= driver.page_source
    #item=driver.find_element(By.CSS_SELECTOR, 'body')
    item=driver.find_element(By.ID, 'paginatorContent')
    items=item.find_elements(By.XPATH, '*')
    counter=0
    for i in items:
        item=i.find_element(By.XPATH, 'div[1]')
        # for i in item:
        #item=driver.find_element(By.CLASS_NAME, 'j9y_23')
        #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
        #r3j_23_jr4_23 = item.find_elements(By.CSS_SELECTOR, "*")
        #r3j_23_jr4_23 = item.find_elements(By.XPATH, "div")
        scroll_down(driver, 10)
        items = item.find_elements(By.XPATH, "*")
        #for i in items:
            # counter+=1
            # print ('#' + str(counter) + '===============================')
            # print(i.text)
        
        for k in items:
            item=k.find_element(By.XPATH, "div[1]")
            item=item.find_element(By.XPATH, "div[1]")
            target=item.find_element(By.XPATH, "a")
            #print(target.innerHTML)
            actions = ActionChains(driver)
            actions.move_to_element(target).perform()
            target.click()
            # Click the link which opens in a new window
            #driver.find_element(By.LINK_TEXT, "new window").click()

            # Wait for the new window or tab
            #driver.wait.until(EC.number_of_windows_to_be(2))
            # Loop through until we find a new window handle
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break     
            # Wait for the new tab to finish loading content
            #driver.wait.until(EC.title_is("SeleniumHQ Browser Automation"))
            time.sleep(3)
        
            #driver.forward()
            #driver.refresh()
            #driver.execute_script("return document.documentElement.outerHTML")
            #item=driver.find_element(By.ID, 'paginatorContent')
            #item=driver.find_element(By.CLASS_NAME, 'ky0_27')
            item_keys=driver.find_elements(By.CLASS_NAME, 'yk4_27')
            item_values=driver.find_elements(By.CLASS_NAME, 'k4y_27')
            heading = driver.find_element(By.CLASS_NAME,"mt7_27")
            specs={}
            #формирует словарь с тех характеристикам
            for m, n in zip (item_keys, item_values):
                    specs[m.text]=n.text
            #=========================================================================================
            #парсим product_set отдельно от остальных характеристик, так как на странице ozon он стоит отдельно
            #и иногда отсутствует
            try:
                product_set = driver.find_element(By.CLASS_NAME, 'RA-a1')
                #product_set = product_set[5]
                if 'Комплектация' in product_set.text:
                    string=product_set.text
                    string=string.replace('Комплектация', '')
                    specs['Комплектация']=string
                    #print(string)   
            except:
                print('No product_set data provided')

            #parsing links to image & video files
            try:
                video=driver.find_element(By.CLASS_NAME, 'kr7_27')
                video=video.find_element(By.XPATH, "video-player")
                url_file = video.get_attribute("src")
                print(url_file)
            except:
                #img=driver.find_element(By.CLASS_NAME, 'qk2_27 q2k_27')
                item=driver.find_element(By.CLASS_NAME, 'l0t_27')
                #item=item.find_element(By.XPATH, "//img")
                item=item.find_element(By.XPATH, "div")
                item=item.find_element(By.XPATH, "div")
                image=item.find_element(By.XPATH, "img")
                url_file = image.get_attribute("src")
                print(url_file)

            for keys, values in specs.items():
                print(keys + ' : ' + values)
            #===========================Required Attributes================================
            #вычленяем название модели из названия товара, так как в характеристиках на странице ozon её нет
            #и вносим в словарь (обязательный атрибут)
            #input_string='Samsung 27" Монитор ViewFinity S8 LS27B800PXIXCI, черный'
            input_string=heading.text
            #удляем запятые из строки
            #input_string.replace(',','')
            #input_string = ' '.join(input_string.split())
            print('====================================')
            print(heading.text)#Samsung 34" Монитор S34C650VAI, черный
            print(input_string)#Samsung 34" Монитор S34C650VAI, черный
            #делим строку на две части по слову "Монитор" и преобразуем её в список (list)
            string=input_string.split('Монитор ')
            #берём вторую часть списка и преобразуем её в строку
            string=str(string[1])
            print(string)#S34C650VAI, черный
            #и делаем из неё ещё один список, разделив его по "," 
            model_colour_list=string.split(',')
            print(model_colour_list)#['S34C650VAI', ' черный']
            #берём первую часть и преобразуем эту часть в строку
            model_card_string=str(model_colour_list[0])
            print(model_card_string)#S34C650VAI
            specs['Название модели (для объединения в одну карточку)']=model_card_string

            #Берем значение бренда из словаря. Если оно отсутствует, вычленяем название бренда из названия модели,
            #и добавляем в Название товара и в словарь
            try: 
                #brand=specs['Бренд']
                specs['Бренд'] = "Samsung"
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
            #если в словаре есть значение цвета, добавляем его название в Название товара из heading.text
            #цвет необязательный атрибут
            #transforming list to string
            type_brand_string=' '.join(type_brand_string)
            print(type_brand_string)#Монитор Samsung 34" S34C650VAI

            try:
                name_string=[
                    type_brand_string,
                    str(specs['Цвет']).lower()
                    ]
            except:
                try:
                    name_string=[
                        type_brand_string,
                        model_colour_list[1]
                    ]
                    specs['Цвет'] = str(model_colour_list[1]).lower(),
                except:
                    name_string=[
                        type_brand_string,
                        ]
            #transforming list to string with commas
            name_string=', '.join(name_string)#Монитор Samsung 34" S34C650VAI, черный
            print(name_string)

            #Название, которое выводится в качестве основного название товара
            #specs['Название']=name_string

            #===============================================================
            #checking if the sku exists in my DB
            try:
                model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
                monitor=Monitor.objects.get(model_name=model_name)

                # item_list={
                #     # "brand_monitor": "Бренд",
                #     # "resolution": "Разрешение",
                #     "screen_size": "Диагональ экрана, дюймы",
                #     "monitor_matrix": "Матрица монитора",
                #     "max_screen_frq": "Макс. частота обновления, Гц",
                #     "monitor_application": "Назначение монитора",
                #     "special_feature": "Особенности",
                #     "design_feature": "Конструктивные особенности",
                #     "power_capacity": "Потребляемая мощность, Вт",
                #     "curved_display": "Изогнутый экран",
                #     "brightness": "Яркость, кд/м2",
                #     "ratio": "Соотношение сторон",
                #     "screen_coating": "Покрытие экрана",
                #     "response_time": "Время отклика, мс",
                #     "dynamic_contrast" : "Динамическая контрастность",
                #     "contrast": "Контрастность",
                #     "look_angle": "Углы обзора (Г/В)",
                #     "hdr": "Технология HDR",
                #     "hdmi_ports": "Число портов HDMI",
                #     "hdr_standard": "Cтандарты HDR",
                #     "monitor_connector": "Разъёмы монитора",
                #     "vesa_fixture": "Стандарт крепления VESA",
                #     "adjustments": "Регулировки",
                #     "size": "Размеры, мм",
                #     "weight": "Вес, кг",
                #     "web_camera": "Web-камера",
                #     "builtin_speaker": "Встроенные динамики",
                #     "warranty_period": "Гарантийный срок",
                #     "country_of_manufacture": "Страна-изготовитель",
                #     "colour_monitor": "Цвет товара",
                #     "monitor_installation": "Установка монитора",
                #     "product_set":  "Комплектация",
                #     "lighting_type": "Тип подсветки",
                #     "pixel_size": "Размер пикселя, мм",
                #     "pixel_per_inch": "РПлотность пикселей, ppi",
                #     "horizontal_frequency": "Частота горизонтальной развертки, кГц",
                #     "vertical_frequency": "Частота вертикальной развертки, Гц",
                #     "stand_adjustment": "Уровни регулировки подставки",
                #     "usb_port": "Количество USB портов",
                #     "life_span": "Срок службы, лет",
                # }
                # all_fields = Monitor._meta.get_fields()
                # for i in all_fields:
                #     if i.value__isnull == True:
                #         item=item_list[i]
                #         try:
                #             f = Monitor._meta.get_field(i)
                #             usb_port=USBPort.objects.get(value=specs[item])
                #             monitor.usb_port=usb_port
                #         except:
                #             pass

            #except Monitor.DoesNotExist:
            except:
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
                if url_file.endswith('mp4'):
                    item.video_url=url_file
                else:
                    item.image_1=url_file
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

                #==========================is_collection=========================================
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
                    if Name.objects.filter(value=specs['Название']).exists():
                        name=Name.objects.get(value=specs['Название'])
                    else:
                        name=Name.objects.create(
                            value=specs['Название']
                        )
                    item.name=name
                except:
                    print('no name data provided')
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
                    if WorkPeriod.objects.filter(value=specs['Срок службы, лет']).exists():
                        work_period=WorkPeriod.objects.get(value=specs['Срок службы, лет'])
                    else:
                        work_period=WorkPeriod.objects.create(
                            value=str(specs['Срок службы, лет'])
                        )
                    item.work_period=work_period
                except:
                    print('no work_period data provided')
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
             



                item.save()
            #time.sleep(10)
            #driver.back()
        
            #Close the tab or window
            driver.close()
            #Switch back to the old tab or window
            driver.switch_to.window(original_window)
    #driver.quit()

    #return render (request, 'products.html')


 

