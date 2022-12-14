from flask import Flask, render_template
from routes.pokemon import pokemons




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/manpower'

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

app.register_blueprint(pokemons)


