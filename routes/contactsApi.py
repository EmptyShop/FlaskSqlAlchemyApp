from flask import Blueprint, request, jsonify
from flask_cors import CORS
from models.contact import Contact
from models.contactSchema import ContactSchema
from utils.db import db

bpcontactsApi = Blueprint('contactsapi', __name__)
CORS(bpcontactsApi, methods=['GET', 'POST', 'PUT', 'DELETE'])

contact_schema = ContactSchema()    # esquema para un solo elemento
contacts_schema = ContactSchema(many=True)  # esquema para varios elementos

@bpcontactsApi.route('/contact', methods = ['GET'])
def get_contacts():
    contacts = Contact.query.all()

    lista_contacts = contacts_schema.dump(contacts)

    return contacts_schema.jsonify(lista_contacts)

@bpcontactsApi.route('/contact/<id>', methods = ['GET'])
def get_contact(id):
    contact = Contact.query.get(id)

    if contact:
        return contact_schema.jsonify(contact)
    else:
        return jsonify(error="No se encontró el contacto."), 404

@bpcontactsApi.route('/contact', methods = ['POST'])
def add_contact():
    fullname = request.json['fullname']
    email = request.json['email']
    phone = request.json['phone']

    contact = Contact(fullname, email, phone)
    db.session.add(contact)
    db.session.commit()

    return contact_schema.jsonify(contact)

@bpcontactsApi.route('/contact/<id>', methods = ['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)

    if contact:
        contact.fullname = request.json['fullname']
        contact.email = request.json['email']
        contact.phone = request.json['phone']

        db.session.commit()

        return jsonify(success="actualizado")
    else:
        return jsonify(error="No se encontró el contacto."), 404

@bpcontactsApi.route('/contact/<id>', methods = ['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)

    if contact:
        db.session.delete(contact)
        db.session.commit()

        return jsonify(success="eliminado")
    else:
        return jsonify(error="No se encontró el contacto."), 404
