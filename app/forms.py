from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
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

class EditPizzaAndThai(FlaskForm):

    id = IntegerField(u'Hvilken matrett vil du endre på? Id-nummer (Obligatorisk):', [validators.Required()])
    name = StringField(u'Nytt Navn')
    description = StringField(u'Endre beskrivelse')
    price = StringField(u'Endre pris')
    submit = SubmitField('Lagre endringer')


class EditGrill(FlaskForm):

    id = IntegerField(u'Hvilken rett vil du endre på? Id-nummer(Obligatorisk)', [validators.Required()])
    name = StringField(u'Nytt navn')
    description = StringField(u'Endre beskrivelse')
    price_small = StringField(u'Endre pris på liten rett (Bruk mellomrom for å fjerne nåværende pris)')
    price_medium = StringField(u'Endre pris på medium rett (Bruk mellomrom for å fjerne nåværende pris)')
    price_large = StringField(u'Endre pris på stor rett (Bruk mellomrom for å fjerne nåværende pris)')
    submit = SubmitField('Lagre endringer')

class LoginForm(FlaskForm):

    brukernavn = StringField(u'Brukernavn: ', [validators.Required()])
    passord = PasswordField(u'Passord: ', [validators.Required()])
    submit = SubmitField('Logg inn')

class SignupForm(FlaskForm):

    brukernavn = StringField(u'Brukernavn: ', [validators.Required()])
    passord = PasswordField(u'Passord: ', [validators.Required()])
    submit = SubmitField('Lag bruker')
