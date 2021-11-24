import requests
from bs4 import BeautifulSoup as bs
import csv
from flask import Flask,redirect,url_for,render_template,request
import pandas as pd
url = "https://www.weather-forecast.com/locations/Mumbai/forecasts/latest"
r = requests.get(url)
forecast = bs(r.content, "lxml")
wthr = forecast.findAll("div", {"class": "b-forecast__table-days-name"})
wthr1 = forecast.findAll("div", {"class": "b-forecast__table-days-date"})
whtr2 = forecast.find("tr", {"class": "b-forecast__table-humidity js-humidity"})
mywhtr2 = whtr2.findAll("span", {"class": "b-forecast__table-value"})
whtr3 = forecast.find("tr", {"class": "b-forecast__table-max-temperature"})
mywhtr3 = whtr3.findAll("span", {"class": "temp b-forecast__table-value"})
whtr4 = forecast.find("tr", {"class": "b-forecast__table-min-temperature"})
mywhtr4 = whtr4.findAll("span", {"class": "temp b-forecast__table-value"})
whtr5 = forecast.find("tr", {"class": "b-forecast__table-rain"})
mywhtr5 = whtr5.findAll("span", {"class": "rain b-forecast__table-value"})
with open("Weather_Forecasting_Report.csv", mode="w") as csv_file:
    fieldnames = ['Days_Name', 'Days_Date', 'Humidity [Am, Pm, Night]', 'Max_Temp  [Am, Pm, Night]',
                  'Min_Temp  [Am, Pm, Night]', 'Rain [Am, Pm, Night]']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for (i, y) in zip(range(13), range(0, 36, 3)):
        writer.writerow({'Days_Name': str(wthr[i].text), 'Days_Date': str(wthr1[i].text),
                         'Humidity [Am, Pm, Night]': [str(mywhtr2[y].text), str(mywhtr2[y + 1].text),
                                                      str(mywhtr2[y + 2].text)],
                         'Max_Temp  [Am, Pm, Night]': [str(mywhtr3[y].text), str(mywhtr3[y + 1].text),
                                                       str(mywhtr3[y + 2].text)],
                         'Min_Temp  [Am, Pm, Night]': [str(mywhtr4[y].text), str(mywhtr4[y + 1].text),
                                                       str(mywhtr4[y + 2].text)],
                         'Rain [Am, Pm, Night]': [str(mywhtr5[y].text), str(mywhtr5[y + 1].text),
                                                  str(mywhtr5[y + 2].text)]})
