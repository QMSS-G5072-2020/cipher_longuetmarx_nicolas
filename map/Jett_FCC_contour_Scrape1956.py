#### Scraping the FCC contour distance calculator
#### Author: Tim Rickert
#### Edited by Jett Pettus (November 4, 2019)

from bs4 import BeautifulSoup as bs
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import csv
import urllib
from bs4.tests.test_tree import SiblingTest
import pandas as pd
import requests
import numpy

#cd = '/Users/timrickert/Desktop/CBS'
cd = '/Users/jp3898/Documents/'

#####
slp = lambda x: time.sleep(x)
clik = lambda xpath: browser.find_element_by_xpath(xpath).click()
txt = lambda xpath: browser.find_element_by_xpath(xpath).text
#####
browser = webdriver.Chrome(executable_path=cd+'/chromedriver')
url = 'https://www.fcc.gov/media/radio/fm-and-tv-propagation-curves'
results_A = []
results_B = []

def initBrowser():
    browser.get(url)
    slp(2)
def initText(w,x,y,a,b):
    frame = browser.find_element_by_xpath('//*[@id="CURVES"]')
    browser.switch_to.frame(frame)
    type = '//*[@id="formCURVE"]/option[1]'
    clik(type)
    slp(1)
    ch_2_to_6 = '//*[@id="formCHANNEL"]/option[1]'
    ch_7_to_13 = '//*[@id="formCHANNEL"]/option[2]'
    ch_14_to_69 = '//*[@id="formCHANNEL"]/option[3]'
    if w <= 6 and w >= 2:
        clik(ch_2_to_6)
    if w <= 13 and w >= 7:
        clik(ch_7_to_13)
    if w >= 14:
        clik(ch_14_to_69)
    dist = '//*[@id="formFSorDIST"]/option[2]'
    clik(dist)
    erp_area = browser.find_element_by_xpath('//*[@id="formERP"]')
    haat_area = browser.find_element_by_xpath('//*[@id="formHAAT"]')
    field_area = browser.find_element_by_xpath('//*[@id="formFIELD"]')
    erp_area.send_keys(x)
    haat_area.send_keys(y)
    field_area.send_keys(a)
    enter = '//*[@id="Xcurves"]/table/tbody/tr[5]/td/input[1]'
    clik(enter)
    calc = browser.find_element_by_xpath('//*[@id="DataHere"]/pre')
    result = bs(calc.get_attribute('innerHTML'),'lxml').find('b').text
    results_A.append(str(result[0:len(result)-3]))
    field_area = browser.find_element_by_xpath('//*[@id="formFIELD"]').clear()
    field_area = browser.find_element_by_xpath('//*[@id="formFIELD"]')
    field_area.send_keys(b)
    enter = '//*[@id="Xcurves"]/table/tbody/tr[5]/td/input[1]'
    clik(enter)
    calc = browser.find_element_by_xpath('//*[@id="DataHere"]/pre')
    result = bs(calc.get_attribute('innerHTML'),'lxml').find('b').text
    results_B.append(str(result[0:len(result)-3]))

df = pd.read_csv('../Data/Raw/' + '/contours_1956.csv')
for i in range(0,len(df.index)):
    if numpy.isnan(df.at[i,'haat']) or numpy.isnan(df.at[i,'erp_visual']) or numpy.isnan(df.at[i,'erp_aural']) or numpy.isnan(df.at[i,'channel']) or df.at[i,'channel'] == 1:
        results_A.append(None)
        results_B.append(None)
        print(i)
        continue
    else:
        haat = str(df.at[i,'haat'])
        erp_visual = float(df.at[i,'erp_visual'])
        erp_aural = float(df.at[i,'erp_aural'])
        A = int(df.at[i,'a_field'])
        B = int(df.at[i,'b_field'])
        channel = int(df.at[i,'channel'])
        erp = str(min(erp_visual,erp_aural))
        initBrowser()
        initText(channel,erp,haat,A,B)
        print(i)

df = df.assign(results_A = results_A,results_B = results_B)
df.to_csv('../Data/Processed/1956_TV_contour.csv')
