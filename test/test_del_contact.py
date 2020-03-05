__author__ = 'Ekaterina'

from model.address import Address


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.redirect_to_contacts_tab()
        app.contact.add_contact(Address(last_name="Ark"))
        app.contact.redirect_to_home_page()
    app.contact.delete_first_contact()
