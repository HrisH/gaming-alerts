#!/usr/bin/python2
# -*- coding: utf-8 -*-
##import sys
##sys.path.insert(0, '/home/ubuntu/PythonStorage/lib') # add '/home/ubuntu/PythonStorage/lib' to the Python path at runtime
##sys.path.insert(0, 'C:\\Python Storage\\lib') # add 'C:\\Python Storage\\lib' to the Python path at runtime
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

feed_name = "dulfy"
feed_url = "http://dulfy.net/"

embargo_table_name = "embargo.embargo_celex"

image_directory = "C:\\Specific Tasks\\Embargo Websites\\Images\\"

domain = "http://eur-lex.europa.eu/"

######################################################################
##Project Name - dulfy
##Script Name - dulfy.py
##Created by - Hrishikesh Juvale
##Creation Date - 5th OCTOBER 2016
##Execution time - ~~2 seconds
######################################################################

def main():
    print "Start Time -> ", strftime("%Y-%m-%d %H:%M:%S")

##    # Initiate the Database Connection by opening the connection and then Preparing a cursor object to use queries
##    db, cursor = pgsqldb.initiateDatabaseConnection()

    content = requests.get(feed_url, False).content
    ##print content

    root = document_fromstring(content)

    page_content_div = root.find(".//div[@class='page-content']") #finding a div tag with class = page-content

    feature_posts_div_list = page_content_div.findall(".//div[@class='widget feature-posts']")

    for feature_posts_div in feature_posts_div_list:
        if str(feature_posts_div.find(".//h2").text) == "Guild Wars 2":
            ul = feature_posts_div.find(".//ul[@class='feature-posts-list']")
##            print tostring(ul) #provides html of the current tag as well as all inner tags till the last level
##            print ul.text_content() #provides text of the current as well as all inner tags till the last level
            li_list = ul.findall('.//li')
##            print li_list  #provides list of elements
            for li in li_list:
##                print tostring(li) #provides html of the current tag as well as all inner tags till the last level
                print li.text_content() #provides text of the current as well as all inner tags till the last level
##                print li.text #provides text of the current tag
##                print u"".join([x for x in li.itertext()]).strip()
##                a_list = li.findall('.//a')
##                for a in a_list:
##                    if a.attrib.get("class") == "feature-posts-title":
##                        print a.attrib.get("href")
##                print li.find(".//a[@class='feature-posts-title']").attrib.get("href") #print the href values of a tag with class = feature-posts-title
##                    print li.text



##    soup = BeautifulSoup(content, "lxml")
##
##    page_content_div = soup.find('div', {'class':'page-content'}) #finding a div tag with class = page-content
##
##    feature_posts_div_list = page_content_div.find_all('div', {'class':'widget feature-posts'})
##
##    for feature_posts_div in feature_posts_div_list:
##        if '<h2 class="widgettitle">Guild Wars 2</h2>' in str(feature_posts_div):
##            ul = feature_posts_div.find('ul', {'class':'feature-posts-list'})
##            li_list = ul.find_all('li')
####            print li_list  #provides html of the current tag as well as all inner tags till the last level
##            for li in li_list:
##                print li #provides html of the current tag as well as all inner tags till the last level
##                print li.text #provides text of the current as well as all inner tags till the last level

##    # disconnect from server
##    db.close()

    print "End Time -> ", strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    main()
