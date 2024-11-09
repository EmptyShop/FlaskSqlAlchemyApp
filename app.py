from flask import Flask
from flask_cors import CORS
from routes.contacts import bpcontacts  # las rutas para la app web
from routes.contactsApi import bpcontactsApi    # las rutas para la Api
from config import DATABASE_CONNECTION_URI, SECRET_KEY

app = Flask(__name__)
CORS(app)

app.config.from_mapping(
    SECRET_KEY = SECRET_KEY
)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# registra las rutas con la app
app.register_blueprint(bpcontacts)
app.register_blueprint(bpcontactsApi)