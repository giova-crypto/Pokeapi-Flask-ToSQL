from utils.db import db

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    base_stat = db.Column(db.SmallInteger)

    def __init__(self, name, base_stat):
        self.name = name
        self.base_stat = base_stat