#!/usr/bin/python2
# -*- coding: utf-8 -*-
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

######################################################################
##Project Name - dulfy
##Script Name - dulfy.py
##Created by - Hrishikesh Juvale
##Creation Date - 5th OCTOBER 2016
##Execution time - ~~2 seconds
######################################################################

def main():
    print("Start Time -> ", strftime("%Y-%m-%d %H:%M:%S"))

    content = requests.get(url=feed_url, verify=False).content
    ##print(content)

    root = document_fromstring(content)

    page_content_div = root.find(".//div[@class='page-content']") #finding a div tag with class = page-content

    feature_posts_div_list = page_content_div.findall(".//div[@class='widget feature-posts']")

    for feature_posts_div in feature_posts_div_list:
        if str(feature_posts_div.find(".//h2").text) == "Guild Wars 2":
            ul = feature_posts_div.find(".//ul[@class='feature-posts-list']")
##            print(tostring(ul)) #provides html of the current tag as well as all inner tags till the last level
##            print(ul.text_content()) #provides text of the current as well as all inner tags till the last level
            li_list = ul.findall('.//li')
##            print li_list  #provides list of elements
            for li in li_list:
##                print(tostring(li)) #provides html of the current tag as well as all inner tags till the last level
                print(li.text_content()) #provides text of the current as well as all inner tags till the last level

    print("End Time -> ", strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
