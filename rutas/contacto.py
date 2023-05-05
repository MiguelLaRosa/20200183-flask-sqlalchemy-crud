from flask import Blueprint, render_template, request, redirect, url_for
from models.contacto import Contact
from utils.db import db

contactos = Blueprint("contacto", __name__)

# Creacion de las siguientes rutas

# Ruta que redirecciona al index


@contactos.route("/")
def index():
    contactos = Contact.query.all()
    return render_template('index.html', contactos=contactos)

# Ruta que registra un nuevo contacto


@contactos.route("/new", methods=["POST"])
def new():
    if request.method == "POST":
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        new_contact = Contact(fullname, email, phone)
        db.session.add(new_contact)
        db.session.commit()

    return redirect(url_for('contacto.index'))

# Ruta que actualiza un contacto por ID


@contactos.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    contacto = Contact.query.get(id)

    if request.method == "POST":
        contacto.fullname = request.form['fullname']
        contacto.email = request.form['email']
        contacto.phone = request.form['phone']

        db.session.commit()

        print('Updated successfully!')

        return redirect(url_for('contacto.index'))

    return render_template("update.html", contact=contacto)

# Ruta que elimina un contacto por ID


@contactos.route("/delete/<id>", methods=["GET"])
def delete(id):
    contacto = Contact.query.get(id)
    db.session.delete(contacto)
    db.session.commit()

    print('Deleted successfully!')

    return redirect(url_for('contacto.index'))
