from flask_app import app
from flask import render_template, redirect, session, request, Flask 
from flask_app.models.dojo import Dojo

@app.route('/')
def index_page():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.display_dojo()
    return render_template('index.html', all_dojos = dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template('/dojos.html', dojo=Dojo.get_one_ninjas(data))
