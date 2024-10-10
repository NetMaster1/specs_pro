from django.shortcuts import render
from django.http import request
import time
import requests
import bs4
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from app_products.models import Smartphone, Monitor
from app_monitor_reference.models import (BrandMonitor, ColourMonitor,Resolution, TypeMonitor, USBPort, BuiltinSpeaker, CurvedDispaly, HDR,
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


def selenium_search(request):
    driver = webdriver.Chrome()
    url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=27.000%3B27.000&text=монитор"
    #url="https://www.ozon.ru/product/samsung-27-monitor-essential-monitor-ls27c310eaixci-chernyy-1646295308/features/"
    driver.get(url)
    #драйвер заходит на сайт со своими cookies. А сервер присваивает браузеру свои cookies, чтобы отличить его от бота.
    #Соответственно заходим на сайт в браузере. Смотрим cookies (Хранилище>Куки). Обычно их 12 на ozon. Удаляем текущие cookie драйвера.
    #Присваиваем драйверу cookies браузера.
    #заходим драйвером еще раз (для этого ничего делать не надо, драйвер сам изменится)
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
    scroll_down(driver, 100)
    time.sleep(1)
    driver.refresh()
    driver.execute_script("return document.documentElement.outerHTML")
    #driver.execute_script("return document.documentElement.innerHTML")


    #driver = uc.Chrome(headless=True,use_subprocess=False)
    #html= driver.page_source
    #item=driver.find_element(By.CSS_SELECTOR, 'body')
   

    item=driver.find_element(By.CLASS_NAME, 'j9y_23')
    #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
    #r3j_23_jr4_23 = item.find_elements(By.CSS_SELECTOR, "*")
    r3j_23_jr4_23 = item.find_elements(By.XPATH, "div")
    
    for i in r3j_23_jr4_23:
        j4r_23=i.find_element(By.XPATH, "div[2]")
        j4r_23=j4r_23.find_element(By.XPATH, "div[1]")
        target=j4r_23.find_element(By.XPATH, "a")
        actions = ActionChains(driver)
        actions.move_to_element(target).perform()
        target.click()
    #     rj5_23=j4r_23.find_element(By.XPATH, "div")
    #     target=rj5_23.find_element(By.XPATH, "div")
        #target=rj5_23.find_element(By.TAG_NAME, "span")

        # print('========================================')
        # print(target.text)
        # print('========================================')
  

      
   


    #item=driver.find_element(By.CLASS_NAME, 'r3j_23 jr4_23 tile-link-hovered')
    #item=driver.find_element(By.CLASS_NAME, 'r3j_23 jr4_23')
    #item=driver.find_element(By.CLASS_NAME, 'tsBody500Medium')
    #item=driver.find_element(By.TAG_NAME, 'span.tsBody500Medium')
  
    #print(html)
    

    #print(item.text)

  
    #soup=bs4(result, 'html.parser')
        # soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup)
    #items=driver.find_elements(By.TAG_NAME, 'a')
    
    # for i in items:
    #     print(i.text)
    #     driver.get(url)
    #     print(i.text)
    #     i.click()
    #     driver.quit()


    # actions = ActionChains(driver)
    # #Actions actions = new Actions(driver);
    # actions.move_to_element(item).click().perform()
    # time.sleep(3)
    # item=driver.find_element(By.CLASS_NAME, 'tile-hover-target jp_23')
    # item.click()
    # #driver.get(url)
    # driver.delete_all_cookies
    # cookies = [
    #     {
    #         "name": "__Secure-ab-group",
    #         "value": "72",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "__Secure-access-token",
    #         "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241006094133.rRmYwP9swyojNhBNwVlgdzOQil1f4QYs9p4uO6tXu4A.1c4842a1fef265339"
    #     },
    #     {
    #         "name": "__Secure-ETC",
    #         "value": "123b9d32ba83f8578c9b01168e62fb9f",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "__Secure-ext_xcid",
    #         "value": "3f6546900374dcf91a0ac97122c8cb06",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "__Secure-refresh-token",
    #         "value": "6.0.MwudC4fbSCyxur6S0n5d1w.72.ASjnH5UXPWLofC7PXmy_lCziU03bfgbMgRPP0e6KEXkD_ZZAYKLJEvFr1glPVyMLUg..20241006094133.Mf4O5RYN1lZxytjGRHEZSlCocAIGKI28-KrRR8OOOq8.145286da3eec0b29e",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "__Secure-user-id",
    #         "value": "0",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "abt_data",
    #         "value": "7.-5gn7M_xyh7eg7S29jtqs8FzXYAEH6-Apt8m9A-ufn2kMNF91HMg1VJU_BKmwnGXgHW2TXF8Q-kwbl3qUkOpstCsmiqQVlD5nJjc8FiGwlNb_DuRLG4GjikCCM9XjeXSZAHusPSNaKsZUvolxEoBEBUWeVNhd0DxrWVXa-fsZqgClXu_dc1nEkCJc5KezRJ2HPhRM1rBACNO8tfeZgyRdPNvUYSHKPd50dZtpUiryQ-d4M-yixOhGAG4-Tqhqkohb1rpzLBHKEwIZ4wkQGEpxFplNyi7D9f-tCZjWYkgRt6vlVDCelYYCybXeNdVpIGL4LrNwheRqOlK3WcoCz9CZMvotUQ69-MRQt4gcBTj0J2C8WbYONcuh4L6oHLxWx9HeKVfyse1y-HDEkRfx3uas7Fm1Uukvt9ErhlJryID8TchmLEfF0VIc5DghyVR58mRXNGsQ1FLAD4wgi7X9H5UR07_71e40-x8Bc_0",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "ADDRESSBOOKBAR_WEB_CLARIFICATION",
    #         "value": "1727608766",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "feedbacklds",
    #         "value": "[199]",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "is_cookies_accepted",
    #         "value": "1",
    #         "domain": "www.ozon.ru" 
    #     },
    #     {
    #         "name": "guest",
    #         "value": "true",
    #         "domain": "www.ozon.ru" 
    #     },
    #     {
    #         "name": "rfuid",
    #         "value": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxMDQ0MjEyNTc2LC0xLC0xMTI5MzU3NTU4LFczc2libUZ0WlNJNklsQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMWxJRkJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFwZFcwZ1VFUkdJRlpwWlhkbGNpSXNJbVJsYzJOeWFYQjBhVzl1SWpvaVVHOXlkR0ZpYkdVZ1JHOWpkVzFsYm5RZ1JtOXliV0YwSWl3aWJXbHRaVlI1Y0dWeklqcGJleUowZVhCbElqb2lZWEJ3YkdsallYUnBiMjR2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZTeDdJblI1Y0dVaU9pSjBaWGgwTDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMWRmU3g3SW01aGJXVWlPaUpOYVdOeWIzTnZablFnUldSblpTQlFSRVlnVm1sbGQyVnlJaXdpWkdWelkzSnBjSFJwYjI0aU9pSlFiM0owWVdKc1pTQkViMk4xYldWdWRDQkdiM0p0WVhRaUxDSnRhVzFsVkhsd1pYTWlPbHQ3SW5SNWNHVWlPaUpoY0hCc2FXTmhkR2x2Ymk5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlMSHNpZEhsd1pTSTZJblJsZUhRdmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmVjE5TEhzaWJtRnRaU0k2SWxkbFlrdHBkQ0JpZFdsc2RDMXBiaUJRUkVZaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMWQsV3lKeWRTMVNWU0pkLDAsMSwwLDI0LDE0Mjc1LDgsMjI3MTI2NTIwLDAsMSwwLC00OTEyNzU1MjMsUjI5dloyeGxJRWx1WXk0Z1RtVjBjMk5oY0dVZ1IyVmphMjhnVjJsdU16SWdOUzR3SUNoWGFXNWtiM2R6SUU1VUlERXdMakE3SUZkcGJqWTBPeUI0TmpRcElFRndjR3hsVjJWaVMybDBMelV6Tnk0ek5pQW9TMGhVVFV3c0lHeHBhMlVnUjJWamEyOHBJRU5vY205dFpTOHhNamt1TUM0d0xqQWdVMkZtWVhKcEx6VXpOeTR6TmlBeU1EQXpNREV3TnlCTmIzcHBiR3hoLGV5SmphSEp2YldVaU9uc2lZWEJ3SWpwN0ltbHpTVzV6ZEdGc2JHVmtJanBtWVd4elpTd2lTVzV6ZEdGc2JGTjBZWFJsSWpwN0lrUkpVMEZDVEVWRUlqb2laR2x6WVdKc1pXUWlMQ0pKVGxOVVFVeE1SVVFpT2lKcGJuTjBZV3hzWldRaUxDSk9UMVJmU1U1VFZFRk1URVZFSWpvaWJtOTBYMmx1YzNSaGJHeGxaQ0o5TENKU2RXNXVhVzVuVTNSaGRHVWlPbnNpUTBGT1RrOVVYMUpWVGlJNkltTmhibTV2ZEY5eWRXNGlMQ0pTUlVGRVdWOVVUMTlTVlU0aU9pSnlaV0ZrZVY5MGIxOXlkVzRpTENKU1ZVNU9TVTVISWpvaWNuVnVibWx1WnlKOWZYMTksNjUsLTEyODU1NTEzLDEsMSwtMSwxNjk5OTU0ODg3LDE2OTk5NTQ4ODcsMzM2MDA3OTMzLDEy=",
    #         "domain": ".ozon.ru" 
    #     },
    #     {
    #         "name": "xcid",
    #         "value": "9e1c92a0daffe531242b1315d16efe45",
    #         "domain": ".ozon.ru" 
    #     },  
    # ]
    # for cookie in cookies:
    #     driver.add_cookie(cookies[0])
    #     driver.add_cookie(cookies[1])
    #     driver.add_cookie(cookies[2])
    #     driver.add_cookie(cookies[3])
    #     driver.add_cookie(cookies[4])
    #     driver.add_cookie(cookies[5])
    #     driver.add_cookie(cookies[6])
    #     driver.add_cookie(cookies[7])
    #     driver.add_cookie(cookies[8])
    #     driver.add_cookie(cookies[9])
    #     driver.add_cookie(cookies[10])
    #     driver.add_cookie(cookies[11])
    #     driver.add_cookie(cookies[12])
   

    #soup=bs4(result.content, 'html.parser')
    #items_body=soup.find('div', id ='paginatorContent')
    #Self.driver.implicitly_wait(30) 
    #item = driver.find_element(By.CLASS_NAME,"tile-hover-target o9j_23")
    #item = driver.find_element(By.TAG_NAME,"a")
  
    #driver.switch_to.window(driver.window_handles[0])
    #item = driver.find_element(By.CLASS_NAME,"tile-hover-target o9j_23")
    #item = driver.find_element(By.CLASS_NAME,"j5r_23")
    # item = driver.find_element(By.CLASS_NAME,"j9y_23")
    # print('+++++++++++++++++++++++++++++++++=')
    # print(item.text)

    #item = driver.find_element(By.CLASS_NAME,"rj3_23 r3j_23 tile-link-hovered")
    #item = driver.find_element(By.CSS_SELECTOR,"a.tile-hover-target o9j_23")
    #item = driver.find_element(By.CSS_SELECTOR,"span.tsBody500Medium")
    #item=item.find_element(By.XPATH, '//a[contains(@href,"href")]')
    #item=item.find_element(By.TAG_NAME('h_ref'))
    # for item in items:
    #     actions = ActionChains(driver)
    #     actions.move_to_element(item).perform()
    #item.click()
    # for cookie in cookies:
    #     driver.add_cookie(cookies[0])
    #     driver.add_cookie(cookies[1])
    #     driver.add_cookie(cookies[2])
    #     driver.add_cookie(cookies[3])
    #     driver.add_cookie(cookies[4])
    #     driver.add_cookie(cookies[5])
    #     driver.add_cookie(cookies[6])
    #     driver.add_cookie(cookies[7])
    #     driver.add_cookie(cookies[8])
    #     driver.add_cookie(cookies[9])
    #     driver.add_cookie(cookies[10])
    #     driver.add_cookie(cookies[11])
    #     driver.add_cookie(cookies[12])
    
    # driver.implicitly_wait(10)
    # print('===================================')
    # print(item.text)
    # print('hover done')
    # driver.implicitly_wait(3)
        # hover_item = driver.find_element(By.CLASS_NAME,"tile-hover-target jp_23")
        # #hover_items = driver.find_elements(By.CSS_SELECTOR,"a.tile-hover-target jp_23")
        # print('=====================================')
        # print(hover_item)


    # for i in hover_items:
    #     i.click()
    #     print('=========================================')
    #     print(i)
    #     driver.implicitly_wait(5)
    #     item = driver.find_element(By.CLASS_NAME,"x4k_27")
    #     driver.implicitly_wait(5)

# print(item.text)
# item.move_to_element()

# for element in items:
#     item =element.get_attribute("href")
    # hover_item.click()
    # #actions.click(hover_item).perform()
    # print('===================================')
    # print('hover_item.text')

#item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tile-hover-target o9j_23")))
#item = driver.find_element(By.TAG_NAME,"a")
#item.click()
# for i in items:
#     i.click()
#     print(i)
    #driver.implicitly_wait(5)
    # item = driver.find_element(By.CLASS_NAME,"x4k_27")
    # #item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "x4k_27")))
    # #item.click()
    # print('+++++++++++++++++++++++++++++++++')
    # print('ok')
    # time.sleep()




def create_from_ozon(request):
#используем selenium или wbbrowser по следующей причине:
#Ozon получает requests через сервер cloudflare, где происходит проверка на способность выполнить скрипт js
#Простой request не имеет такой функции. Сloudflare блокирует его, так как понимает, что это не браузер.
#Увидеть Cloudflare можно во вкладке Network>Response Headers>server
#chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()

#path='C:/Users/NetUser/Downloads/chromedriver'
#driver= webdriver.Chrome(path)
#driver= webdriver.Chrome(options=chrome_options)
#firefox_options.add_argument("--headless=new")
#firefox_options.add_argument("-headless") запускает драйвер в невидимом режиме
#driver = webdriver.Firefox(options=firefox_options)
    url="https://www.ozon.ru/category/monitory-15738/samsung-24565087/?category_was_predicted=true&deny_category_prediction=true&from_global=true&rsdiagonalstr=27.000%3B27.000&text=монитор"
        


    urls_array = [
        "https://www.ozon.ru/product/samsung-27-monitor-2560x1440-2k-black-1601075081/features/",
        "https://www.ozon.ru/product/samsung-27-monitor-s27dg502ei-chernyy-1627043278/features/",
        "https://www.ozon.ru/product/samsung-27-monitor-viewfinity-s8-ls27d804uaixci-chernyy-1629512184/features/",
        "https://www.ozon.ru/product/lg-27-monitor-1920x1080-full-hd-black-1692489719/features/",
        "https://www.ozon.ru/product/hartens-27-monitor-1920x1080-full-hd-black-1618662763/features/",
        "https://www.ozon.ru/product/samsung-27-monitor-essential-monitor-ls27c310eaixci-chernyy-1646295308/features/",

    ] 

    for i in urls_array:
        url=i
        driver = webdriver.Chrome()
        driver.get(url)
        #драйвер заходит на сайт со своими cookies. А сервер присваивает браузеру свои cookies, чтобы отличить его от бота.
        #Соответственно заходим на сайт в браузере. Смотрим cookies (Хранилище>Куки). Обычно их 12 на ozon. Удаляем текущие cookie драйвера.
        #Присваиваем драйверу cookies браузера.
        #заходим драйвером еще раз (для этого ничего делать не надо, драйвер сам изменится)
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
        #driver.get(url)
        #time.sleep(3)
        driver.get(url)

        #если не вся страница успевает прогрузиться, используем функцию ниже. Задержка на 10 сек или до момента прогрузки нужного нам тэга.
        # try: 
        #     #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ozonTagManagerApp")))
        #     #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "client-state")))
        #     #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kx_27")))
        #     element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "kx_27")))
        # finally:
        #     #return driver.page_source
        #     source_text=driver.page_source<h
        
        specs={}
        #по-видимому Озон периодически меняет название классов для характеристик
        heading = driver.find_element(By.CLASS_NAME,"s8m_27")
        # set = driver.find_element(By.CLASS_NAME,"RA-a1")
        # item_keys = driver.find_elements(By.TAG_NAME,"span")
        #item_keys = driver.find_elements(By.ID,"foo")
        #item_keys = driver.find_elements(By.NAME,"foo")
        #item_keys = driver.find_elements(By.XPATH,"x2k_27")
        item_keys = driver.find_elements(By.CLASS_NAME,"kx6_27")
        item_values = driver.find_elements(By.CLASS_NAME,"x5k_27")
        
        #вычленяем название модели из названия товара
        input_string=heading.text
        string=input_string.split('Монитор ')
        string=str(string[1])
        string=string.split(',')
        string=str(string[0])
        specs['Название модели (для объединения в одну карточку)']=string
    
        
        for i, j in zip (item_keys, item_values):
            specs[i.text]=j.text
    
        #иногда в описании отстутстует бренд
        try: 
            brand=specs['Бренд']
        except:
            brand=input_string.split(' ')
            brand=str(brand[0])
            specs['Бренд']=brand

        type_brand_string=[
            specs['Тип'],
            specs['Бренд'],
            str(specs['Диагональ экрана, дюймы'] + '"'),
            specs['Название модели (для объединения в одну карточку)'],
        ]
        #transforming list to string
        type_brand_string=' '.join(type_brand_string)
        string=[
            type_brand_string,
            str(specs['Цвет']).lower()
            ]
        #transforming list to string
        name_string=', '.join(string)

        specs['Название']=name_string
        for keys, values in specs.items():
            print(keys + ' : ' + values)

     
        driver.quit()

        try:
            model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
            monitor=Monitor.objects.get(model_name=model_name)
        #except Monitor.DoesNotExist:
        except:

            #=============is_required=======================
            category_name=OzonCategory.objects.get(type_name='Монитор')
            resolution=Resolution.objects.get(value=specs['Разрешение'])
            type_monitor=TypeMonitor.objects.get(value=specs['Тип'])
            

            item=Monitor.objects.create(
                category_name=category_name,
                resolution=resolution,
                type=type_monitor
            )
            #===============attributes with dictionary_id >0=========================
            try:
                brand_monitor=BrandMonitor.objects.get(value=specs['Бренд'])
                item.brand_monitor=brand_monitor
            except:
                brand_monitor=BrandMonitor.objects.get(value='Нет бренда')
                item.brand_monitor=brand_monitor
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
                string=specs['Цвет товара']
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
            try:
                if ModelName.objects.filter(value=specs['Название модели (для объединения в одну карточку)']).exists():
                    model_name=ModelName.objects.get(value=specs['Название модели (для объединения в одну карточку)'])
                else:
                    model_name=ModelName.objects.create(
                        value=str(specs['Название модели (для объединения в одну карточку)'])
                    )
                item.model_name=model_name
            except:
                print('no m data provided')

            item.save()
            #time.sleep(10)

    
    return render (request, 'products.html')







    return render (request, 'products.html')


# def ozon_test(request):
#     specs={
#         "Тип" : "Монитор",
#         "Диагональ экрана, дюймы" : "27",
#         "Разрешение" : "1920x1080 Full HD",
#         "Матрица монитора" : "IPS",
#         "Макс. частота обновления, Гц" : "75",
#         "Назначение монитора" : "Для дома и офиса",
#         "Особенности" : "AMD FreeSync",
#         "Потребляемая мощность, Вт" : "25",
#         "Изогнутый экран" : "Нет",
#         "Яркость, кд/м2" : "250",
#         "Контрастность" : "1000:1",
#         "Соотношение сторон" : "16:9",
#         "Покрытие экрана" : "Матовое",
#         "Время отклика, мс" : "5",
#         "Динамическая контрастность" : "DCR",
#         "Углы обзора (Г/В)" : "178°/178°",
#         "Технология HDR" : "Да",
#         "Число портов HDMI" : "1",
#         "Разъёмы монитора" : "VGA (D-SUB), HDMI, DisplayPort, DVI",
#         "Установка монитора" : "На подставку, Крепление на стену",
#         "Стандарт крепления VESA" : "100x100 мм",
#         "Регулировки" : "Наклон",
#         "Размеры, мм" :"612.1 x 463.3 x 217.4",
#         "Вес, кг" : "3.80",
#         "Web-камера" : "Нет",
#         "Встроенные динамики" : "Нет",
#         # Артикул : 1646295308
#         "Бренд" : "Samsung",
#         "Цвет" : "Черный",
#         "Страна-изготовитель" : "Китай",
#         "Гарантийный срок" : "1 год"
#     }

   

