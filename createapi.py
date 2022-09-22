#import requests
#setup flask
from unicodedata import name
from flask import Flask, request
app  = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

# configure database in code and  then use terminal to do add the  tables and data in it by following steps:
# from createapi import db
# db.create_all()
#drink = Drink(name="Grape Soda", description="tastes like grapes") - to do this you willl have to do from createapi import Drink
#Anytime anything has to be used in the terminal from the file/code, it has to be imported
#db.session.add(drink)
#sb.session.commit()
#verify drink has been added by typing either drink OR Drink.query.all()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#in ORM, everything to be stored in DB is defined as models so we are creating a model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description=db.Column(db.String(120))

    #to print drink objecto nce we create it in terminal with data in it
    def __repr__(self):
        return f"{self.name} - {self.description}" 


#simple route , api endpoint 
@app.route('/')
def index():
    return 'hello'

#get request for drinks that are stored in the app
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    #create list as we cannot directly print drink so we need to reiterate through it and create a list
    output=[]
    for drink in drinks:
        drink_data = {"name":drink.name, "description": drink.description}
        #creating a list of dictionaries
        output.append(drink_data)

    return {"drinks" :  output}

    

#get request by id
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name" : drink.name, "description" : drink.description}


#adding a drink-post
@app.route('/drinks', methods=['POST'])
def add_drink():

#reading data that has been sent as json in the request and adding it to Db and commiting it
    drink = Drink(name= request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {"newdrinkid" : drink.id}




#deleting a drink-delete
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error" : "no drink found so nothing can be deleted"}
    db.session.delete(drink)
    db.session.commit()
    return {"Success" : "yippee"}
