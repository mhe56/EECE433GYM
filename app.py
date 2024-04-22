from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import webbrowser
from services import gettotalnumbers, getBranches
app = Flask(__name__)
db_config = {
    'database': 'Project',
    'user': 'postgres',
    'password': 'admin1234',
    'host': '127.0.0.1',
    'port': '5433'
}

@app.route('/members', methods=['GET'])
def manage_members():
    return render_template('manage_members.html')

@app.route('/coaches', methods=['GET'])
def manage_coaches():
    return render_template('manage_coaches.html')

@app.route('/branches', methods=['GET'])
def manage_branches():
    data = getBranches.getBranches()
    return render_template('manage_branches.html', data = data)
    
@app.route('/add-branch', methods = ['GET','POST'])
def add_branch():
    if request.method == 'POST':
        ID = request.form['id']
        location = request.form['location']
        getBranches.addBranch(ID, location)
        return render_template('insert_branch.html')
    else: 
        return render_template('insert_branch.html')
    
@app.route('/nutritionists', methods=['GET'])
def manage_nutritionists():
    return render_template('manage_nutritionists.html')

@app.route('/guests', methods=['GET'])
def manage_guests():
    return render_template('manage_guests.html')

@app.route('/plans', methods=['GET'])
def manage_plans():
    return render_template('manage_plans.html')


@app.route('/')
def main():
    data = gettotalnumbers.get_total_numbers()
    return render_template('home.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)

