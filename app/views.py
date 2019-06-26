from app import app, db
from flask import Flask, render_template, flash, session, redirect, url_for
from app.models import PizzaMenu, ThaiMenu, GrillMenu
from app.forms import AddPizza, AddThai, AddGrill, DeleteFood


@app.route('/')
def home():
	pizzamenu = PizzaMenu.query.all()
	grillmenu = GrillMenu.query.all()
	thaimenu = ThaiMenu.query.all()
	return render_template("index.html", pizzamenu = pizzamenu, grillmenu = grillmenu, thaimenu = thaimenu)

@app.route('/addpizza',methods=['GET','POST'])
def addpizza():

	title = "Legg til pizza"

	form = AddPizza()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		session['item'] = form.name.data
		description = form.description.data
		allergies = form.allergies.data
		price = form.price.data
		new_pizza = PizzaMenu(id=id,title=name,description=description,allergies=allergies,price=price)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('forms.html', form=form, title=title)

@app.route('/addthaimat',methods=['GET','POST'])
def addthai():

	title = "Legg til thaimat"

	form = AddThai()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		session['item'] = form.name.data
		description = form.description.data
		allergies = form.allergies.data
		price = form.price.data
		new_pizza = ThaiMenu(id=id,title=name,description=description,allergies=allergies,price=price)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('forms.html', form=form, title=title)

@app.route('/addgrillmat',methods=['GET','POST'])
def addgrill():

	title = "Legg til grillmat"

	form = AddGrill()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		session['item'] = form.name.data
		description = form.description.data
		allergies = form.allergies.data
		price_small = form.price_small.data
		price_medium = form.price_medium.data
		price_large = form.price_large.data
		new_pizza = GrillMenu(id=id,title=name,description=description,allergies=allergies,price_small=price_small,price_medium=price_medium,price_large=price_large)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('forms.html', form=form, title=title)

@app.route('/add_confirm', methods=['GET','POST'])
def add_confirm():

	return render_template('confirm.html')

@app.route('/deletepizza',methods=['GET','POST'])
def delete_pizza():

	title = "Slett Pizza"

	form = DeleteFood()

	if form.validate_on_submit():
		id = form.idDel.data
		delete = PizzaMenu.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('delete.html', form=form, title=title)

@app.route('/deletethai',methods=['GET','POST'])
def delete_thai():

	title = "Slett Thaimat"

	form = DeleteFood()

	if form.validate_on_submit():
		id = form.idDel.data
		delete = ThaiMenu.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('delete.html', form=form, title=title)

@app.route('/deletegrill',methods=['GET','POST'])
def delete_grill():

	title = "Slett Grillmat"

	form = DeleteFood()

	if form.validate_on_submit():
		id = form.idDel.data
		delete = GrillMenu.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('add_confirm'))

	return render_template('delete.html', form=form, title=title)
