from flask_mongoengine import MongoEngine

class MongoDBConfig(object):
    def mongo_configure(self):
        return MongoEngine(config={"host":"mongodb://localhost/product-catalog"})