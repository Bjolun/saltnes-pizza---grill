from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class PizzaMenu(db.Model):

    __tablename__ = "pizzamenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    price = db.Column(db.String)

    def __init__(self, id, title, description, allergies, price):
        self.id = id
        self.title = title
        self.description = description
        self.allergies = allergies
        self.price = price

class ThaiMenu(db.Model):

    __tablename__ = "thaimenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    price = db.Column(db.String)

    def __init__(self, id, title, description, allergies, price):
        self.id = id
        self.title = title
        self.description = description
        self.allergies = allergies
        self.price = price

class GrillMenu(db.Model):

    __tablename__ = "grillmenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    # Price for each size, if only one size then use "price_large"
    price_small = db.Column(db.String)
    price_medium = db.Column(db.String)
    price_large = db.Column(db.String)

    def __init__(self, id, title, description, allergies, price_small, price_medium, price_large):
        self.id = id
        self.title = title
        self.description = description
        self.allergies = allergies
        self.price_small = price_small
        self.price_medium = price_medium
        self.price_large = price_large

class Users(db.Model,UserMixin):

    __tablename__ = "brukere"

    id = db.Column(db.Integer, primary_key=True)
    brukernavn = db.Column(db.String(64), unique=True)
    passord_hashet = db.Column(db.String(128), unique=False)

    def __init__(self, brukernavn, passord):
        self.brukernavn = brukernavn
        self.passord_hashet = generate_password_hash(passord)

    def check_password(self, passord):

        return check_password_hash(self.passord_hashet, passord)

class PizzaInformation(db.Model,UserMixin):

    __tablename__ = "pizza_informasjon"

    id = db.Column(db.Integer, primary_key=True)
    medium_pizza_price = db.Column(db.String)
    price_red_sauce = db.Column(db.String)
    price_white_sauce = db.Column(db.String)
    pizza_extra_meat = db.Column(db.String)
    pizza_extra_cheese = db.Column(db.String)

    def __init__(self, medium_pizza_price, price_red_sauce, price_white_sauce, pizza_extra_meat, pizza_extra_cheese):
        self.medium_pizza_price = medium_pizza_price
        self.price_red_sauce = price_red_sauce
        self.price_white_sauce = price_white_sauce
        self.pizza_extra_meat = pizza_extra_meat
        self.pizza_extra_cheese = pizza_extra_cheese

class ThaiInformation(db.Model,UserMixin):

    __tablename__ = "thai_informasjon"

    id = db.Column(db.Integer, primary_key=True)
    thai_extra_meat = db.Column(db.String)
    thai_extra_rice = db.Column(db.String)

    def __init__(self, thai_extra_meat, thai_extra_rice):
        self.thai_extra_meat = thai_extra_meat
        self.thai_extra_rice = thai_extra_rice
