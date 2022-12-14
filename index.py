from app import app
from utils.db import db

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)