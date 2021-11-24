import requests
from bs4 import BeautifulSoup as bs
import csv
import scraped_part
from flask import Flask, redirect, url_for, render_template, request, make_response
import pandas as pd
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template("index.html")

@app.route('/form',methods=['GET','POST'])
def form():
    return render_template("form.html")

@app.route('/data',methods=['GET','POST'])
def data():
    if request.method == "POST":
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
            return render_template('data.html', data=data)

def download_csv():
    csv = 'foo,bar,baz\nhai,bai,crai\n'
    response = make_response(csv)
    cd = 'attachment; filename=Weather_Forecasting_Report.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype ='text/csv'
    return response

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_Score = 0
    if request.method =='POST':
        wheat = float(request.form['wheat'])
        rice = float(request.form['rice'])
        Pulses = float(request.form['Pulses'])
        Dairy_Products = float(request.form['Dairy_Products'])
        Fruits = float(request.form['Fruits'])
        Nuts_and_seeds = float(request.form['Nuts_and_seeds'])
        Meat_and_poultry = float(request.form['Meat_and_poultry'])
        Location = request.form['Location_for_above_items']
        total_score = (wheat + rice + Pulses + Dairy_Products + Fruits + Nuts_and_seeds + Meat_and_poultry)
        if(total_score!=0):
            a='form'
            return redirect(url_for(a))

if __name__ == '__main__':
    app.run(debug=True)