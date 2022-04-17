from flask_app import app
from flask import render_template, redirect, session, request, Flask 
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=dojo.Dojo.display_dojo())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')