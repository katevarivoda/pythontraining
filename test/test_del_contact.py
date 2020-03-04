__author__ = 'Ekaterina'

from model.address import Address


def test_del_first_contact(app):
    if app.contact.count == 0:
        app.contact.add_contact(Address)
    app.contact.delete_contact()
