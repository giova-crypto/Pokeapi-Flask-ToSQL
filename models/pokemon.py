from utils.db import db

pokemon_stats = db.Table('pokemon_stats',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
    db.Column('stat_id', db.Integer, db.ForeignKey('stats.id'))
)

pokemon_types = db.Table('pokemon_types',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('ptypes.id'))
)

pokemon_abilities = db.Table('pokemon_abilities',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
    db.Column('ability_id', db.Integer, db.ForeignKey('abilities.id'))
)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    image = db.Column(db.String(300))
    stat = db.relationship('Stats', secondary=pokemon_stats, backref='stats')
    type = db.relationship('ptypes', secondary=pokemon_types, backref='ptypes')
    ability = db.relationship('Abilities', secondary=pokemon_abilities, backref='abilities')

    def __init__(self, name, image):
        self.name = name
        self.image = image