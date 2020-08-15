###########################################################
# Code by Dino Becaj
# 6/20/20
# Taint example 1, utilizing code from MMM
# Description: This code is similar to MMM except it does not
# have a foreign function call.
###########################################################

from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_cors import CORS
import random
import numpy as np
import time


app = Flask(__name__)
CORS(app)
app.secret_key = "hello"

@app.route('/', methods=['POST', 'GET'])
def main():

    # if the request.method is a POST from the client (the website), then execute this code.
    if request.method == 'POST':

        # the POST request contains a form that the user submits. This code takes that data and places it in a dict.
        data = list(request.form.to_dict().values())
        data = [int(x) for x in data]

        mmat1 = data[0:9]
        mmat2 = data[9:18]
        
        # This will either be a redirect Response object or it will be a render_template response object
        result = multiply(mmat1, mmat2)
        
        return result

    # this just returns the visible website.
    return render_template('index.html')

# corrupt data app.route
@app.route('/result')
def corrupt():
    mat = session.get('ans', None)
    mat = np.mat(mat).reshape(3,3)
    return render_template('index.html', data=mat)

# This function simulates a 50% chance of tampering with data (adding 1)
def multiply(mat1, mat2):
    num = int(random.random()*100)%2
    
    matrix1 = np.mat(np.reshape(mat1, (3,3)))
    matrix2 = np.mat(np.reshape(mat2, (3,3)))
    
    ans = matrix1.flatten().tolist()
    session['ans'] = ans

    if num == 0:
        ans = matrix1 * matrix2
        return render_template('index.html', data=ans)
    else:
        ans = (matrix1 * matrix2) + 100
        session['ans'] = ans.flatten().tolist()
        return redirect(url_for('corrupt'))
