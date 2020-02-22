__author__ = 'Ekaterina'

from model.address import Address


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Address(last_name="Ivan", first_name="Ivan", address="New York", phone="00000", address2="",
                note="Not important"))
    app.session.logout()
