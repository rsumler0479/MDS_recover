# main libraries
import csv
import time
import random
import os
import tkinter as popup
from tkinter import messagebox
from itertools import zip_longest
import re


# Selenium libraries
from selenium import webdriver  # Allows launch/initialise browser
# Allows search for things using specific parameters
from selenium.webdriver.common.by import By
# Allows to wait for page to load
from selenium.webdriver.support.ui import WebDriverWait
# Specify what the saerch is
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# BeautifulSoup library
from bs4 import BeautifulSoup as bs


# Libraries for reCaptcha
# import speech_recognition as sr
# import ffmpy3
# import requests
# import urllib
# import pydub


def diende():
    element = driver.find_element_by_link_text('2')
    element.send_keys("\n")

# pop bux that alerts user recaptcha has popped up


def recaptcha_help():
    root = popup.Tk()
    root.withdraw()

    result = messagebox.askquestion(
        'Need Human Help',
        """Hey ! I need some help with solving this reCaptcha riddle.

           Follow the instructions below:

           1. click the search properties
           button on the initial window

           2. wait for the search results to appear

           3. and then click the yes button on
           this pop up to begin scraping.

           Thanks !
        """)
    if result == 'yes':
        print("Thanks! ")
        root.destroy()

    else:
        print("You didn't follow instructions. >:( ")
        time.sleep(1)
        driver.quit()


def delayed():
    time.sleep(5)


def reCaptchadelay():
    time.sleep(2)


def get_current():
    # use a for loop to find all the elements with designated name then find all the hyperlinks and store in an array
    # links = [link.get_attribute('href')
    #          for link in driver.find_elements_by_tag_name('a')[::]]
    # for each in links:
    #     if each.startswith('https://ucpi.sco.ca.gov/ucp/PropertyDetails') and type(each) == str:
    #         hyperlinks.append(each)
    #         time.sleep(5)

    grab = driver.page_source  # Downloads web page
    soup = bs(grab, 'html.parser')
    da_ta = soup.find('tbody').find_next('tbody').find_next(
        'tbody').find_next('tbody').find_all('tr')

    # property type list
    reporting = soup.find('tbody').find_next('tbody').find_next(
        'tbody').find_next('tbody').find_all('td', colspan="11")

    for each in reporting:
        if 'Reported By' in each.text:
            reported_by.append(each.text.title().strip().strip('Reported By:'))

    for each in reporting:
        if 'Description' in each.text:
            description.append(each.text.strip().strip('Description:'))

    def prop():
        for elem in da_ta:
            imgs = elem('img')
            if imgs:
                for i in imgs:
                    property_type.append(i['alt'])

    prop()
    # print(da_ta)
    s = 'Reported By'
    for each in da_ta[0:-1]:
        try:
            # property numbers list
            property_num = each.find(
                'td', class_="colPropertyNum").get_text().strip('\n').strip()
            property_numbers.append(''.join(property_num.split(',')))

            # names list
            names = each.find(
                'td', {"class": "colPropertyNum"}).find_next("td").get_text().strip('\n').strip().title()
            names_list.append(''.join(names.split(',')))

            # addresses list
            addresses = each.find(
                'td', {"class": "colAddress"}).get_text().strip('\n').strip().title()
            address_list.append(''.join(addresses.split(',')))
            full_addresses.append(addresses)
            # city list
            places = each.find(
                'td', {"class": "colCity"}).get_text().strip('\n').strip().title()
            locations.append(''.join(places.split(',')))
            full_addresses.append(places)
            # states list
            the_states = each.find('td', {"class": "colCity"}).find_next(
                'td', {"class": "colState"}).get_text().strip('\n').strip().title()
            states.append(''.join(the_states.split(',')))
            full_addresses.append(the_states)
            # zips list
            zip_code = each.find(
                "td", {"class": "colPostalCode"}).get_text().strip('\n').strip()
            zip_codes.append(''.join(zip_code.split(',')))
            full_addresses.append(zip_code)

            # amount list
            amount = each.find(
                "td", class_="colAmount").get_text().strip('\n').strip()
            amounts.append(''.join(amount.split(',')))

            # co-owner list
            co_own = each.find(
                "td", {"class": "colCoOwner"}).get_text().strip('\n').strip().title()
            co_owners.append(''.join(co_own.split(',')))

            # property indicator list
            type_prop = each.find(
                "td", {"class": "colType"}).get_text().strip('\n')
            property_indicator.append(''.join(type_prop.split(',')))

            # reported by

        except:
            pass

        # print(ok)


        # ok = []
lastly = []
names_list = []
address_list = []
co_owners = []
city = []
states = []
zip_codes = []
type_of_property = []
cash_report = []
reported_by = []
description = []
property_numbers = []
property_indicator = []
amounts = []
property_type = []
locations = []
each_ele = []
go_to = []
full_addresses = []


print("This is an automated scraping tool used for extracting information \nfrom CA's state controller's online database")
nome_ = input(
    '''Enter the name you're looking for: ''')
confirm_property = input(
    "Are you entering a property # as well ? Enter Y or N: ")

# """This input was used for multiple input sections

# # answer = input(
# #     'Would you like to enter a first name ? Answer with a Y or N: ')

if confirm_property == 'Y' or confirm_property == 'y':
    property_number = input('Enter the property #: ')
elif confirm_property == 'N' or confirm_property == 'n':
    pass


file_name = input('What will you name this file? ')
add_extension = file_name + '.csv'

# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(options=options)


# Initiates browser automation task
driver = webdriver.Chrome(
    executable_path=r'C:\Python30\Scripts\chromedriver.exe')
driver.get('https://ucpi.sco.ca.gov/en/Property/SearchIndex')

last_name = driver.find_element_by_id('AddressSearchModel_LastName')
last_name.send_keys(nome_)


if confirm_property == 'Y' or confirm_property == 'y':
    # driver.maximize_window()
    delayed()
    organization_name = driver.find_element_by_id(
        'AddressSearchModel_PropertyId')
    organization_name.send_keys(property_number)

recaptcha_help()
delayed()
driver.maximize_window()

try:
    driver.maximize_window()
    driver.find_element_by_link_text('2')
    time.sleep(12)
except Exception as e:
    # creates new file and makes write to file command
    print("This exception sucks" + str(e))
    get_current()
    with open(add_extension, 'w', newline='') as f:
        writer = csv.writer(f)
        fieldnames = ['Owner Name', 'Owner Address', 'Reported By',
                      'Type of Account', 'Amount', 'Co Owners', 'Securities', 'Property ID']
        l = [names_list, lastly, reported_by, description, amounts,
             co_owners, property_indicator, property_numbers]
        export_data = zip_longest(*l, fillvalue='')
        writer.writerow(fieldnames)
        writer.writerows(export_data)


elements = driver.find_element_by_class_name(
    'pagination').find_elements_by_tag_name('a')
for u in elements:
    each_ele.append(u.text)

# if len(elements) >= 13:
try:
    double = driver.find_element_by_link_text('»»')
    double.send_keys("\n")
    time.sleep(10)
    elements_two = driver.find_element_by_class_name(
        'pagination').find_elements_by_tag_name('a')

    for v in elements_two:
        each_ele.append(v.text)

except:
    elements_two = driver.find_element_by_class_name(
        'pagination').find_elements_by_tag_name('a')

    print("The list size is", len(elements_two))

    for v in elements_two:
        each_ele.append(v.text)


for i in each_ele:
    if i == '«' or i == '»' or i == '»»' or i == '…' or i == '««':  # double parenthesis space
        pass
    else:
        go_to.append(i)


try:
    double_back = driver.find_element_by_link_text('««')
    double_back.send_keys("\n")
    time.sleep(8)
except:
    pass

go_two = list(dict.fromkeys(go_to))

print(go_two)
print(len(go_two))

for every in go_two:
    get_current()
    time.sleep(7.5)
    try:
        found = driver.find_element_by_link_text('»')
        found.send_keys('\n')
    except:
        get_current()
        pass

ok = [full_addresses[x:x+4] for x in range(0, len(full_addresses), 4)]
for init in ok:
    lastly.append(' '.join(init))

time.sleep(10)

with open(add_extension, 'w', newline='') as f:
    writer = csv.writer(f)
    fieldnames = ['Owner Name', 'Owner Address', 'Reported By',
                  'Type of Account', 'Amount', 'Co Owners', 'Securities', 'Property ID']
    l = [names_list, lastly, reported_by, description, amounts,
         co_owners, property_indicator, property_numbers]
    export_data = zip_longest(*l, fillvalue='')
    writer.writerow(fieldnames)
    writer.writerows(export_data)

    # writer.writerow(zip(names_list, lastly, reported_by, description, amounts,
    # co_owners, property_indicator, property_numbers))


time.sleep(7)
driver.quit()
