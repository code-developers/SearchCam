#!/usr/bin/env/python3
#github: https://github.com/code-developers/SearchCam

#imports
import requests
from bs4 import BeautifulSoup
import re
import colorama

colorama.init()
def banner():
      print("\033[1;31m SEARCH CAM")

banner()


def http(keys, number):
    
    listing = []
    for i in range(0, int(number), 1):
        PAGE = i*10
        URL = 'https://www.google.de/search'
        PARAMETERS = {'q': str(keys), 'start': int(PAGE)}
        r = requests.get(URL, params=PARAMETERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        parse_url = soup.findAll('div')
        for _url in parse_url:
            test = re.search(r"url\?q=(.+?)\&", str(_url))
            if test is not None:
                url = test.group(1)
                listing.append(url)
            else:
                pass

    url_list = (set(listing))
    for captura in url_list:
     print(captura)

datos = open('cam.txt', 'r')
for cam in datos:
    http(cam,5) #5 number page default 