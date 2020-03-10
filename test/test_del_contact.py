__author__ = 'Ekaterina'

from model.address import Address


def test_del_first_contact(app):
    app.contact.add_contact_if_empty()
    old_contacts = app.contact.get_contacts_list()
    old_contacts_length = len(old_contacts)
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert old_contacts_length - 1 == len(new_contacts)
    # удаляем первый элемент из старого списка
    # old_contacts[0:1] = []
    # assert old_contacts == new_contacts
