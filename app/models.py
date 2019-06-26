from app import db

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
