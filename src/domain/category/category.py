import mongoengine as me

class Category(me.Document):
    meta = {
        "collection": "categories"
    }
    id = me.StringField()
    title = me.StringField()
    description = me.StringField()
    owner_id = me.StringField()