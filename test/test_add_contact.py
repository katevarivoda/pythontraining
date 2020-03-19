# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact_info = Contact(last_name="Nikitina", first_name="Kate", homephone="123 76 76", work="234", mobile="35353",
                           email="mail@mail.com")
    app.contact.add_contact(contact_info)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


