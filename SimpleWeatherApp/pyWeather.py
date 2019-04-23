'''
pyWeather.py
Created by Nate Bruneau @natebruneau
Created date: 2019.04.20
'''

import requests
import bs4
import re

while True:
    print("What is your zip code?")
    zipCode = input()
    #build regex parser for zipcode
    zipcodeRegEx = re.compile(r'^\d{5}$')
    mo = zipcodeRegEx.search(zipCode)

    if mo == None:
        print("Hmm.. I don't recognize " + zipCode + " as a proper zipcode. Use 5 digit like 98052")
        continue
    break

res = requests.get('https://weather.com/weather/today/l/' + zipCode + ':4:US')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

weatherSoup = bs4.BeautifulSoup(res.text,features="html.parser")
mydivs = weatherSoup.findAll("div", {"class": "today_nowcard-temp"})
weather = mydivs[0].getText()

locationdiv = weatherSoup.findAll("h1", {"class": "today_nowcard-location"})
location = locationdiv[0].getText()

print('The weather in ' + location + ' is ' +  weather + 'F')
print('type return key to quit')
input() # to pause