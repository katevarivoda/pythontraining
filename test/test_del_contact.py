__author__ = 'Ekaterina'

from model.address import Address
from random import randrange


def test_del_some_contact(app):
    app.contact.contact_count()
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    old_contacts_length = len(old_contacts)
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert old_contacts_length - 1 == len(new_contacts)
    # удаляем первый элемент из старого списка
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
