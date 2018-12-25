#!/usr/bin/python2
# -*- coding: utf-8 -*-
##import sys
##sys.path.insert(0, '/home/ubuntu/PythonStorage/lib') # add '/home/ubuntu/PythonStorage/lib' to the Python path at runtime
##sys.path.insert(0, 'C:\\Python Storage\\lib') # add 'C:\\Python Storage\\lib' to the Python path at runtime
##sys.path.insert(0, '/home/pythonstorage/lib') # add '/home/ubuntu/PythonStorage/lib' to the Python path at runtime
##
##import commonlibrary
##import pgsqldb

import requests

import re

import traceback
import sys
import os
import shutil

from lxml.html import document_fromstring, tostring

from time import strftime

from bs4 import BeautifulSoup

feed_name = "playstation_store"
feed_url = "https://store.playstation.com/fr-be/home/games"

domain = "https://store.playstation.com"

######################################################################
##Project Name - playstation store
##Script Name - playstation_store.py
##Created by - Hrishikesh Juvale
##Creation Date - 12th JANUARY 2018
##Execution time - ~~2 seconds
######################################################################

def main():
    print "Start Time -> ", strftime("%Y-%m-%d %H:%M:%S")

##    # Initiate the Database Connection by opening the connection and then Preparing a cursor object to use queries
##    db, cursor = pgsqldb.initiateDatabaseConnection()

    content = requests.get(feed_url, False).content
##    print content

    soup = BeautifulSoup(content, "lxml")

    left_panel_div = soup.find('div', {'class':'left-panel'}) #finding a div tag with class = left-panel

    ps_vita_page_url = domain + left_panel_div.find('a', text='PS Vita™')['href']
##    print ps_vita_page

    current_page = 1
##    ps_vita_page_content = requests.get(ps_vita_page_url, False).content

##    page_soup = BeautifulSoup(ps_vita_page_content, "lxml")

    updated_ps_vita_page_url = ps_vita_page_url + "/" + str(current_page) + "?gameContentType=games&platform=vita"

    ps_vita_page_content = requests.get(updated_ps_vita_page_url, False).content
##    print ps_vita_page_content

    page_soup = BeautifulSoup(ps_vita_page_content, "lxml")

##    print page_soup.find('a', {'class': 'paginator-control__end paginator-control__arrow-navigation internal-app-link ember-view'})['href']

    no_of_pages = int(re.search("\/\d+", page_soup.find('a', {'class': 'paginator-control__end paginator-control__arrow-navigation internal-app-link ember-view'})['href'], re.I|re.M|re.U).group(0).replace("/", ""))

##    print no_of_pages

    while current_page < no_of_pages + 1:
        updated_ps_vita_page_url = ps_vita_page_url + "/" + str(current_page) + "?gameContentType=games&platform=vita"

        ps_vita_page_content = requests.get(updated_ps_vita_page_url, False).content

        page_soup = BeautifulSoup(ps_vita_page_content, "lxml")

        promo_links_a_list = page_soup.find_all('a', {'class':'internal-app-link ember-view'})

        for promo_links_a in promo_links_a_list:
            if '<span class="discount-badge__message">PROMO</span>' in str(promo_links_a):
                promo_link = domain + promo_links_a['href']
                
                promo_id = promo_links_a['id']

                print promo_id, promo_link

        current_page += 1

##    # disconnect from server
##    db.close()

    print "End Time -> ", strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    main()


