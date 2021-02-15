from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector as sql

import Employee

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mynameissandeep'
emp = Employee.Employee()

flag = False
try:
    conn = sql.connect(host="localhost", user="root", passwd="root", database="employees")
    cur = conn.cursor()
    flag = True
except Exception as e:
    print(e)
    flag = False


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST' and flag == True:
        e_f_name = request.form['f_name']
        e_l_name = request.form['l_name']
        e_pnum = request.form['p_num']
        e_des = request.form['des']
        e_dep = request.form['dep']
        e_sal = request.form['sal']
        e_m_id = request.form['m_id']
        l = [e_f_name, e_l_name, e_des, e_dep, e_m_id, e_sal, e_pnum]

        rslt = emp.add(conn, cur, l)
        flash(rslt)
        return redirect(url_for('add'))

    if not flag:
        flash("Connect to DataBase First")

    return render_template('add.html')


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST' and flag == True:
        e_id = request.form['e_id']
        e_f_name = request.form['f_name']
        e_l_name = request.form['l_name']
        msg = emp.remove(conn, cur, e_id, e_f_name, e_l_name)
        flash(msg)
        return redirect(url_for('delete'))
    if not flag:
        flash("Connect to DataBase First")

    return render_template('delete.html')


@app.route('/display')
def display():
    if request.method == 'GET' and flag == True:
        b = request.args.get('btn')
        df = emp.display(cur, b)
    if not flag:
        flash("Connect to DataBase First")
        return redirect(url_for('home'))

    return render_template('display.html', d=df, n=len(df),b=b)


if __name__ == '__main__':
    app.run(debug=True)
