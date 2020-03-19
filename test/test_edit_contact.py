__author__ = 'Ekaterina'

from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    contact = Contact(last_name="Nikitina", first_name="Kate", address="New York", homephone="123", address2="Moscow",
                      note="Not important", mobile="2345", work="3535", email="mail@go.ru")
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(last_name="Nikitina"))
        app.contact.redirect_to_home_page()
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_name(app):
#     contact = Address(first_name="Kate")
#     if app.contact.count() == 0:
#         app.contact.add_contact(contact)
#         app.contact.redirect_to_home_page()
#     old_contacts = app.contact.get_contacts_list()
#     app.contact.edit_first_contact(contact)
#     new_contacts = app.contact.get_contacts_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Address.id_or_max) == sorted(new_contacts, key=Address.id_or_max)
