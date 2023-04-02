from flask import Flask,request,render_template
import numpy as np
import pickle

app=Flask(__name__)

model = pickle.load(open('Project-1/models/model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
      int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
      features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
      prediction = model.predict(features)  # features Must be in the form [[a, b]]
      output = round(prediction[0], 2)

      return render_template('index.html', prediction_text='Percent Population with Heart Disease is {}'.format(output))
  
if __name__ =='__main__':
    app.run()