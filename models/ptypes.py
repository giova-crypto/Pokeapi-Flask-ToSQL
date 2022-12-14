from utils.db import db

class ptypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    def __init__(self, name):
        self.name = name