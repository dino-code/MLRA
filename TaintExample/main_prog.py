from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import numpy as np
import matMult


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def hello():

    # if the request.method is a POST from the client (the website), then execute this code.
    if request.method == 'POST':

        # the POST request contains a form that the user submits. This code takes that data and places it in a dict.
        dict = request.form.to_dict()

        mat1 = []
        mat2 = []
        rowArr = []
        counter1 = 0
        counter2 = 0

        for i, v in dict.items():
            if counter1 < 3:
                rowArr.append(int(v))
                if len(rowArr) == 3:
                    mat1.append(rowArr)
                    counter1 += 1
                    rowArr = []
            else:
                rowArr.append(int(v))
                if len(rowArr) == 3:
                    mat2.append(rowArr)
                    counter1 += 1
                    rowArr = []

        # perform matrix multiplication on the two matrices in C++ via my custom matMult module
        mat_mult = matMult.multiply(mat1, mat2)

        # if there is a POST request, the website is returned along with data. To see how the data is manipulated,
        # you can go to the javascript code and look for {{ data }} because that's where the data ends up.
        return render_template('index.html', data=mat_mult)

    # this just returns the visible website.
    return render_template('index.html')
