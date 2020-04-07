__author__ = 'Ekaterina'

from model.contact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    contact = Contact(last_name="Nikitina", first_name="Kate", address="New York", homephone="123", address2="Moscow",
                      note="Not important", mobile="2345", work="3535", email="mail@go.ru")
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(last_name="Nikitina"))
        app.contact.redirect_to_home_page()
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_groups_list(), key=Contact.id_or_max)


