from random import randint
from database import get_db, close_db

def fetch_catalog():
    db = get_db()
    #Gets everything from products and services and displays all of it
    products = db.execute("""SELECT * FROM products;""").fetchall()
    services = db.execute("""SELECT * FROM services;""").fetchall()
    close_db()
    return products, services

def random_products(user):
        # The id's for the db products and services
        choices = [12, 10, 54, 32, 1, 2, 7, 100, 20, 30, 34, 19, 3, 4, 5, 99, 88,
        60, 61, 62, 63, 64, 65, 66]
        # Picks a random id from the list
        memory = []
        pick = choices[randint(0, 23)]
        products = []
        db = get_db()
        profile_info = db.execute("""SELECT * FROM profile WHERE user_id = ?;""",(user,)).fetchone()
        if profile_info is not None:
            profile_info = profile_info
        else:
            profile_info = None
        #Saves the pick to memory to try ensure no duplicates 
        memory.append(pick)
        #Ensures that only 3 products will be chosen
        while len(products) < 3:            #This is for a randomized catalog on home page loading which allows you to go directly to
                                            #random pages
            product = db.execute("""SELECT * FROM products WHERE product_id = ?;""", (pick,)).fetchone()
            service = db.execute("""SELECT * FROM services WHERE product_id = ?;""", (pick,)).fetchone()
            if product is not None:
                new_pick = choices[randint(0, 23)]  #Picking a new item and comparing with the previous item
                while new_pick in memory:             #Changes the pick if ite in memory
                    new_pick = choices[randint(0, 23)]  
                pick = new_pick
                products.append(product)               #appends the dict product to the list products
            else:
                new_pick = choices[randint(0, 23)]      #The same as above but for services
                while new_pick == pick:         
                    new_pick = choices[randint(0, 23)]
                pick = new_pick
                products.append(service)
        return products