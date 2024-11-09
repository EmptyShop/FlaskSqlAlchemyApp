from flask import Blueprint, redirect, render_template, url_for, flash
from models.contact import Contact
from utils.db import db
from utils.contactForm import ContactForm

bpcontacts = Blueprint('contacts', __name__)

@bpcontacts.route("/")
def index():
    contacts = Contact.query.all()
    
    form = ContactForm()
    action = "/new"
    form.submit.label.text = "Add"
    
    return render_template('home.html', 
                           form = form, action = action, contacts = contacts)

@bpcontacts.route("/new", methods = ['POST'])
def add_contact():
    form = ContactForm()

    fullname = form.fullname.data
    email = form.email.data
    phone = form.phone.data

    contact = Contact(fullname, email, phone)

    db.session.add(contact)
    db.session.commit()

    flash("Contact added successfuly.")

    return redirect(url_for('contacts.index'))

@bpcontacts.route("/update/<id>", methods = ['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get(id)
    form = ContactForm()
    
    if form.validate_on_submit():
        contact.fullname = form.fullname.data
        contact.email = form.email.data
        contact.phone = form.phone.data

        db.session.commit()

        flash("Contact updated successfuly.")

        return redirect(url_for('contacts.index'))
    else:
        action = f"/update/{id}"
        form.fullname.data = contact.fullname
        form.email.data = contact.email
        form.phone.data = contact.phone
        form.submit.label.text = "Update"
        return render_template('home.html',
                               form = form, action = action)

@bpcontacts.route("/delete/<id>")
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("Contact deleted successfuly.")

    return redirect(url_for('contacts.index'))