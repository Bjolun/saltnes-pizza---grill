#!usr/bin/python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, SelectMultipleField, RadioField
from wtforms import validators, widgets

allergies_list = [(u'Melk',u'Melk'),(u'Hvetegluten',u'Hvetegluten'),(u'Selleri',u'Selleri'),(u'Sennep',u'Sennep'),(u'Soya',u'Soya'),(u'Skalldyr',u'Skalldyr'),(u'Nøtter',u'Nøtter'),(u'Egg',u'Egg'),(u'Sesam',u'Sesam'),(u'Fisk',u'Fisk')]

class AddPizza(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Pizza tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Pizzaen? ',[validators.Required()])
    allergies = SelectMultipleField(u'Velg allergener for maten',choices=allergies_list,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    price = StringField(u'Pris på pizza (stor): ')
    submit = SubmitField(u'Legg til Pizza')

class AddThai(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Thaimat tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Thaimaten? ',[validators.Required()])
    allergies = SelectMultipleField(u'Velg allergener for maten',choices=allergies_list,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    price = StringField(u'Pris på thaimat: ')
    submit = SubmitField(u'Legg til Thaimat')

class AddGrill(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Grillmat tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Grillmaten? ',[validators.Required()])
    allergies = SelectMultipleField(u'Velg allergener for maten',choices=allergies_list,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    price_small = StringField(u'Pris på grillmaten (liten): ')
    price_medium = StringField(u'Pris på grillmaten (medium)')
    price_large = StringField(u'Pris på grillmaten (stor)')
    submit = SubmitField(u'Legg til grillmat')

class DeleteFood(FlaskForm):

    idDel = IntegerField(u'Id-Nummer på retten du vil slette.',[validators.Required()])
    del_confirm = RadioField(u"Bekreft",choices=[(u'ja',u'Ja, jeg vil slette denne retten')])
    submit = SubmitField(u'Slett')

class EditPizzaAndThai(FlaskForm):

    id = IntegerField(u'Hvilken matrett vil du endre på? Id-nummer (Obligatorisk):', [validators.Required()])
    name = StringField(u'Nytt Navn')
    description = StringField(u'Endre beskrivelse')
    price = StringField(u'Endre pris')
    allergies_check = SelectMultipleField(u'Allergi-sjekk', choices=[(u"yes",u'Huk av for å endre på allergier')],option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    allergies = SelectMultipleField(u'Velg allergener for maten',choices=allergies_list,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    submit = SubmitField(u'Lagre endringer')


class EditGrill(FlaskForm):

    id = IntegerField(u'Hvilken rett vil du endre på? Id-nummer(Obligatorisk)', [validators.Required()])
    name = StringField(u'Nytt navn')
    description = StringField(u'Endre beskrivelse')
    price_small = StringField(u'Endre pris på liten rett (Bruk mellomrom for å fjerne nåværende pris)')
    price_medium = StringField(u'Endre pris på medium rett (Bruk mellomrom for å fjerne nåværende pris)')
    price_large = StringField(u'Endre pris på stor rett (Bruk mellomrom for å fjerne nåværende pris)')
    allergies_check = SelectMultipleField(u'Allergi-sjekk', choices=[(u"yes",'Huk av for å endre på allergier')],option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    allergies = SelectMultipleField(u'Velg allergener for maten',choices=allergies_list,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    submit = SubmitField(u'Lagre endringer')

class LoginForm(FlaskForm):

    brukernavn = StringField(u'Brukernavn: ', [validators.Required()])
    passord = PasswordField(u'Passord: ', [validators.Required()])
    submit = SubmitField(u'Logg inn')

class SignupForm(FlaskForm):

    brukernavn = StringField(u'Brukernavn: ', [validators.Required()])
    passord = PasswordField(u'Passord: ', [validators.Required()])
    submit = SubmitField(u'Lag bruker')

class InformationPizza(FlaskForm):

    medium_pizza_price = StringField(u'Pris for medium pizza: ')
    red_sauce = StringField(u'Pris for rød saus, pizza: ')
    white_sauce = StringField(u'Pris for hvit saus, pizza: ')
    pizza_extra_meat = StringField(u'Pris for ekstra kjøtt på pizza: ')
    pizza_extra_cheese = StringField(u'Pris for ekstra ost på pizza: ')
    submit = SubmitField(u'Endre informasjon')

class InformationThai(FlaskForm):

    thai_extra_meat = StringField(u'Pris for ekstra kjøtt: ')
    thai_extra_rice = StringField(u'Pris for ekstra ris: ')
    submit = SubmitField(u'Endre informasjon')
