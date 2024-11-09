from app import app
from utils.db import db # la db para la app
from utils.ma import ma # el esquema para la Api

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all() # crea las tablas y realiza los cambios en la bd

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.64')