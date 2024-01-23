import mongoengine as me

class Products(me.Document):
    meta = {
        "collection": "products"
    }
    id = me.StringField()
    title = me.StringField()
    description = me.StringField()
    owner_id = me.StringField()
    price = me.IntField()