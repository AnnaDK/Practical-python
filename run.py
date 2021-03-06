import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-u1lvc.mongodb.net/cookbook?retryWrites=true&w=majorit'

mongo = PyMongo(app)


@app.route('/')
@app.route('/find_recipes')
def find_recipes():
    return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())





@app.route('/add_recipes')
def add_recipes():
    return render_template("add_recipe.html", categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
