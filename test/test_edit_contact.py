__author__ = 'Ekaterina'

from model.address import Address


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Address(last_name="Olga"))
        app.contact.redirect_to_home_page()
    app.contact.edit_first_contact(
        Address(last_name="Ivan", first_name="Ivan", address="New York", phone="00000", address2="Moscow",
                note="Not important"))


def test_edit_first_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Address(first_name="Olga"))
        app.contact.redirect_to_home_page()
    app.contact.edit_first_contact(Address(first_name="Violetta"))
