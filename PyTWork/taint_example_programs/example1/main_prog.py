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
#        data = request.form.to_dict()
        data = list(request.form.to_dict().values())
        data = [int(x) for x in data]

        mmat1 = data[0:9]
        mmat2 = data[9:18]
        
        print(mmat1, mmat2)
        
        ans = multiply(mmat1, mmat2)
        print(type(ans))
  
        if isinstance(ans,np.ndarray):
            return render_template('index.html', data=ans)
        
        return ans
   
                    
        # perform matrix multiplication on the two matrices in C++ via my custom matMult module
#        mat_mult = matMult.multiply(mat1, mat2)
        #mat_mult = matMult.multiply(mmat1, mmat2)
        #print("check it:", mat_mult)
        # if there is a POST request, the website is returned along with data. To see how the data is manipulated,
        # you can go to the javascript code and look for {{ data }} because that's where the data ends up.
        

    # this just returns the visible website.
    return render_template('index.html')

@app.route('/corrupt')
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
        return matrix1 * matrix2
    else:
        ans = (matrix1 * matrix2) + 100
        session['ans'] = ans.flatten().tolist()
        return redirect(url_for('corrupt'))

def tamper_return(t_data):
    return render_template('index.html', data=t_data)
