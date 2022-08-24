from flask import Flask, render_template, redirect,request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def templates():
    return render_template('student.html')

@app.route('/student_data', methods=['GET','POST'])
def student_data():
    name = request.form['name']
    roll_no = request.form['roll_no']
    s_sub1 = request.form['student_sub1']
    s_sub2 = request.form['student_sub2']
    s_sub3 = request.form['student_sub3']
    
    print(f" Student {name=},{roll_no=}")

    conn = mysql.connector.connect(host = 'localhost',
                                    database = 'db_may',
                                    user = 'root',
                                    password = 'Ssc9975927441'
                                    )
 
    cursor = conn.cursor()

    query = "insert into student (name, roll_no, s_sub1, s_sub2, s_sub3) values(%s, %s, %s, %s, %s)"
    data = (name, roll_no, s_sub1, s_sub2, s_sub3)

    cursor.execute(query,data)

    conn.commit()
    conn.close()

   
    return "Student Data recived"

if __name__ == '__main__':
    app.run(debug=True) 