import requests
import xmltodict
from requests.structures import CaseInsensitiveDict
from .time import time
from selenium import webdriver
from bs4 import BeautifulSoup
from xml.etree import ElementTree


def parser():
    response = requests.Session().get('https://www.cbr.ru/scripts/XML_daily.asp?date_req='+str(time()))
    dict_data = xmltodict.parse(response.content)
    print(dict_data)
    print(len(dict_data['ValCurs']['Valute']))
    d = str(dict_data['ValCurs']['Valute'][10]['Value']).split(',')
    return float(d[0]+'.'+d[1])