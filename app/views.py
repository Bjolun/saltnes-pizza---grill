#!usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from flask import Flask, render_template, flash, session, redirect, url_for, abort, request
from app.models import PizzaMenu, ThaiMenu, GrillMenu, GrillTallerken, Users, PizzaInformation, ThaiInformation
from app.forms import AddPizza, AddThai, AddGrill, AddGrillTallerken, DeleteFood, EditPizzaAndThai, EditGrill, EditGrillTallerken, LoginForm, SignupForm, InformationPizza, InformationThai
from flask_login import login_user, login_required, logout_user

@app.route('/')
def home():
	pizzamenu = PizzaMenu.query.all()
	grillmenu = GrillMenu.query.all()
	grilltallerken = GrillTallerken.query.all()
	thaimenu = ThaiMenu.query.all()
	pizzainformation = PizzaInformation.query.all()
	thaiinformation = ThaiInformation.query.all()

	return render_template("index.html", pizzamenu = pizzamenu, grillmenu = grillmenu, grilltallerken = grilltallerken, thaimenu = thaimenu, pizzainformation = pizzainformation, thaiinformation = thaiinformation)

@app.route('/addpizza',methods=['GET','POST'])
@login_required
def addpizza():

	title = u"Legg til pizza"

	form = AddPizza()
	pizzamenu = PizzaMenu.query.all()


	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		description = form.description.data
		allergies = ' '.join(form.allergies.data)
		price = form.price.data
		new_pizza = PizzaMenu(id=id,title=name,description=description,allergies=allergies,price=price)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('addpizza'))

	return render_template('forms.html', form=form, title=title, menu=pizzamenu)

@app.route('/addthaimat',methods=['GET','POST'])
@login_required
def addthai():

	thaimenu = ThaiMenu.query.all()
	title = u"Legg til thaimat "

	form = AddThai()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		description = form.description.data
		allergies = ' '.join(form.allergies.data)
		price = form.price.data
		new_pizza = ThaiMenu(id=id,title=name,description=description,allergies=allergies,price=price)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('addthai'))

	return render_template('forms.html', form=form, title=title, menu=thaimenu)

@app.route('/addgrillmat',methods=['GET','POST'])
@login_required
def addgrill():

	title = u"Legg til grillmat"

	form = AddGrill()
	grillmenu = GrillMenu.query.all()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		description = form.description.data
		allergies = ' '.join(form.allergies.data)
		price_small = form.price_small.data
		price_medium = form.price_medium.data
		price_large = form.price_large.data
		new_pizza = GrillMenu(id=id,title=name,description=description,allergies=allergies,price_small=price_small,price_medium=price_medium,price_large=price_large)
		db.session.add(new_pizza)
		db.session.commit()

		return redirect(url_for('addgrill'))

	return render_template('forms.html', form=form, title=title, menu=grillmenu)

@app.route('/addgrilltallerken',methods=['GET','POST'])
@login_required
def addgrilltallerken():

	title = u"Legg til grilltallerken"

	form = AddGrillTallerken()
	grilltallerken = GrillTallerken.query.all()

	if form.validate_on_submit():

		id = int(form.id.data)
		name = form.name.data
		description = form.description.data
		allergies = ' '.join(form.allergies.data)
		price_small = form.price_small.data
		price_medium = form.price_medium.data
		price_large = form.price_large.data
		new_food = GrillTallerken(id=id,title=name,description=description,allergies=allergies,price_small=price_small,price_medium=price_medium,price_large=price_large)
		db.session.add(new_food)
		db.session.commit()

		return redirect(url_for('addgrilltallerken'))

	return render_template('forms.html', form=form, title=title, menu=grilltallerken)

@app.route('/add_confirm', methods=['GET','POST'])
@login_required
def add_confirm():

	return render_template('confirm.html')

@app.route('/deletepizza',methods=['GET','POST'])
@login_required
def delete_pizza():

	title = u"Slett Pizza"

	form = DeleteFood()
	pizzamenu = PizzaMenu.query.all()

	if form.validate_on_submit():
		id = form.idDel.data
		delete = PizzaMenu.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('delete_pizza'))

	return render_template('delete.html', form=form, title=title, menu=pizzamenu)

@app.route('/deletethai',methods=['GET','POST'])
@login_required
def delete_thai():

	title = u"Slett Thaimat"

	form = DeleteFood()
	thaimenu = ThaiMenu.query.all()

	if form.validate_on_submit():
		if del_confirm.data == "ja":
			id = form.idDel.data
			delete = ThaiMenu.query.get(id)

			db.session.delete(delete)
			db.session.commit()

		return redirect(url_for('delete_thai'))

	return render_template('delete.html', form=form, title=title, menu=thaimenu)

@app.route('/deletegrill',methods=['GET','POST'])
@login_required
def delete_grill():

	title = u"Slett Grillmat"

	form = DeleteFood()
	grillmenu = GrillMenu.query.all()


	if form.validate_on_submit():
		id = form.idDel.data
		delete = GrillMenu.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('delete_grill'))

	return render_template('delete.html', form=form, title=title, menu=grillmenu)

@app.route('/deletegrilltallerken',methods=['GET','POST'])
@login_required
def delete_grilltallerken():

	title = u"Slett Grilltallerken"

	form = DeleteFood()
	grilltallerken = GrillTallerken.query.all()


	if form.validate_on_submit():
		id = form.idDel.data
		delete = GrillTallerken.query.get(id)

		db.session.delete(delete)
		db.session.commit()

		return redirect(url_for('delete_grilltallerken'))

	return render_template('delete.html', form=form, title=title, menu=grilltallerken)

@app.route('/editpizza', methods=['GET', 'POST'])
@login_required
def edit_pizza():

	title = u"Endre pizza"
	pizzamenu = PizzaMenu.query.all()


	form = EditPizzaAndThai()

	if form.validate_on_submit():
		id = form.id.data

		if form.name.data != "":
			db.session.query(PizzaMenu).filter(PizzaMenu.id == id).update({'title': form.name.data})
			db.session.commit()

		if form.description.data != "":
			db.session.query(PizzaMenu).filter(PizzaMenu.id == id).update({'description': form.description.data})
			db.session.commit()

		if form.price.data != "":
			db.session.query(PizzaMenu).filter(PizzaMenu.id == id).update({'price': form.price.data})
			db.session.commit()

		try:
			if form.allergies_check.data[0]:
				db.session.query(PizzaMenu).filter(PizzaMenu.id == id).update({'allergies': ' '.join(form.allergies.data)})
				db.session.commit()
		except:
			pass

		return redirect(url_for(u'edit_pizza'))


	return render_template(u'editpizza.html', form = form, title = title, menu=pizzamenu)

@app.route('/edit_thai', methods=['GET', 'POST'])
@login_required
def edit_thai():

	title = u'Endre thaimat'

	form = EditPizzaAndThai()
	thaimenu = ThaiMenu.query.all()

	if form.validate_on_submit():
		id = form.id.data

		if form.name.data != "":
			db.session.query(ThaiMenu).filter(ThaiMenu.id == id).update({'title': form.name.data})
			db.session.commit()

		if form.description.data != "":
			db.session.query(ThaiMenu).filter(ThaiMenu.id == id).update({'description': form.description.data})
			db.session.commit()

		if form.price.data != "":
			db.session.query(ThaiMenu).filter(ThaiMenu.id == id).update({'price': form.price.data})
			db.session.commit()

		try:
			if form.allergies_check.data[0]:
				db.session.query(ThaiMenu).filter(ThaiMenu.id == id).update({'allergies': ' '.join(form.allergies.data)})
				db.session.commit()
		except:
			pass

		return redirect(url_for(u'edit_thai'))

	return render_template(u'edit_thai.html', form = form, title = title, menu=thaimenu)

@app.route('/edit_grill', methods=['GET', 'POST'])
@login_required
def edit_grill():

	title = u'Endre grillmat'

	form = EditGrill()
	grillmenu = GrillMenu.query.all()

	if form.validate_on_submit():
		id = form.id.data

		if form.name.data != "":
			db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'title': form.name.data})
			db.session.commit()

		if form.description.data != "":
			db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'description': form.description.data})
			db.session.commit()

		if form.price_small.data != "":
			db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'price_small': form.price_small.data})
			db.session.commit()

		if form.price_medium.data != "":
			db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'price_medium': form.price_medium.data})
			db.session.commit()

		if form.price_large.data != "":
			db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'price_large': form.price_large.data})
			db.session.commit()

		try:
			if form.allergies_check.data[0]:
				db.session.query(GrillMenu).filter(GrillMenu.id == id).update({'allergies': ' '.join(form.allergies.data)})
				db.session.commit()
		except:
			pass

		return redirect(url_for(u'edit_grill'))

	return render_template(u'editgrill.html', form = form, title = title, menu=grillmenu)

@app.route('/edit_grilltallerken', methods=['GET', 'POST'])
@login_required
def edit_grilltallerken():

	title = u'Endre grilltallerken'

	form = EditGrillTallerken()
	grillmenu = GrillTallerken.query.all()

	if form.validate_on_submit():
		id = form.id.data

		if form.name.data != "":
			db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'title': form.name.data})
			db.session.commit()

		if form.description.data != "":
			db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'description': form.description.data})
			db.session.commit()

		if form.price_small.data != "":
			db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'price_small': form.price_small.data})
			db.session.commit()

		if form.price_medium.data != "":
			db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'price_medium': form.price_medium.data})
			db.session.commit()

		if form.price_large.data != "":
			db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'price_large': form.price_large.data})
			db.session.commit()

		try:
			if form.allergies_check.data[0]:
				db.session.query(GrillTallerken).filter(GrillTallerken.id == id).update({'allergies': ' '.join(form.allergies.data)})
				db.session.commit()
		except:
			pass

		return redirect(url_for(u'edit_grilltallerken'))

	return render_template(u'editgrilltallerken.html', form = form, title = title, menu=grillmenu)

@app.route('/editinfothai', methods=['GET','POST'])
@login_required
def edit_info_thai():
	title = u"Endre andre priser assosiert med thaimat"
	form = InformationThai()
	thaiinformation = ThaiInformation.query.all()

	if form.validate_on_submit():
		if form.thai_extra_meat.data != "":
			db.session.query(ThaiInformation).filter(ThaiInformation.id == 1).update({'thai_extra_meat': form.thai_extra_meat.data})
			db.session.commit()

		if form.thai_extra_rice.data != "":
			db.session.query(ThaiInformation).filter(ThaiInformation.id == 1).update({'thai_extra_rice':form.thai_extra_rice.data})
			db.session.commit()

		return redirect(url_for(u'edit_info_thai'))

	return render_template(u'editinfothai.html', title=title, form=form, info=thaiinformation[0])

@app.route('/editinfopizza', methods=['GET','POST'])
@login_required
def edit_info_pizza():
	title = u"Endre andre priser assosiert med pizza"
	form = InformationPizza()
	pizzainformation = PizzaInformation.query.all()

	if form.validate_on_submit():
		if form.medium_pizza_price.data != "":
			db.session.query(PizzaInformation).filter(PizzaInformation.id == 1).update({'medium_pizza_price': form.medium_pizza_price.data})
			db.session.commit()

		if form.red_sauce.data != "":
			db.session.query(PizzaInformation).filter(PizzaInformation.id == 1).update({'price_red_sauce': form.red_sauce.data})
			db.session.commit()

		if form.white_sauce.data != "":
			db.session.query(PizzaInformation).filter(PizzaInformation.id == 1).update({'price_white_sauce': form.white_sauce.data})
			db.session.commit()

		if form.pizza_extra_meat.data != "":
			db.session.query(PizzaInformation).filter(PizzaInformation.id == 1).update({'pizza_extra_meat':form.pizza_extra_meat.data})
			db.session.commit()

		if form.pizza_extra_cheese.data != "":
			db.session.query(PizzaInformation).filter(PizzaInformation.id == 1).update({'pizza_extra_cheese':form.pizza_extra_cheese.data})
			db.session.commit()

		return redirect(url_for('edit_info_pizza'))

	return render_template('editinfopizza.html', title=title, form=form, info=pizzainformation[0])

@app.route('/logout')
@login_required
def logout():

	# from flask-login
	logout_user()

	flash(u'You logged out')
	return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()

	if form.validate_on_submit():

		try:
			user = Users.query.filter_by(brukernavn=form.brukernavn.data).first()
		except:
			session['login_msg'] = [u"Kunne ikke logge deg inn.", u"Passord eller brukernavn er feil."]

		try:
			# Uses the function to check if the password matches
			if user.check_password(form.passord.data) and user is not None:

				# from flask-login
				login_user(user)
				flash(u"Logged in successfully!")

				next = request.args.get('next')

				if next == None or not next[0] == '/':
					next = url_for('home')

				return redirect(next)

		except:
			session['login_msg'] = [u"Kunne ikke logge deg inn.", u"Passord eller brukernavn er feil."]
			return redirect(url_for('login'))

	return render_template('login.html', form=form)

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#
# 	form = SignupForm()
#
# 	if form.validate_on_submit():
#
# 		brukernavn = form.brukernavn.data
# 		passord = form.passord.data
#
# 		new_user = Users(brukernavn=brukernavn, passord=passord)
# 		db.session.add(new_user)
# 		db.session.commit()
#
# 		return redirect(url_for('home'))
#
# 	return render_template('signup.html', form=form)
