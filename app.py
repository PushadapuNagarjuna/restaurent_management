from model import app, db, Menu
db.create_all()
menu_card = {'Idly':'20rs','Dosa':'30rs','Puri':'30rs','Lemon rice':'40rs','Thumps-up':'20rs','IceCream':'10rs'}
for name, price in menu_card.items():
    if Menu.query.filter(Menu.item_name == name):
        print(f"Item {name} already exists")
    else:
        db.session.add(Menu(name=name, price=price))
        db.session.commit()
