from app import db

class PizzaMenu(db.Model):

    __tablename__ = "pizzamenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    price = db.Column(db.String)

    def __init__(self, title, description, allergies, price):
        title = self.title
        description = self.description
        allergies = self.allergies
        price = self.price

class ThaiMenu(db.Model):

    __tablename__ = "thaimenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    price = db.Column(db.String)

    def __init__(self, title, description, allergies, price):
        title = self.title
        description = self.description
        allergies = self.allergies
        price = self.price

class GrillMenu(db.Model):

    __tablename__ = "grillmenu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    allergies = db.Column(db.String)
    price = db.Column(db.String)

    def __init__(self, title, description, allergies, price):
        title = self.title
        description = self.description
        allergies = self.allergies
        price = self.price
