from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ refers to this file.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cart.db"
db = SQLAlchemy(app)

class user_cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False) # Don't want user to be able to create and empty list item.

    def __repr__(self):
        return "ITEM %r" %self.id

@app.route("/", methods = ["GET", "POST"]) # This empty slash just means that it's starting the server. There's no route; This is running right where it starts up.
def home():
    if request.method == 'POST':
        item_content = request.form["item"] # gets the content of the form with the given id
        new_cart_item = user_cart(title = item_content) # creates a new item to be stored in the database

        try:
            db.session.add(new_cart_item) # adding the item to the cart
            db.session.commit() # pushing the item to the cart (basically finalizing it)
            return redirect("/")
        except:
            return "There was an issue adding your item."


    else:
        items = user_cart.query.all() # returns everything in the database
        return render_template("home.html", items = items) # items = items puts the database onto the page itself


if __name__ == "__main__":
    app.run(debug = True)