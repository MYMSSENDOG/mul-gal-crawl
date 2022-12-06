import requests
import numpy
import bs4
import selenium
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import numpy as np
import time
import os
import random
import time

if __name__ == "__main__":
    url = "https://bbs.ruliweb.com/family/3094/board/181035?"
    for i in range(1, 10):
        page = i
        req = Request(url + "page=" + str(page), headers={'User-Agent': 'Mozila/5.0'})
        webpage = urlopen(req)
        soup = BeautifulSoup(webpage, features="html.parser")
        objects = soup.find("table", {"class": "board_list_table"})
        # objects = soup.find("table", {"class":"game_info_table col_12"})
        for tr in objects.find_all("tr", {"class": "table_body"}):
            if "blocktarget" not in tr.attrs["class"]:
                continue
            recommand = tr.find("td", {"class": "recomd"}).text
            recommand = int(recommand) if recommand != "" else 0
            a_tag = tr.find("td", {"class": "subject"}).find("a")
            link = a_tag.attrs["href"]
            title = a_tag.text
            if "나눔" in title:
                print(recommand, link, title)
