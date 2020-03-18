# -*- coding: utf-8 -*-
from model.address import Address


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact_info = Address(last_name="Nikitina", first_name="Kate", homephone="123", work="234", mobile="35353")
    app.contact.add_contact(contact_info)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Address.id_or_max) == sorted(new_contacts, key=Address.id_or_max)


