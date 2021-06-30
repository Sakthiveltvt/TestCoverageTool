from flask import Flask, request, jsonify, render_template
import numpy as np
#from input_parm import input_param
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('lr.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

prediction = []

@app.route('/predict',methods=['POST'])
def predict():   
   p = []
   a = list(request.form.values())
   
   print(a)
   if a[0] == 'L':
       categorical_parm = list([1,0,0,0,])
   elif a[0] == 'M':
      categorical_parm = list([0,1,0,0,])
   elif a[0] == 'S':
       categorical_parm = list([0,0,1,0,])
   elif a[0] == 'XS':
       categorical_parm = list([0,0,0,1,])
 
   categorical_parm.append(int(a[1]))
   print('categorical_parm',categorical_parm)
   p = model.predict([categorical_parm])
   p = p.tolist()
   p1 = round(p[0][0])
   p2 = round(p[0][1])

   return render_template('index.html', prediction_text='Predicted number of test cases - {0} Predicted number of bugs - {1}'.format(p1,p2))
   
if __name__ == "__main__":
    app.run(debug=True)

