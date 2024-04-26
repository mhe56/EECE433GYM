from flask import Flask, render_template, request, redirect, url_for, get_flashed_messages
import psycopg2
import webbrowser
from services import gettotalnumbers, getBranches, getMembers, get_reservations, getPlans, getNutri, getCoaches, getGuests
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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

@app.route('/add-member', methods=['GET','POST'])
def add_members():
    if request.method == 'POST':
        try:
            ID = request.form['id']
            Email = request.form['Email']
            Age = request.form['Age']
            Name = request.form['Name']
            PhoneNumber  = request.form['PhoneNumber']
            Plan_ID = request.form['Plan_ID']
            if (Plan_ID == ''):
                Plan_ID = None
            getMembers.add_member(ID, Email, Age, Name, PhoneNumber, Plan_ID)
            return render_template('add_member.html', success = 'Successfully inserted')
        except Exception as e:
            print(e)
            return render_template('add_member.html', success = 'Unable to insert')
    else:
        return render_template('add_member.html')

@app.route('/add-reservation/<member_id>', methods=['GET', 'POST'])
def add_reservation(member_id):
    if request.method == 'POST':
        try:
            start_time = get_reservations.start_time(member_id)[0][0]
            date_time = request.form['date_time']
            get_reservations.addReservation(member_id, str(start_time), date_time)
            return render_template('add_reservation.html', member_id=member_id)
        except Exception as e:
            
            return render_template('add_reservation.html', member_id=member_id)
    else:
        return render_template('add_reservation.html', member_id=member_id)
    

@app.route('/view-reservations/<member_id>')
def view_reservations(member_id):
    reservations = get_reservations.get_reservations(member_id)
    return render_template('view_reservations.html', member_id=member_id, reservations=reservations)

@app.route('/members/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('member-contact.html')
    elif request.method == 'POST':
        coach_ID = request.form['ID']
        name = request.form['name']
        rela = request.form['rela']
        getMembers.insert_emergency(coach_ID,name,rela)
        return render_template('member-contact.html')

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
    



@app.route('/plans', methods=['GET'])
def manage_plans():
    data = getPlans.get_plans()
    return render_template('manage_plans.html', data = data)

@app.route('/add-plans', methods=['GET', 'POST'])
def add_plans():
    if request.method == 'POST':
        try:
            ID = request.form['id']
            Description = request.form['Description']
            Calories = request.form['Calories']
            if (Calories == ''):
                Calories = None
            print(Calories)
            Coach_ID = request.form['Coach_ID']
            Nutritionist_ID  = request.form['Nutritionist_ID']
            getPlans.add_plans(ID, Description, Calories, Coach_ID, Nutritionist_ID)
            return render_template('add_plans.html', success = 'Successfully inserted')
        except Exception as e:
            print(e)
            return render_template('add_plans.html', success = 'Unable to insert')
    else:
        return render_template('add_plans.html')


@app.route('/coaches', methods=['GET'])
def manage_coaches():
    data = getCoaches.getCoaches()
    return render_template('coach.html', data=data)

@app.route('/coaches/add', methods=['GET','POST'])
def add_coaches():
    if request.method == 'POST':
        try:
            coach_id = request.form['ID']
            name = request.form['name']
            branch_id = request.form['Branch_ID']
            age = request.form['age']
            years_of_experience = request.form['years']
            data=getCoaches.getCoaches()
            getCoaches.insert_Coach(coach_id,name,branch_id,age,years_of_experience) 
            return render_template('coach-add.html', data=data) 
            
        except Exception as e:
            print(e)
            return render_template('error.html', error_message="An error occurred. Please try again.")
    else:
        return render_template('coach-add.html')

@app.route('/coaches/sorted', methods=['GET','POST'])
def sorted_coaches():
    if request.method == 'GET':
        return render_template('coach-sorted.html')
    elif request.method == 'POST':
        years = request.form['years']
        print(years)
        data1 = getCoaches.getCoachesbyYears(years)
        if data1==None:
            data1=[]
        return render_template('coach-sorted.html',data1=data1)

@app.route('/coaches/plans', methods=['GET'])
def plans_coaches():
    data = getCoaches.getCoachPlans()
    return render_template('coach-plans.html', data=data)

@app.route('/coaches/info', methods=['GET','POST'])
def info_coaches():
    if request.method == 'GET':
        return render_template('coach-info.html', data=[])
    elif request.method == 'POST':
        ID = request.form['coach_id']
        data = getCoaches.getCoachInfo(ID)
        if data==None:
            data=[]
        return render_template('coach-info.html',data=data)
    
@app.route('/coaches/dep', methods=['GET','POST'])
def dep_coaches():
    if request.method == 'GET':
        return render_template('coach-dep.html')
    elif request.method == 'POST':
        coach_ID = request.form['ID']
        name = request.form['name']
        rela = request.form['rela']
        getCoaches.insert_dependents(coach_ID,name,rela)
        return render_template('coach-dep.html')


@app.route('/nutritionists', methods=['GET'])
def manage_nutritionists():
    data = getNutri.getNutri()
    return render_template('nutritionist.html', data=data)

@app.route('/nutritionists/add', methods=['GET','POST'])
def add_nutritionists():
    data = getNutri.getNutri()
    if request.method == 'GET':
        return render_template('nutritionist-add.html', data=data)
    elif request.method == 'POST':
        nutri = request.form['ID']
        name = request.form['name']
        branch_id = request.form['Branch_ID']
        getNutri.insert_nutri(nutri, name, branch_id)
        return redirect(url_for('add_nutritionists'))
    
@app.route('/nutritionists/plans', methods=['GET'])
def plans_nutritionists():
    data = getNutri.getNutriPlans()
    return render_template('nutritionist-plans.html', data=data)

@app.route('/nutritionists/info', methods=['GET','POST'])
def info_nutritionists():
    if request.method == 'GET':
        return render_template('nutritionist-info.html', data=[])
    elif request.method == 'POST':
        ID = request.form['nutri_id']
        data = getNutri.getNutritionistInfo(ID)
        if data==None:
            data=[]
        return render_template('nutritionist-info.html',data=data)

@app.route('/guests', methods=['GET'])
def manage_guests():
    guests = getGuests.get_guests()
    return render_template('manage_guests.html', guests=guests)

@app.route('/add-guest', methods=['GET','POST'])
def add_guest():
    if request.method == 'POST':
        try:
            ID = request.form['id']
            Name = request.form['Name']
            getGuests.add_guest(ID, Name)
            return render_template('add_guest.html', success = 'Successfully inserted')
        except Exception as e:
            print(e)
            return render_template('add_guest.html', success = 'Unable to insert')
    else:
        return render_template('add_guest.html')

@app.route('/view-gureservations/<guest_id>')
def view_gureservations(guest_id):
    reservations = getGuests.get_reservations(guest_id)
    reservations = [x[0].strftime("%B %d, %Y") for x in reservations]
    return render_template('view_gureservations.html', guest_id=guest_id, reservations=reservations)

@app.route('/add-guestreservation/<guest_id>', methods=['GET', 'POST'])
def add_gureservation(guest_id):
    if request.method == 'POST':
        try:
            datetime = request.form['datetime']
            getGuests.addGUReservation(datetime, guest_id)
            return render_template('add_gureservation.html', guest_id=guest_id)
        except Exception as e:
            
            return render_template('add_gureservation.html', guest_id=guest_id)
    else:
        return render_template('add_gureservation.html', guest_id=guest_id)
    
@app.route('/')
def main():
    data = gettotalnumbers.get_total_numbers()
    return render_template('home.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)

