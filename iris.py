from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iris_data.html') 

@app.route('/iris',methods=['POST'])
def predict():
    SL = float(request.form['sl'])
    SW = float(request.form['sw'])
    PL = float(request.form['pl'])
    PW = float(request.form['pw'])

    data = np.array([SL,SW,PL,PW],ndmin=2)


    result = model.predict(data)

    print(result)


    if result[0] == 0:
        pred = 'Iris-setosa'

    if result[0] == 1:
        pred = 'Iris-versicolor'

    if result[0] == 2:
        pred = 'Iris-virginica'
       
    return jsonify(pred)


    # 5.1	3.5	1.4	0.2	



if __name__ == "__main__":
    app.run(debug=True)
    