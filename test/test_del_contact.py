__author__ = 'Ekaterina'

import random

from model.contact import Contact
from random import randrange


def test_del_some_contact(app, db, check_ui):
    app.contact.contact_count()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_groups_list(), key=Contact.id_or_max)

