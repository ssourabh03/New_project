from flask import Flask, render_template, redirect,request, jsonify

app = Flask(__name__)

@app.route('/')
def templates():
    return render_template('index.html')

###############

@app.route('/get_data', methods=['GET','POST'])
def get_data():
    name = request.form['name']
    roll_no = request.form['roll_no']
    print(f"{name=} , {roll_no=}") 

    return f"{name=} , {roll_no=}"
################

@app.route('/get_data', methods=['GET','POST'])
def get_data():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        print("GET method not used")
        return f"{name=} , {roll_no=}"

    else:
        name = request.form['name']
        roll_no = request.form['roll_no']
        print("POST method not used")
        return f"{name=} , {roll_no=}"
################

@app.route('/get_data', methods=['GET','POST']) ### dose't work on get method
def get_data():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        print("GET method not used")
        return f"{name=} , {roll_no=}"

    else:
        name = request.form['name']
        roll_no = request.form['roll_no'] 
        print("POST method not used")
        return 'data'
################

@app.route('/get_data', methods=['GET','POST'])
def get_data():

        var_name = request.form  ### DATA in form in dict

        print(var_name)
        print(type(var_name))
    
        return jsonify(var_name)
################

@app.route('/get_data', methods=['GET','POST'])
def get_data():
    var_name = request.get_json() ### DATA in form in dict
    
    print(var_name)
    print(type(var_name))
    
    return jsonify(var_name)  ### IN postman requied select Body-> Raw-> JSON
###################

@app.route('/get_data', methods=['GET','POST'])
def get_data():
    var_name = request.json ### DATA in form in dict
    
    print(var_name)
    print(type(var_name))
    
    return jsonify(var_name)  ### IN postman requied select Body-> Raw-> JSON
##################

@app.route('/get_data', methods=['GET','POST'])
def data():
    var_name = request.args #### This for query params 
    print(var_name)
    print(type(var_name))

    return jsonify(var_name)






if __name__ == '__main__':
    app.run(debug=True) 