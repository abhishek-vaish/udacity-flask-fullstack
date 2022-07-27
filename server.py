from flask import Flask, redirect, render_template, request, url_for
from database import Base, Restaurant, MenuItems, engine
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
def readRestaurant():
    restaurant = session.query(Restaurant).first()
    DEFAULT_MESSAGE='No items found!!'
    print(restaurant)
    if restaurant:
        items = session.query(MenuItems)
        return render_template('main.html', name=restaurant.name, id=restaurant.id, items=items)
    else:
        return render_template('main.html', data=DEFAULT_MESSAGE)
     
@app.route('/restaurant/create', methods=['GET', 'POST'])
def createRestaurant():
    if request.method == 'POST':
        restaurant_name = request.form['name']
        session.add(Restaurant(name=restaurant_name))
        session.commit()
        return redirect(url_for('readRestaurant'))
    else:
        return render_template('restaurant.html')

# Task 1: Create route for newMenuItem function here


@app.route("/restaurant/<int:restaurant_id>/create/", methods=['GET','POST'])
def createMenuItem(restaurant_id):
    try:
        if request.method == 'POST':
            session.add(MenuItems(
                name=request.form['name'], 
                description=request.form['description'],
                price=request.form['price'], 
                course=request.form['course'], 
                restaurant_id=restaurant_id
            ))
            session.commit()
            return redirect(url_for('readRestaurant'))
        else:
            return render_template('menuitems.html', restaurant_id=restaurant_id)
    except:
        session.rollback()
        return

# Task 2: Create route for editMenuItem function here

@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/")
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/")
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"



if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)
    