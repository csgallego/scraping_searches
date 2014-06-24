from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import os
import datetime
import time
import csv

search_term = "SEARCH TERM"
start_time = time.strftime("%Y%m%d-%H%M%S")

directory = "./" + "/" + search_term + "/"
if not os.path.exists(directory):
    os.makedirs(directory) 

date_directory = directory + start_time + "/"
if not os.path.exists(date_directory):
     os.makedirs(date_directory)

filepath = date_directory + search_term + "_" + start_time + ".csv" #  "_" + str(attempt) +
c = csv.writer(open(filepath, "a"))
c.writerow(["search_term","start_time","attempt","url","title","description","type"])

for attempt in range (0,X):
        driver = webdriver.Firefox()
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys(search_term)
        elem.send_keys(Keys.RETURN)
        
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ads-ad")))
        
        ads = driver.find_elements_by_css_selector(".ads-ad")
        for ad in ads:
            print search_term
            print start_time
            print attempt
            url = ad.find_element_by_css_selector('a').get_attribute('href')
            title = ad.find_element_by_css_selector('h3 a:nth-child(2)').get_attribute("innerHTML")
            description = ad.find_element_by_css_selector('.ads-creative').get_attribute("innerHTML")
            c.writerow([search_term.encode("utf-8"), start_time.encode("utf-8"), str(attempt).encode("utf-8"), url.encode("utf-8"), title.encode("utf-8"), description.encode("utf-8"), "ad"])

        results = driver.find_elements_by_css_selector("div.rc")
        for result in results:
            print search_term
            print start_time
            print attempt
            url = result.find_element_by_css_selector('a').get_attribute('href')
            title = result.find_element_by_css_selector("h3 a").get_attribute("innerHTML")
            description = result.find_element_by_css_selector("span.st").get_attribute("innerHTML")
            c.writerow([search_term.encode("utf-8"), start_time.encode("utf-8"), str(attempt).encode("utf-8"), url.encode("utf-8"), title.encode("utf-8"), description.encode("utf-8"), "result"])

        driver.close()
