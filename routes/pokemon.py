import requests
from flask import Blueprint
import pandas as pd
from models.pokemon import Pokemon
from models.stats import Stats
from models.ptypes import ptypes
from models.abilities import Abilities
from utils.db import db
pokemons = Blueprint('pokemons', __name__)

def save_pokemon(data):
    image = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+str(data.get('order'))+'.png'
    new_poke = Pokemon(data.get('name'), image)
    types = []
    stats = []
    abilities = []
    old_types = []
    old_abilities = []
    for st in data.get('stats'):
        new_stat = Stats(name=st.get("stat").get('name'), base_stat=st.get('base_stat'))
        stats.append(new_stat)
    for type in data.get('types'):
        row = db.session.query(ptypes).filter_by(name=type.get('type').get('name')).first()
        if(row):
            old_types.append(row)
        else:
            new_type = ptypes(name=type.get('type').get('name'))
            types.append(new_type)
    for ability in data.get('abilities'):
        row = db.session.query(Abilities).filter_by(name=ability.get('ability').get('name')).first()
        if (row):
            old_abilities.append(row)
        else:
            new_ability = Abilities(name=ability.get('ability').get('name'))
            abilities.append(new_ability)
    db.session.add_all(stats)
    db.session.add_all(types)
    db.session.add_all(abilities)
    db.session.add(new_poke)
    for st in stats:
        new_poke.stat.append(st)
    for tp in types:
        new_poke.type.append(tp)
    for ab in abilities:
        new_poke.ability.append(ab)
    for otp in old_types:
        new_poke.type.append(otp)
    for oab in old_abilities:
        new_poke.ability.append(oab)

    db.session.commit()

@pokemons.route('/init')
def start_flow():
    try:
        req = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
        results = req.json().get('results')
        for poke in results:
            url = poke.get('url')
            req = requests.get(url)
            data = req.json()
            save_pokemon(data)
        return "Success"
    except Exception as e:
        return "Something went wrong: ",e

@pokemons.route('/punto4/1')
def punto41():
    sql = db.text('select p.id,p.name, p.image  from pokemon_types as pt join pokemon as p on pt.pokemon_id = p.id group by p.id having COUNT(*) >1')
    query = db.engine.execute(sql)
    df = pd.DataFrame(query.fetchall())
    df.to_excel("punto4/script1.xlsx", index=False)
    return "success"

@pokemons.route('/punto4/2')
def punto42():
    sql = db.text('select pt.type_id, t.name, COUNT(*) from pokemon_types as pt join ptypes as t on pt.type_id = t.id group by t.id order by COUNT(*) desc limit 1')
    query = db.engine.execute(sql)
    df = pd.DataFrame(query.fetchall())
    df.to_excel("punto4/script2.xlsx", index=False)
    return "success"
