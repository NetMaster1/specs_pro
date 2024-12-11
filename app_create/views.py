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
    PartNumber, Name, ModelName, LifeSpan, MaxCardVolume, BatteryCapacity, StandByPeriod, WorkPeriod, RecordMaxSpeed, ProcessorFrequency,
    FrontCamerResolution, BasicCamerResolution, MarketingColour, HardDrive, MatrixType, CardType, BluetoothType, VideoProcessorBrand,
    HazardGrade, VideoProcessor, ProcessorBrand, ProcessorModel, OSMobile, AndroidVersion, IOSVersion, ESimSupport, PublishingYear,
    NavigationType, Sensor, SimType, WifiType, CameraFunction, WirelessInterface, CaseMaterial, Interface, CommunicationStandard,
    ChargingFunction, Stabilization, Authentication,
    )
from app_reference_smartphones.models import (BrandSmartphone, SmartphoneModel, TypeSmartphone, ScreenResolution, VideoQuality, 
    GadgetModel, ProtectionGrade, Colour, QntyOfBasicCamera, Processor, ProcessorCoreQnty, MicroSDSlot, CaseForm, EuroAsianCode,
    SimCardQnty, ScreenResolution, VideoQuality, QntyOfBasicCamera, Processor, ProcessorCoreQnty, MicroSDSlot, CaseForm, ProtectionGrade, 
    
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

def selenium_search_ozon_smartphone(request):
    #driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.proxy = Proxy({ 'proxyType': ProxyType.MANUAL, 'httpProxy' : 'http.proxy:1234'})
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Firefox()
    url="https://www.ozon.ru/category/smartfony-15502/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=смартфон"
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
    scroll_down(driver, 1000)
   
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

    time.sleep(3)
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
                item_keys=driver.find_elements(By.CLASS_NAME, 'y7k_27')
                item_values=driver.find_elements(By.CLASS_NAME, 'ky8_27')
                #формирует словарь с тех характеристикам
                specs={}
                for m, n in zip (item_keys, item_values):
                    key_string=m.text
                    value_string=n.text
                    if '"' in key_string:
                        key_string=key_string.replace('"', "")#deleting ""
                    if ':' in key_string:
                        key_string=key_string.replace(':', "")#deleting ""
                        key_string=key_string.strip()
                    if '"' in value_string:
                        value_string=value_string.replace('"', "")
                    #specs[m.text]=n.text
                    specs[key_string]=value_string   
                #=========================================================================================
                #парсим product_set (комплектация), warranty_period (гарантийный срок) и "название цвета" отдельно от 
                # остальных характеристик, так как на странице ozon они стоит отдельно и иногда отсутствуют
                try:
                    item = driver.find_element(By.CLASS_NAME, 'l6u_27')
                    item_div=item.find_element(By.XPATH, "div[2]")
                    if "Комплектация" in item_div.text:
                        key_items = item_div.find_elements(By.TAG_NAME, 'h3')
                        value_items = item_div.find_elements(By.TAG_NAME,"p")
                        for k, l in zip (key_items, value_items):
                            specs[k.text]=l.text
                    else:
                        item_div=item.find_element(By.XPATH, "div[1]")
                        if "Комплектация" in item_div.text:
                            key_items = item_div.find_elements(By.TAG_NAME, 'h3')
                            value_items = item_div.find_elements(By.TAG_NAME,"p")
                            for k, l in zip (key_items, value_items):
                                specs[k.text]=l.text
                except Exception as e:
                    print('Exception Error #1: ')
                    print (e)
                    print('no product set')
               #specs = dict(sorted(specs.items()))
                for keys, values in specs.items():
                    print(keys + ' : ' + values)
                    time.sleep(3)

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
                string=input_string.split('Смартфон ')
                #берём вторую часть списка и преобразуем её в строку
                string=str(string[1])
                print("String after word 'monitor': " + string)#S34C650VAI, черный
                try:
                    #и делаем из получившейся строки ещё один список, разделив его по первой "," 
                    model_name_list=string.split(',', 1)#['S34C650VAI', ' черный']
                    #преобразуем первую член списка в строку
                    model_name_string=str(model_name_list[0])#S34C650VAI
                    print("Converting the string into list splitting it by ',': " + model_name_string)
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
                specs['Название модели (для объединения в одну карточку)']=model_name_string

                #Берем значение бренда из словаря. Если оно отсутствует, вычленяем название бренда из названия модели,
                #и добавляем в Название товара и в словарь
              
                specs['Бренд'] = "Samsung"
                brand=specs['Бренд']
          
                #формируем название (name) товара
                specs['Тип']='Смартфон'
                type_brand_string=[
                    specs['Тип'],
                    brand,
                    specs['Название модели (для объединения в одну карточку)'],
                    specs['Оперативная память'],
                    specs['Встроенная память'],
                    
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
                
                #Название, которое выводится в качестве основного название товара
                #specs['Название']=name_string
                #transforming list to string with commas
                name_string=', '.join(name_string)#Монитор Samsung 34" S34C650VAI, черный
                print('Monitor Name: ' + name_string)

                #===============================================================
                #checking if the sku exists in my DB
                if ModelName.objects.filter(value=specs['Название модели (для объединения в одну карточку)'], equipment_brand=brand, equipment_type=specs['Тип']).exists():
                    try:
                        model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'], equipment_brand=brand, equipment_type=specs['Тип'])
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
                            print('item.screen_size edited to ' + str(item.screen_size))
                        if item.pixel_size is None and 'Размер пикселя, мм' in specs:
                            if PixelSize.objects.filter(value=specs['Размер пикселя, мм']).exists():
                                pixel_size=PixelSize.objects.get(value=specs['Размер пикселя, мм'])
                            else:
                                pixel_size=PixelSize.objects.create(
                                    value=str(specs['Размер пикселя, мм'])
                                )
                            item.pixel_size=pixel_size
                            print('item.pixel_size edited to ' + str(item.pixel_size))
                        if item.warranty_period is None and 'Гарантийный срок' in specs:
                            if WarrantyPeriod.objects.filter(value=specs['Гарантийный срок']).exists():
                                warranty_period=WarrantyPeriod.objects.get(value=specs['Гарантийный срок']) 
                            else:
                                warranty_period=WarrantyPeriod.objects.create(
                                    value=str(specs['Гарантийный срок'])
                                )
                            item.warranty_period=warranty_period
                            print('item.warranty_period edited to ' + str(item.warranty_period))
                        if item.hdmi_ports is None and 'Число портов HDMI' in specs:
                            if HDMIPorts.objects.filter(value=specs['Число портов HDMI']).exists():
                                hdmi_ports=HDMIPorts.objects.get(value=specs['Число портов HDMI'])
                            else:
                                hdmi_ports=HDMIPorts.objects.create(
                                    value=str(specs['Число портов HDMI'])
                                )
                            item.hdmi_ports=hdmi_ports
                            print('item.hdmi_ports edited')
                        if item.max_screen_frq is None and 'Макс. частота обновления, Гц' in specs:
                            if MaxScreenFrequency.objects.filter(value=specs['Макс. частота обновления, Гц']).exists():
                                max_screen_frq=MaxScreenFrequency.objects.get(value=specs['Макс. частота обновления, Гц'])
                            else:
                                max_screen_frq=MaxScreenFrequency.objects.create(
                                    value=str(specs['Макс. частота обновления, Гц'])
                                )
                            item.max_screen_frq=max_screen_frq
                            print('item.max_screen_frq edited')
                        if item.brightness is None and 'Яркость, кд/м2' in specs:
                            if Brightness.objects.filter(value=specs['Яркость, кд/м2']).exists():
                                brightness=Brightness.objects.get(value=specs['Яркость, кд/м2'])
                            else:
                                brightness=Brightness.objects.create(
                                    value=str(specs['Яркость, кд/м2'])
                                )
                            item.brightness=brightness
                            print('item.brigtness edited')
                        if item.contrast is None and 'Контрастность' in specs:
                            if Contrast.objects.filter(value=specs['Контрастность']).exists():
                                contrast=Contrast.objects.get(value=specs['Контрастность'])
                            else:
                                contrast=Contrast.objects.create(
                                    value=str(specs['Контрастность'])
                                )
                            item.contrast=contrast
                            print('item.contrast edited')
                        if item.dynamic_contrast is None and 'Динамическая контрастность' in specs:
                            if DynamicContrast.objects.filter(value=specs['Динамическая контрастность']).exists():
                                dynamic_contrast=DynamicContrast.objects.get(value=specs['Динамическая контрастность'])
                            else:
                                dynamic_contrast=DynamicContrast.objects.create(
                                    value=str(specs['Динамическая контрастность'])
                                )
                            item.dynamic_contrast=dynamic_contrast
                            print('item.dynamic_contrast edited')
                        if item.vertical_frequency is None and 'Частота вертикальной развертки, Гц' in specs:
                            if VerticalFrequency.objects.filter(value=specs['Частота вертикальной развертки, Гц']).exists():
                                vertical_frequency=VerticalFrequency.objects.get(value=specs['Частота вертикальной развертки, Гц'])
                            else:
                                vertical_frequency=VerticalFrequency.objects.create(
                                    value=str(specs['Частота вертикальной развертки, Гц'])
                                )
                            item.vertical_frequency=vertical_frequency
                            print('item.vertical_frequency edited')
                        if item.horizontal_frequency is None and 'Частота горизонтальной развертки, кГц' in specs:
                            if HorizontalFrequency.objects.filter(value=specs['Частота горизонтальной развертки, кГц']).exists():
                                horizontal_frequency=HorizontalFrequency.objects.get(value=specs['Частота горизонтальной развертки, кГц'])
                            else:
                                horizontal_frequency=HorizontalFrequency.objects.create(
                                    value=str(specs['Частота горизонтальной развертки, кГц'])
                                )
                            item.horizontal_frequency=horizontal_frequency
                            print('item.horizontal_frequency edited')
                        if item.web_camera is None and 'Web-камера' in specs:
                            if WebCamera.objects.filter(value=specs['Web-камера']).exists():
                                web_camera=WebCamera.objects.get(value=specs['Web-камера'])
                            else:
                                web_camera=WebCamera.objects.create(
                                    value=str(specs['Web-камера'])
                                )
                            item.web_camera=web_camera
                            print('item.web_camera edited')
                        if item.stand_adjustment is None and 'Уровни регулировки подставки' in specs:
                            if StandAdjustment.objects.filter(value=specs['Уровни регулировки подставки']).exists():
                                stand_adjustment=StandAdjustment.objects.get(value=specs['Уровни регулировки подставки'])
                            else:
                                stand_adjustment=StandAdjustment.objects.create(
                                    value=str(specs['Уровни регулировки подставки'])
                                )
                            item.stand_adjustment=stand_adjustment
                            print('item.stand_adjustment edited')
                        if item.power_capacity is None and 'Потребляемая мощность, Вт' in specs:
                            if PowerCapacity.objects.filter(value=specs['Потребляемая мощность, Вт']).exists():
                                power_capacity=PowerCapacity.objects.get(value=specs['Потребляемая мощность, Вт'])
                            else:
                                power_capacity=PowerCapacity.objects.create(
                                    value=str(specs['Потребляемая мощность, Вт'])
                                )
                            item.power_capacity=power_capacity
                            print('item.power_capacity edited')
                        if item.pixel_per_inch is None and 'Плотность пикселей, ppi' in specs:
                            if PixelPerInch.objects.filter(value=specs['Плотность пикселей, ppi']).exists():
                                pixel_per_inch=PixelPerInch.objects.get(value=specs['Плотность пикселей, ppi'])
                            else:
                                pixel_per_inch=PixelPerInch.objects.create(
                                    value=str(specs['Плотность пикселей, ppi'])
                                )
                            item.pixel_per_inch=pixel_per_inch
                            print('item.pixel_per_inch edited')
                        if item.response_time is None and 'Время отклика, мс' in specs:
                            if ResponseTime.objects.filter(value=specs['Время отклика, мс']).exists():
                                response_time=ResponseTime.objects.get(value=specs['Время отклика, мс'])
                            else:
                                response_time=ResponseTime.objects.create(
                                    value=str(specs['Время отклика, мс'])
                                )
                            item.response_time=response_time
                            print('item.response_time edited')
                        if item.description is None and 'Аннотация' in specs:
                            if Description.objects.filter(value=specs['Аннотация']).exists():
                                description=Description.objects.get(value=specs['Аннотация'])
                            else:
                                description=Description.objects.create(
                                    value=str(specs['Аннотация'])
                                )
                            item.description=description
                            print('item.description edited')
                        if item.size is None and 'Размеры, мм' in specs:
                            if Size.objects.filter(value=specs['Размеры, мм']).exists():
                                size=Size.objects.get(value=specs['Размеры, мм'])
                            else:
                                size=Size.objects.create(
                                    value=str(specs['Размеры, мм'])
                                )
                            item.size=size
                            print('item.size edited')
                        if item.product_set is None and 'Комплектация' in specs:
                            if ProductSet.objects.filter(value=specs['Комплектация']).exists():
                                product_set=ProductSet.objects.get(value=specs['Комплектация'])
                            else:
                                product_set=ProductSet.objects.create(
                                    value=str(specs['Комплектация'])
                                )
                            item.product_set=product_set
                            print('item.product_set edited to ' + str(item.product_set))
                        if item.life_span is None and 'Срок службы, лет' in specs:
                            if LifeSpan.objects.filter(value=specs['Срок службы, лет']).exists():
                                life_span=LifeSpan.objects.get(value=specs['Срок службы, лет'])
                            else:
                                life_span=LifeSpan.objects.create(
                                    value=str(specs['Срок службы, лет'])
                                )
                            item.life_span=life_span
                            print('item.life_span edited')
                        if item.weight is None and 'Вес, кг' in specs:
                            if Weight.objects.filter(value=specs['Вес, кг']).exists():
                                weight=Weight.objects.get(value=specs['Вес, кг'])
                            else:
                                weight=Weight.objects.create(
                                    value=str(specs['Вес, кг'])
                                )
                            item.weight=weight
                            print('item.weight edited')
                        if item.key_word is None and 'Ключевые слова' in specs:      
                            if KeyWord.objects.filter(value=specs['Ключевые слова']).exists():
                                key_word=KeyWord.objects.get(value=specs['Ключевые слова'])
                            else:
                                key_word=KeyWord.objects.create(
                                    value=str(specs['Ключевые слова'])
                                )
                            item.key_word=key_word 
                            print('item.key_word edited')
                        if item.part_number is None and 'Партномер' in specs:  
                            if PartNumber.objects.filter(value=specs['Партномер']).exists():
                                part_number=PartNumber.objects.get(value=specs['Партномер'])
                            else:
                                part_number=PartNumber.objects.create(
                                    value=str(specs['Партномер'])
                                )
                            item.part_number=part_number
                            print('item.part_number edited')
                        #=========================editing items with dictionary > 0=======================================
                        if item.usb_port is None and 'Количество USB портов' in specs:  
                            if USBPort.objects.filter(value=specs['Количество USB портов']).exists():
                                usb_port=USBPort.objects.get(value=specs['Количество USB портов'])
                                item.usb_port=usb_port
                                print('item.usb_port edited')
                        if item.builtin_speaker is None and 'Встроенные динамики' in specs:  
                            if BuiltinSpeaker.objects.filter(value=specs['Встроенные динамики']).exists():
                                builtin_speaker=BuiltinSpeaker.objects.get(value=specs['Встроенные динамики'])
                                item.builtin_speaker=builtin_speaker
                                print('item.builtin_speaker edited')
                        if item.curved_display is None and 'Изогнутый экран' in specs:
                            if CurvedDispaly.objects.filter(value=specs['Изогнутый экран']).exists():
                                curved_display=CurvedDispaly.objects.get(value=specs['Изогнутый экран'])
                                item.curved_display=curved_display
                                print('item.curved_display edited')
                        if item.hdr is None and 'Технология HDR' in specs:
                            if HDR.objects.filter(value=specs['Технология HDR']).exists():
                                hdr=HDR.objects.get(value=specs['Технология HDR'])
                                item.hdr=hdr
                                print('item.hdr edited')
                        if item.screen_coating is None and 'Покрытие экрана' in specs:
                            if ScreenCoating.objects.filter(value=specs['Покрытие экрана']).exists():
                                screen_coating=ScreenCoating.objects.get(value=specs['Покрытие экрана'])
                                item.screen_coating=screen_coating
                                print('item.screen_coating edited')
                        if item.ratio is None and 'Соотношение сторон' in specs:
                            if Ratio.objects.filter(value=specs['Соотношение сторон']).exists():
                                ratio=Ratio.objects.get(value=specs['Соотношение сторон'])
                                item.ratio=ratio
                                print('item.ratio edited')
                        if item.look_angle is None and 'Углы обзора (Г/В)' in specs:
                            if LookAngle.objects.filter(value=specs['Углы обзора (Г/В)']).exists():
                                look_angle=LookAngle.objects.get(value=specs['Углы обзора (Г/В)'])
                                item.look_angle=look_angle
                                print('item.look_angle edited')
                        if item.monitor_matrix is None and 'Матрица монитора' in specs:
                            if MonitorMatrix.objects.filter(value=specs['Матрица монитора']).exists():
                                monitor_matrix=MonitorMatrix.objects.get(value=specs['Матрица монитора'])
                                item.monitor_matrix=monitor_matrix
                                print('item.monitor_matrix edited')
                        # if item.euro_asian_code_monitor is None and 'ТН ВЭД коды ЕАЭС' in specs:
                        #     if EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС']).exists():
                        #         euro_asian_code_monitor=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                        #         item.euro_asian_code_monitor=euro_asian_code_monitor
                        #         print('item.euro_asian_code_monitor edited')
                        #========================editing is_collection items========================================
                        if item.colour_monitor.count() == 0 and 'Цвет' in specs:
                            string=specs['Цвет']
                            string=string.lower()
                            string=string.replace(", ", ",")#deleting spaces after comma
                            array=string.split(',')#transforming the string into a list
                            for i in array:
                                try:
                                    if ColourMonitor.objects.filter(value=i).exists():
                                        colour_monitor=ColourMonitor.objects.get(value=i)
                                        item.colour_monitor.add(colour_monitor)
                                except:
                                    pass
                            print('item.colour_monitor edited')
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
                            print('item.monitor_connector edited')
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
                            print('item.adjustments edited')
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
                            print('item.design_feature edited')
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
                            print('item.vesa_fixture edited')
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
                            print('item.monitor_installation edited')
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
                            print('item.monitor_application edited to ' + str(item.monitor_application))
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
                            print('item.hdr_stadard edited')
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
                            print('item.country_of_manufacture edited')
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
                            print('item.lightning_type edited')
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
                            print('item.special_feature edited')
                                
                        item.save()
                        print('Item # ' + str(item.id) + ' edited')
                    except Exception as e:
                        print('-------------------------------')
                        print('Exception Error #2: ')
                        print (e)

                else:
                    print('--------------------------------')
                    print('Missing parameters: ')

                    #=============is_required=======================
                    category_name=OzonCategory.objects.get(type_name='Смартфон')
                    #resolution=Resolution.objects.get(value=specs['Разрешение'])
                   
                    model_name=ModelName.objects.create(
                        value=specs['Название модели (для объединения в одну карточку)'],
                        #следующие два параметра нунжы для работы с БД в административной панели
                        #они помогают отдлеть model_names для оборудования разных типов
                        equipment_type=specs['Тип'],
                        equipment_brand=specs['Бренд']
                        )
                    
                    name=Name.objects.create(value=name_string)
                    type_monitor=TypeSmartphone.objects.get(value='Монитор')

                    try:
                        resolution=Resolution.objects.get(value=specs['Разрешение'])
                    except:
                        resolution=Resolution.objects.get(value='1920x1080 Full HD')#in case specs['Разрешение'] does not exist

                    try:
                        brand=Brand_Monitor.objects.get(value=specs['Бренд'])
                    except:
                        brand=Brand_Monitor.objects.get(value='Нет бренда')
                    #=============dictionnay id = 0 =====================================               
                    item=Smartphone.objects.create(
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
                        hard_drive=HardDrive.objects.get(value=specs['Встроенная память'])
                        item.hard_drive=hard_drive
                    except:
                        print('No hard_drive provided')
                    try:
                        matrix_type=MatrixType.objects.get(value=specs['Технология матрицы'])
                        item.matrix_type=matrix_type
                    except:
                        print('No matrix_type data provided')
                    try:
                        sim_card_qnty=SimCardQnty.objects.get(value=specs['Число физических SIM-карт'])
                        item.sim_card_qnty=sim_card_qnty
                    except:
                        print('No sim_card_qnty data provided')
                    try:
                        card_type=CardType.objects.get(value=specs['Тип карты памяти'])
                        item.card_type=card_type
                    except:
                        print('No card_type data provided')
                    try:
                        bluetooth=BluetoothType.objects.get(value=specs['Модуль связи Bluetooth'])
                        item.bluetooth=bluetooth
                    except:
                        print('No bluetooth data provided')
                    try:
                        video_processor_brand=VideoProcessorBrand.objects.get(value=specs['Бренд графического процессора'])
                        item.video_processor_brand=video_processor_brand
                    except:
                        print('No video_processor_brand data provided')
                    try:
                        screen_resolution=ScreenResolution.objects.get(value=specs['Разрешение экрана'])
                        item.screen_resolution=screen_resolution
                    except:
                        print('No screen_resolution data provided')
                    try:
                        video_quality=VideoQuality.objects.get(value=specs['Качество видео'])
                        item.video_quality=video_quality
                    except:
                        print('No video_quality data provided')
                    try:
                        hazard_grade=HazardGrade.objects.get(value=specs['Класс опасности товара'])
                        item.hazard_grade=hazard_grade
                    except:
                        print('No hazard_grade data provided')
                    try:
                        qnty_of_basic_cameras=QntyOfBasicCamera.objects.get(value=specs['Количество основных камер'])
                        item.qnty_of_basic_cameras=qnty_of_basic_cameras
                    except:
                        print('No qnty_of_basic_cameras data provided')
                    try:
                        processor=Processor.objects.get(value=specs['Процессор'])
                        item.processor=processor
                    except:
                        print('No processor data provided')
                    try:
                        video_processor=VideoProcessor.objects.get(value=specs['Видеопроцессор'])
                        item.video_processor=video_processor
                    except:
                        print('No video_processor data provided')
                    try:
                        processor_brand=ProcessorBrand.objects.get(value=specs['Бренд процессора'])
                        item.processor_brand=processor_brand
                    except:
                        print('No processor_brand data provided')
                    try:
                        processor_core_qnty=ProcessorCoreQnty.objects.get(value=specs['Число ядер процессора'])
                        item.processor_core_qnty=processor_core_qnty
                    except:
                        print('No processor_core_qnty data provided')
                    try:
                        processor_model=ProcessorModel.objects.get(value=specs['Модель процессора'])
                        item.processor_model=processor_model
                    except:
                        print('No processor_model data provided')
                    try:
                        operation_system=OSMobile.objects.get(value=specs['Операционная система'])
                        item.operation_system=operation_system
                    except:
                        print('No operation_system data provided')
                    try:
                        android_version=AndroidVersion.objects.get(value=specs['Версия Android'])
                        item.android_version=android_version
                    except:
                        print('No android_version data provided')
                    try:
                        microsd_slot=MicroSDSlot.objects.get(value=specs['Слот для карты памяти'])
                        item.microsd_slot=microsd_slot
                    except:
                        print('No microsd_slot data provided')
                    try:
                        case_form=CaseForm.objects.get(value=specs['Тип корпуса'])
                        item.case_form=case_form
                    except:
                        print('No case_form data provided')
                    try:
                        ios_version=IOSVersion.objects.get(value=specs['Версия iOS'])
                        item.ios_version=ios_version
                    except:
                        print('No ios_version data provided')
                    try:
                        esim_support=ESimSupport.objects.get(value=specs['Поддержка eSim'])
                        item.esim_support=esim_support
                    except:
                        print('No esim_support data provided')
                    try:
                        ram=RamSmartphone.objects.get(value=specs['Оперативная память'])
                        item.ram=ram
                    except:
                        print('No ram data provided')
                    try:
                        publishing_year=PublishingYear.objects.get(value=specs['Год анонсирования'])
                        item.publishing_year=publishing_year
                    except:
                        print('No publishing_year data provided')
                    # try:
                    #     euro_asian_code_monitor=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                    #     item.euro_asian_code_monitor=euro_asian_code_monitor
                    # except:
                    #     print('No euro_asian_code_monitor data provided')

                    #==========================is_collection (Many)=========================================
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
                        string=specs['Навигация']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if NavigationType.objects.filter(value=i).exists():
                                navigation=NavigationType.objects.get(value=i)
                                item.navigation.add(navigation)
                    except:
                        print('No navigation data provided')
                    try:
                        string=specs['Встроенные датчики']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if Sensor.objects.filter(value=i).exists():
                                sensor=Sensor.objects.get(value=i)
                                item.sensor.add(sensor)
                    except:
                        print('No sensor data provided')
                    try:
                        string=specs['Форм-фактор SIM']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if SimType.objects.filter(value=i).exists():
                                sim_type=SimType.objects.get(value=i)
                                item.sim_type.add(sim_type)
                    except:
                        print('No sim_type data provided')
                    try:
                        string=specs['Модуль связи WiFi']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if WifiType.objects.filter(value=i).exists():
                                wifi=WifiType.objects.get(value=i)
                                item.wifi.add(wifi)
                    except:
                        print('No wifi data provided')
                    try:
                        string=specs['Степень защиты']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if ProtectionGrade.objects.filter(value=i).exists():
                                protection_grade=ProtectionGrade.objects.get(value=i)
                                item.protection_grade.add(protection_grade)
                    except:
                        print('No protection_grade data provided')
                    try:
                        string=specs['Функции камеры']
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if CameraFunction.objects.filter(value=i).exists():
                                camera_function=CameraFunction.objects.get(value=i)
                                item.camera_function.add(camera_function)
                    except:
                        print('No camera_function data provided')
                    try:
                        string=specs['Цвет товара']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            str(specs['Цвет']).lower()
                            if Colour.objects.filter(value=i).exists():
                                colour=Colour.objects.get(value=i)
                                item.colour.add(colour)
                    except:
                        print('No colour data provided')
                    try:
                        string=specs['Беспроводные интерфейсы']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if WirelessInterface.objects.filter(value=i).exists():
                                wireless_interface=WirelessInterface.objects.get(value=i)
                                item.wireless_interface.add(wireless_interface)
                    except:
                        print('No wireless_interface data provided')
                    try:
                        string=specs['Основной материал корпуса']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if CaseMaterial.objects.filter(value=i).exists():
                                case_material=CaseMaterial.objects.get(value=i)
                                item.case_material.add(case_material)
                    except:
                        print('No case_material data provided')
                    try:
                        string=specs['Интерфейсы']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if Interface.objects.filter(value=i).exists():
                                interface=Interface.objects.get(value=i)
                                item.interface.add(interface)
                    except:
                        print('No interface data provided')
                    try:
                        string=specs['Стандарты связи']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if CommunicationStandard.objects.filter(value=i).exists():
                                comms_standard=CommunicationStandard.objects.get(value=i)
                                item.comms_standard.add(comms_standard)
                    except:
                        print('No comms_standard data provided')
                    try:
                        string=specs['Стандарты связи']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if CommunicationStandard.objects.filter(value=i).exists():
                                comms_standard=CommunicationStandard.objects.get(value=i)
                                item.comms_standard.add(comms_standard)
                    except:
                        print('No comms_standard data provided')
                    try:
                        string=specs['Особенности']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if SpecialFeature.objects.filter(value=i).exists():
                                special_feature=SpecialFeature.objects.get(value=i)
                                item.special_feature.add(special_feature)
                    except:
                        print('No special_feature data provided')
                    try:
                        string=specs['Функции зарядки']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if ChargingFunction.objects.filter(value=i).exists():
                                stabilization=ChargingFunction.objects.get(value=i)
                                item.charging_function.add(charging_function)
                    except:
                        print('No charging_function data provided')
                    try:
                        string=specs['Стабилизация']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if Stabilization.objects.filter(value=i).exists():
                                stabilization=Stabilization.objects.get(value=i)
                                item.stabilization.add(stabilization)
                    except:
                        print('No stabilization data provided')
                    try:
                        string=specs['Аутентификация']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            if Authentication.objects.filter(value=i).exists():
                                authentification=Authentication.objects.get(value=i)
                                item.authentification.add(authentification)
                    except:
                        print('No authentification data provided')




                    
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
                        if Weight.objects.filter(value=specs['Вес товара, г']).exists():
                            weight=Weight.objects.get(value=specs['Вес, кг'])
                        else:
                            weight=Weight.objects.create(
                                value=str(specs['Вес товара, г'])
                            )
                        item.weight=weight
                    except:
                        print('no weight data provided')
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
                        if MaxCardVolume.objects.filter(value=specs['Макс. объём карты памяти, ГБ']).exists():
                            max_card_volume=MaxCardVolume.objects.get(value=specs['Партномер'])
                        else:
                            max_card_volume=MaxCardVolume.objects.create(
                                value=str(specs['Макс. объём карты памяти, ГБ'])
                            )
                        item.max_card_volume=max_card_volume
                    except:
                        print('no max_card_volume data provided')
                    try:
                        if FrontCamerResolution.objects.filter(value=specs['Разрешение фронтальной (селфи) камеры, Мпикс']).exists():
                            front_camera_resolution=FrontCamerResolution.objects.get(value=specs['Разрешение фронтальной (селфи) камеры, Мпикс'])
                        else:
                            front_camera_resolution=FrontCamerResolution.objects.create(
                                value=str(specs['Разрешение фронтальной (селфи) камеры, Мпикс'])
                            )
                        item.front_camera_resolution=front_camera_resolution
                    except:
                        print('no front_camera_resolution data provided')
                    try:
                        if BasicCamerResolution.objects.filter(value=specs['Разрешение фронтальной (селфи) камеры, Мпикс']).exists():
                            basic_camera_resolution=BasicCamerResolution.objects.get(value=specs['Разрешение фронтальной (селфи) камеры, Мпикс'])
                        else:
                            basic_camera_resolution=BasicCamerResolution.objects.create(
                                value=str(specs['Разрешение фронтальной (селфи) камеры, Мпикс'])
                            )
                        item.basic_camera_resolution=basic_camera_resolution
                    except:
                        print('no basic_camera_resolution data provided')
                    try:
                        if BatteryCapacity.objects.filter(value=specs['Емкость аккумулятора, мАч']).exists():
                            battery_capacity=BatteryCapacity.objects.get(value=specs['Емкость аккумулятора, мАч'])
                        else:
                            battery_capacity=BatteryCapacity.objects.create(
                                value=str(specs['Емкость аккумулятора, мАч'])
                            )
                        item.battery_capacity=battery_capacity
                    except:
                        print('no battery_capacity data provided')
                    try:
                        if StandByPeriod.objects.filter(value=specs['Работа в режиме ожидания, ч']).exists():
                            standby_period=StandByPeriod.objects.get(value=specs['Работа в режиме ожидания, ч'])
                        else:
                            standby_period=StandByPeriod.objects.create(
                                value=str(specs['Работа в режиме ожидания, ч'])
                            )
                        item.standby_period=standby_period
                    except:
                        print('no standby_period data provided')
                    try:
                        if WorkPeriod.objects.filter(value=specs['Время работы в режиме разговора, ч']).exists():
                            work_period=WorkPeriod.objects.get(value=specs['Время работы в режиме разговора, ч'])
                        else:
                            work_period=WorkPeriod.objects.create(
                                value=str(specs['Время работы в режиме разговора, ч'])
                            )
                        item.work_period=work_period
                    except:
                        print('no work_period data provided')
                    try:
                        if RecordMaxSpeed.objects.filter(value=specs['Макс. скорость видеосъемки, кадр/с']).exists():
                            record_max_speed=RecordMaxSpeed.objects.get(value=specs['Макс. скорость видеосъемки, кадр/с'])
                        else:
                            record_max_speed=RecordMaxSpeed.objects.create(
                                value=specs['Макс. скорость видеосъемки, кадр/с']
                            )
                        item.record_max_speed=record_max_speed
                    except:
                        print('no record_max_speed data provided')
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
                        if MarketingColour.objects.filter(value=specs['Название цвета']).exists():
                            marketing_colour=MarketingColour.objects.get(value=specs['Название цвета'])
                        else:
                            marketing_colour=MarketingColour.objects.create(
                                value=str(specs['Название цвета'])
                            )
                        item.marketing_colour=marketing_colour
                    except:
                        print('no marketing_colour data provided')
                    try:
                        if ProcessorFrequency.objects.filter(value=specs['Частота процессора, ГГц']).exists():
                            processor_frequency=ProcessorFrequency.objects.get(value=specs['Частота процессора, ГГц'])
                        else:
                            processor_frequency=ProcessorFrequency.objects.create(
                                value=str(specs['Частота процессора, ГГц'])
                            )
                        item.processor_frequency=processor_frequency
                    except:
                        print('no processor_frequency data provided')
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
                    print('ITEM # ' + str(item.id) + ' CREATED')


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


def selenium_search_ozon_monitor(request):
    #driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.proxy = Proxy({ 'proxyType': ProxyType.MANUAL, 'httpProxy' : 'http.proxy:1234'})
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Firefox()
    url="https://www.ozon.ru/category/monitory-15738/benq-26303024/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=brand&text=монитор"
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
    scroll_down(driver, 1000)
   
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

    time.sleep(3)
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
                item_keys=driver.find_elements(By.CLASS_NAME, 'yk4_27')
                item_values=driver.find_elements(By.CLASS_NAME, 'y4k_27')
                specs={}
                #формирует словарь с тех характеристикам
                for m, n in zip (item_keys, item_values):
                    key_string=m.text
                    value_string=n.text
                    if '"' in key_string:
                        key_string=key_string.replace('"', "")#deleting ""
                    if ':' in key_string:
                        key_string=key_string.replace(':', "")#deleting ""
                        key_string=key_string.strip()
                    if '"' in value_string:
                        value_string=value_string.replace('"', "")
                    #specs[m.text]=n.text
                    specs[key_string]=value_string   
                #=========================================================================================
                #парсим product_set отдельно от остальных характеристик, так как на странице ozon он стоит отдельно
                #и иногда отсутствует
                try:
                    item = driver.find_element(By.CLASS_NAME, 'l6u_27')
                    item_div=item.find_element(By.XPATH, "div[2]")
                    if "Комплектация" in item_div.text:
                        key_items = item_div.find_elements(By.TAG_NAME, 'h3')
                        value_items = item_div.find_elements(By.TAG_NAME,"p")
                        for k, l in zip (key_items, value_items):
                            specs[k.text]=l.text
                    else:
                        item_div=item.find_element(By.XPATH, "div[1]")
                        if "Комплектация" in item_div.text:
                            key_items = item_div.find_elements(By.TAG_NAME, 'h3')
                            value_items = item_div.find_elements(By.TAG_NAME,"p")
                            for k, l in zip (key_items, value_items):
                                specs[k.text]=l.text
                except Exception as e:
                    print('Exception Error #1: ')
                    print (e)
                    print('no product set')
                specs = dict(sorted(specs.items()))
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
                    #и делаем из получившейся строки ещё один список, разделив его по первой "," 
                    model_name_list=string.split(',', 1)#['S34C650VAI', ' черный']
                    #преобразуем первую член списка в строку
                    model_name_string=str(model_name_list[0])#S34C650VAI
                    print("Converting the string into list splitting it by ',': " + model_name_string)
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
                specs['Название модели (для объединения в одну карточку)']=model_name_string

                #Берем значение бренда из словаря. Если оно отсутствует, вычленяем название бренда из названия модели,
                #и добавляем в Название товара и в словарь
              
                specs['Бренд'] = "BenQ"
                brand=specs['Бренд']
          
                #формируем название (name) товара
                specs['Тип']='Монитор'
                type_brand_string=[
                    specs['Тип'],
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
                
                #Название, которое выводится в качестве основного название товара
                #specs['Название']=name_string
                #transforming list to string with commas
                name_string=', '.join(name_string)#Монитор Samsung 34" S34C650VAI, черный
                print('Monitor Name: ' + name_string)

                #===============================================================
                #checking if the sku exists in my DB
                if ModelName.objects.filter(value=specs['Название модели (для объединения в одну карточку)'], equipment_brand=brand, equipment_type=specs['Тип']).exists():
                    try:
                        model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'], equipment_brand=brand, equipment_type=specs['Тип'])
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
                            print('item.screen_size edited to ' + str(item.screen_size))
                        if item.pixel_size is None and 'Размер пикселя, мм' in specs:
                            if PixelSize.objects.filter(value=specs['Размер пикселя, мм']).exists():
                                pixel_size=PixelSize.objects.get(value=specs['Размер пикселя, мм'])
                            else:
                                pixel_size=PixelSize.objects.create(
                                    value=str(specs['Размер пикселя, мм'])
                                )
                            item.pixel_size=pixel_size
                            print('item.pixel_size edited to ' + str(item.pixel_size))
                        if item.warranty_period is None and 'Гарантийный срок' in specs:
                            if WarrantyPeriod.objects.filter(value=specs['Гарантийный срок']).exists():
                                warranty_period=WarrantyPeriod.objects.get(value=specs['Гарантийный срок']) 
                            else:
                                warranty_period=WarrantyPeriod.objects.create(
                                    value=str(specs['Гарантийный срок'])
                                )
                            item.warranty_period=warranty_period
                            print('item.warranty_period edited to ' + str(item.warranty_period))
                        if item.hdmi_ports is None and 'Число портов HDMI' in specs:
                            if HDMIPorts.objects.filter(value=specs['Число портов HDMI']).exists():
                                hdmi_ports=HDMIPorts.objects.get(value=specs['Число портов HDMI'])
                            else:
                                hdmi_ports=HDMIPorts.objects.create(
                                    value=str(specs['Число портов HDMI'])
                                )
                            item.hdmi_ports=hdmi_ports
                            print('item.hdmi_ports edited')
                        if item.max_screen_frq is None and 'Макс. частота обновления, Гц' in specs:
                            if MaxScreenFrequency.objects.filter(value=specs['Макс. частота обновления, Гц']).exists():
                                max_screen_frq=MaxScreenFrequency.objects.get(value=specs['Макс. частота обновления, Гц'])
                            else:
                                max_screen_frq=MaxScreenFrequency.objects.create(
                                    value=str(specs['Макс. частота обновления, Гц'])
                                )
                            item.max_screen_frq=max_screen_frq
                            print('item.max_screen_frq edited')
                        if item.brightness is None and 'Яркость, кд/м2' in specs:
                            if Brightness.objects.filter(value=specs['Яркость, кд/м2']).exists():
                                brightness=Brightness.objects.get(value=specs['Яркость, кд/м2'])
                            else:
                                brightness=Brightness.objects.create(
                                    value=str(specs['Яркость, кд/м2'])
                                )
                            item.brightness=brightness
                            print('item.brigtness edited')
                        if item.contrast is None and 'Контрастность' in specs:
                            if Contrast.objects.filter(value=specs['Контрастность']).exists():
                                contrast=Contrast.objects.get(value=specs['Контрастность'])
                            else:
                                contrast=Contrast.objects.create(
                                    value=str(specs['Контрастность'])
                                )
                            item.contrast=contrast
                            print('item.contrast edited')
                        if item.dynamic_contrast is None and 'Динамическая контрастность' in specs:
                            if DynamicContrast.objects.filter(value=specs['Динамическая контрастность']).exists():
                                dynamic_contrast=DynamicContrast.objects.get(value=specs['Динамическая контрастность'])
                            else:
                                dynamic_contrast=DynamicContrast.objects.create(
                                    value=str(specs['Динамическая контрастность'])
                                )
                            item.dynamic_contrast=dynamic_contrast
                            print('item.dynamic_contrast edited')
                        if item.vertical_frequency is None and 'Частота вертикальной развертки, Гц' in specs:
                            if VerticalFrequency.objects.filter(value=specs['Частота вертикальной развертки, Гц']).exists():
                                vertical_frequency=VerticalFrequency.objects.get(value=specs['Частота вертикальной развертки, Гц'])
                            else:
                                vertical_frequency=VerticalFrequency.objects.create(
                                    value=str(specs['Частота вертикальной развертки, Гц'])
                                )
                            item.vertical_frequency=vertical_frequency
                            print('item.vertical_frequency edited')
                        if item.horizontal_frequency is None and 'Частота горизонтальной развертки, кГц' in specs:
                            if HorizontalFrequency.objects.filter(value=specs['Частота горизонтальной развертки, кГц']).exists():
                                horizontal_frequency=HorizontalFrequency.objects.get(value=specs['Частота горизонтальной развертки, кГц'])
                            else:
                                horizontal_frequency=HorizontalFrequency.objects.create(
                                    value=str(specs['Частота горизонтальной развертки, кГц'])
                                )
                            item.horizontal_frequency=horizontal_frequency
                            print('item.horizontal_frequency edited')
                        if item.web_camera is None and 'Web-камера' in specs:
                            if WebCamera.objects.filter(value=specs['Web-камера']).exists():
                                web_camera=WebCamera.objects.get(value=specs['Web-камера'])
                            else:
                                web_camera=WebCamera.objects.create(
                                    value=str(specs['Web-камера'])
                                )
                            item.web_camera=web_camera
                            print('item.web_camera edited')
                        if item.stand_adjustment is None and 'Уровни регулировки подставки' in specs:
                            if StandAdjustment.objects.filter(value=specs['Уровни регулировки подставки']).exists():
                                stand_adjustment=StandAdjustment.objects.get(value=specs['Уровни регулировки подставки'])
                            else:
                                stand_adjustment=StandAdjustment.objects.create(
                                    value=str(specs['Уровни регулировки подставки'])
                                )
                            item.stand_adjustment=stand_adjustment
                            print('item.stand_adjustment edited')
                        if item.power_capacity is None and 'Потребляемая мощность, Вт' in specs:
                            if PowerCapacity.objects.filter(value=specs['Потребляемая мощность, Вт']).exists():
                                power_capacity=PowerCapacity.objects.get(value=specs['Потребляемая мощность, Вт'])
                            else:
                                power_capacity=PowerCapacity.objects.create(
                                    value=str(specs['Потребляемая мощность, Вт'])
                                )
                            item.power_capacity=power_capacity
                            print('item.power_capacity edited')
                        if item.pixel_per_inch is None and 'Плотность пикселей, ppi' in specs:
                            if PixelPerInch.objects.filter(value=specs['Плотность пикселей, ppi']).exists():
                                pixel_per_inch=PixelPerInch.objects.get(value=specs['Плотность пикселей, ppi'])
                            else:
                                pixel_per_inch=PixelPerInch.objects.create(
                                    value=str(specs['Плотность пикселей, ppi'])
                                )
                            item.pixel_per_inch=pixel_per_inch
                            print('item.pixel_per_inch edited')
                        if item.response_time is None and 'Время отклика, мс' in specs:
                            if ResponseTime.objects.filter(value=specs['Время отклика, мс']).exists():
                                response_time=ResponseTime.objects.get(value=specs['Время отклика, мс'])
                            else:
                                response_time=ResponseTime.objects.create(
                                    value=str(specs['Время отклика, мс'])
                                )
                            item.response_time=response_time
                            print('item.response_time edited')
                        if item.description is None and 'Аннотация' in specs:
                            if Description.objects.filter(value=specs['Аннотация']).exists():
                                description=Description.objects.get(value=specs['Аннотация'])
                            else:
                                description=Description.objects.create(
                                    value=str(specs['Аннотация'])
                                )
                            item.description=description
                            print('item.description edited')
                        if item.size is None and 'Размеры, мм' in specs:
                            if Size.objects.filter(value=specs['Размеры, мм']).exists():
                                size=Size.objects.get(value=specs['Размеры, мм'])
                            else:
                                size=Size.objects.create(
                                    value=str(specs['Размеры, мм'])
                                )
                            item.size=size
                            print('item.size edited')
                        if item.product_set is None and 'Комплектация' in specs:
                            if ProductSet.objects.filter(value=specs['Комплектация']).exists():
                                product_set=ProductSet.objects.get(value=specs['Комплектация'])
                            else:
                                product_set=ProductSet.objects.create(
                                    value=str(specs['Комплектация'])
                                )
                            item.product_set=product_set
                            print('item.product_set edited to ' + str(item.product_set))
                        if item.life_span is None and 'Срок службы, лет' in specs:
                            if LifeSpan.objects.filter(value=specs['Срок службы, лет']).exists():
                                life_span=LifeSpan.objects.get(value=specs['Срок службы, лет'])
                            else:
                                life_span=LifeSpan.objects.create(
                                    value=str(specs['Срок службы, лет'])
                                )
                            item.life_span=life_span
                            print('item.life_span edited')
                        if item.weight is None and 'Вес, кг' in specs:
                            if Weight.objects.filter(value=specs['Вес, кг']).exists():
                                weight=Weight.objects.get(value=specs['Вес, кг'])
                            else:
                                weight=Weight.objects.create(
                                    value=str(specs['Вес, кг'])
                                )
                            item.weight=weight
                            print('item.weight edited')
                        if item.key_word is None and 'Ключевые слова' in specs:      
                            if KeyWord.objects.filter(value=specs['Ключевые слова']).exists():
                                key_word=KeyWord.objects.get(value=specs['Ключевые слова'])
                            else:
                                key_word=KeyWord.objects.create(
                                    value=str(specs['Ключевые слова'])
                                )
                            item.key_word=key_word 
                            print('item.key_word edited')
                        if item.part_number is None and 'Партномер' in specs:  
                            if PartNumber.objects.filter(value=specs['Партномер']).exists():
                                part_number=PartNumber.objects.get(value=specs['Партномер'])
                            else:
                                part_number=PartNumber.objects.create(
                                    value=str(specs['Партномер'])
                                )
                            item.part_number=part_number
                            print('item.part_number edited')
                        #=========================editing items with dictionary > 0=======================================
                        if item.usb_port is None and 'Количество USB портов' in specs:  
                            if USBPort.objects.filter(value=specs['Количество USB портов']).exists():
                                usb_port=USBPort.objects.get(value=specs['Количество USB портов'])
                                item.usb_port=usb_port
                                print('item.usb_port edited')
                        if item.builtin_speaker is None and 'Встроенные динамики' in specs:  
                            if BuiltinSpeaker.objects.filter(value=specs['Встроенные динамики']).exists():
                                builtin_speaker=BuiltinSpeaker.objects.get(value=specs['Встроенные динамики'])
                                item.builtin_speaker=builtin_speaker
                                print('item.builtin_speaker edited')
                        if item.curved_display is None and 'Изогнутый экран' in specs:
                            if CurvedDispaly.objects.filter(value=specs['Изогнутый экран']).exists():
                                curved_display=CurvedDispaly.objects.get(value=specs['Изогнутый экран'])
                                item.curved_display=curved_display
                                print('item.curved_display edited')
                        if item.hdr is None and 'Технология HDR' in specs:
                            if HDR.objects.filter(value=specs['Технология HDR']).exists():
                                hdr=HDR.objects.get(value=specs['Технология HDR'])
                                item.hdr=hdr
                                print('item.hdr edited')
                        if item.screen_coating is None and 'Покрытие экрана' in specs:
                            if ScreenCoating.objects.filter(value=specs['Покрытие экрана']).exists():
                                screen_coating=ScreenCoating.objects.get(value=specs['Покрытие экрана'])
                                item.screen_coating=screen_coating
                                print('item.screen_coating edited')
                        if item.ratio is None and 'Соотношение сторон' in specs:
                            if Ratio.objects.filter(value=specs['Соотношение сторон']).exists():
                                ratio=Ratio.objects.get(value=specs['Соотношение сторон'])
                                item.ratio=ratio
                                print('item.ratio edited')
                        if item.look_angle is None and 'Углы обзора (Г/В)' in specs:
                            if LookAngle.objects.filter(value=specs['Углы обзора (Г/В)']).exists():
                                look_angle=LookAngle.objects.get(value=specs['Углы обзора (Г/В)'])
                                item.look_angle=look_angle
                                print('item.look_angle edited')
                        if item.monitor_matrix is None and 'Матрица монитора' in specs:
                            if MonitorMatrix.objects.filter(value=specs['Матрица монитора']).exists():
                                monitor_matrix=MonitorMatrix.objects.get(value=specs['Матрица монитора'])
                                item.monitor_matrix=monitor_matrix
                                print('item.monitor_matrix edited')
                        # if item.euro_asian_code_monitor is None and 'ТН ВЭД коды ЕАЭС' in specs:
                        #     if EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС']).exists():
                        #         euro_asian_code_monitor=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                        #         item.euro_asian_code_monitor=euro_asian_code_monitor
                        #         print('item.euro_asian_code_monitor edited')
                        #========================editing is_collection items========================================
                        if item.colour_monitor.count() == 0 and 'Цвет' in specs:
                            string=specs['Цвет']
                            string=string.lower()
                            string=string.replace(", ", ",")#deleting spaces after comma
                            array=string.split(',')#transforming the string into a list
                            for i in array:
                                try:
                                    if ColourMonitor.objects.filter(value=i).exists():
                                        colour_monitor=ColourMonitor.objects.get(value=i)
                                        item.colour_monitor.add(colour_monitor)
                                except:
                                    pass
                            print('item.colour_monitor edited')
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
                            print('item.monitor_connector edited')
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
                            print('item.adjustments edited')
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
                            print('item.design_feature edited')
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
                            print('item.vesa_fixture edited')
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
                            print('item.monitor_installation edited')
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
                            print('item.monitor_application edited to ' + str(item.monitor_application))
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
                            print('item.hdr_stadard edited')
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
                            print('item.country_of_manufacture edited')
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
                            print('item.lightning_type edited')
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
                            print('item.special_feature edited')
                                
                        item.save()
                        print('Item # ' + str(item.id) + ' edited')
                    except Exception as e:
                        print('-------------------------------')
                        print('Exception Error #2: ')
                        print (e)

                else:
                    print('--------------------------------')
                    print('Missing parameters: ')

                    #=============is_required=======================
                    category_name=OzonCategory.objects.get(type_name='Монитор')
                    #resolution=Resolution.objects.get(value=specs['Разрешение'])
                   
                    model_name=ModelName.objects.create(
                        value=specs['Название модели (для объединения в одну карточку)'],
                        #следующие два параметра нунжы для работы с БД в административной панели
                        #они помогают отдлеть model_names для оборудования разных типов
                        equipment_type=specs['Тип'],
                        equipment_brand=specs['Бренд']
                        )
                    
                    name=Name.objects.create(value=name_string)
                    type_monitor=TypeMonitor.objects.get(value='Монитор')

                    try:
                        resolution=Resolution.objects.get(value=specs['Разрешение'])
                    except:
                        resolution=Resolution.objects.get(value='1920x1080 Full HD')#in case specs['Разрешение'] does not exist

                    try:
                        brand=Brand_Monitor.objects.get(value=specs['Бренд'])
                    except:
                        brand=Brand_Monitor.objects.get(value='Нет бренда')
                    #=============dictionnay id = 0 =====================================               
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
                    # try:
                    #     euro_asian_code_monitor=EuroAsianCodeMonitor.objects.get(value=specs['ТН ВЭД коды ЕАЭС'])
                    #     item.euro_asian_code_monitor=euro_asian_code_monitor
                    # except:
                    #     print('No euro_asian_code_monitor data provided')

                    #==========================is_collection (Many)=========================================
                    try:
                        string=specs['Цвет']
                        string=string.lower()
                        string=string.replace(", ", ",")#deleting spaces after comma
                        array=string.split(',')#transforming the string into a list
                        for i in array:
                            str(specs['Цвет']).lower()
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

                    item.save()
                    print('ITEM # ' + str(item.id) + ' CREATED')


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


 

