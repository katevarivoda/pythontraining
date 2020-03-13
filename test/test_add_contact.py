# -*- coding: utf-8 -*-
from model.address import Address


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact_info = Address(last_name="Nikitina", first_name="Kate")
    app.contact.add_contact(contact_info)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Address.id_or_max) == sorted(new_contacts, key=Address.id_or_max)


