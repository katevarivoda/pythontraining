__author__ = 'Ekaterina'

from model.address import Address


def test_edit_contact(app):
    app.contact.edit_first_contact(
        Address(last_name="Ivan", first_name="Ivan", address="New York", phone="00000", address2="Moscow",
                note="Not important"))
