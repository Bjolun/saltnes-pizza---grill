from app import app
from flask import Flask, render_template
from app.models import db, PizzaMenu, ThaiMenu, GrillMenu


@app.route('/')
def home():

	return render_template("index.html")

@app.route("/menu")
def menu():
	return render_template("menu.html")
