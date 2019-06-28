from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators

class AddPizza(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Pizza tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Pizzaen? ',[validators.Required()])
    allergies = StringField(u'Allergier (i tall):',[validators.Required()])
    price = StringField(u'Pris på pizza (stor): ')
    submit = SubmitField('Legg til Pizza')

class AddThai(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Thaimat tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Thaimaten? ',[validators.Required()])
    allergies = StringField(u'Allergier (i tall):',[validators.Required()])
    price = StringField(u'Pris på thaimat: ')
    submit = SubmitField('Legg til Thaimat')

class AddGrill(FlaskForm):

    id = IntegerField(u'Hvilken id har matretten? ',[validators.Required()])
    name = StringField(u'Grillmat tittel: ',[validators.Required()])
    description = StringField(u'Hva inneholder Grillmaten? ',[validators.Required()])
    allergies = StringField(u'Allergier (i tall):',[validators.Required()])
    price_small = StringField(u'Pris på grillmaten (liten): ')
    price_medium = StringField(u'Pris på grillmaten (medium)')
    price_large = StringField(u'Pris på grillmaten (stor)')
    submit = SubmitField('Legg til grillmat')

class DeleteFood(FlaskForm):

    idDel = IntegerField(u'Id-Nummer på retten du vil slette.',[validators.Required()])
    submit = SubmitField('Slett')

class EditPizza(FlaskForm):

    id = IntegerField(u'Hvilken pizza vil du endre på? Id-nummer(Obligatorisk):', [validators.Required()])
    name = StringField(u'Nytt Navn')
    description = StringField(u'Endre beskrivelse')
    price = StringField(u'Endre pris')
    submit = SubmitField('Lagre endringer')
