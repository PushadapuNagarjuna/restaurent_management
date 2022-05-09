from main import app, db, Menu
from flask_restful import Api, Resource

api = Api(app)


class Menu_card(Resource):
    def get(self):
        card = Menu.query.all()
        items = []
        for item in card:
            items.append(f"{{'id':{item.item_id},'item_name':{item.item_name},'price':{item.price}}}")
        return {'Menu': items}


api.add_resource(Menu_card, '/menu')
app.run(debug=True)
