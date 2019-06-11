from app import app
from flask import Flask, render_template, flash, session, redirect, url_for
from app.models import db, PizzaMenu, ThaiMenu, GrillMenu
from app.forms import AddPizza, AddThai, AddGrill


@app.route('/')
def home():

	return render_template("index.html")

@app.route('/addpizza',methods=['GET','POST'])
def addpizza():

	title = "Legg til pizza"

	form = AddPizza()

	if form.validate_on_submit():
		name = form.name.data
		session['item'] = form.name.data
		description = form.description.data
		allergies = form.allergies.data
		price = form.price.data
		return redirect(url_for('add_confirm'))

	return render_template('forms.html', form=form, title=title)

@app.route('/addthaimat',methods=['GET','POST'])
def addthai():

	title = "Legg til thaimat"

	form = AddThai()

	return render_template('forms.html', form=form, title=title)

@app.route('/addgrillmat',methods=['GET','POST'])
def addgrill():

	title = "Legg til grillmat"

	form = AddGrill()

	return render_template('forms.html', form=form, title=title)

@app.route('/add_confirm', methods=['GET','POST'])
def add_confirm():

	return render_template('confirm.html')
