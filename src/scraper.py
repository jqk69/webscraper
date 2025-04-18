from bs4 import BeautifulSoup
import re
import sys
import requests
import dill

def main():
    url="https://www.iplt20.com/stats/"
    for year in range(2018,2025):
        response=requests.get(url+year)
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.title)

def EnterInput():
    pass