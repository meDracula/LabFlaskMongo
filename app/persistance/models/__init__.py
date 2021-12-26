from app.persistance.db import Document, db


class User(Document):
    collection = db.users


class Researchers(Document):
    collection = db.researchers
