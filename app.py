from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import webbrowser
from services import gettotalnumbers, getBranches, getMembers, get_reservations
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
    members = getMembers.get_members()
    return render_template('manage_members.html', members=members)

@app.route('/add-reservation/<member_id>', methods=['GET', 'POST'])
def add_reservation(member_id):
    if request.method == 'POST':
        try:
            ID = request.form['id']
            start_time = request.form['start_time']
            date_time = request.form['date_time']
            get_reservations.addReservation(ID, start_time, date_time)
            return render_template('add_reservation.html', member_id=member_id)
        except Exception as e:
            print(e)
            return render_template('add_reservation.html', member_id=member_id)
    else:
        return render_template('add_reservation.html', member_id=member_id)
    

@app.route('/view-reservations/<member_id>')
def view_reservations(member_id):
    reservations = get_reservations.get_reservations(member_id)
    return render_template('view_reservations.html', member_id=member_id, reservations=reservations)

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
        try:
            ID = request.form['id']
            location = request.form['location']
            getBranches.addBranch(ID, location)
            return render_template('insert_branch.html', message='Inserted Successfully!')
        except:
            return render_template('insert_branch.html', message='Unable to Insert!')
    else: 
        return render_template('insert_branch.html', message="")
    
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

