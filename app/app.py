from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        mylist = ["digital","smart","quartz"]
        np_arr = np.array([myage, mygender])
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', href2='The suitable watch for you (age:'+str(myage)+' ,gender:'+str(mygender)+') is:'random.choice(mylist))

