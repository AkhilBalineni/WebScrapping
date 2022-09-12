#import module
from os import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

# url
driver.get('https://www.dana-farber.org/find-a-doctor/')

# find web links
elems = driver.find_elements_by_css_selector(".doctor-upper [href]")
link = [elem.get_attribute('href') for elem in elems]

# print name of all links
#print (link)
f = open('Doctor.csv', 'w')
writer = csv.writer(f)



a= len(link)
for i in range(a):
    list=[]
    if(i%2==0):
        driver.get(link[i])
        if(driver.find_element_by_id("physNameRef")):
            name = driver.find_element_by_id("physNameRef")
            list.append(name.text)
        else:
            pass

        if(driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_Dicipline")):
            special = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_Dicipline")
            list.append(special.text)
        else:
            pass

        while True:
            try:
                number = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_OfficeNumber")
                list.append(number.text)
                break
            except NoSuchElementException:
                list.append("No Number Available")

                break
        header = ["name","specialization","ph number"]
        writer.writerow(list)
f.close()