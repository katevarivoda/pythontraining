__author__ = 'Ekaterina'

from fixture import contact
from random import randrange
import re
from model.contact import Contact


def test_contact(app):
    contact = app.contact.get_contacts_list()
    index = randrange(len(contact))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


# def test_contact_db_home(app, db):
#     contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
#     contacts_on_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
#     for i in range(len(contacts_on_home_page)):
#         contact_from_home_page = contacts_on_home_page[i]
#         contact_from_db = contacts_db[i]
#         assert contact_from_home_page.id == contact_from_db.id
#         assert contact_from_home_page.first_name == contact_from_db.first_name
#         assert contact_from_home_page.last_name == contact_from_db.last_name
#         assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
#         assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)

def test_phones_on_homepage(app, db):
    contacts_from_homepage = app.contact.get_contacts_list()
    contacts_from_db = db.get_contact_list()
    for contact_from_homepage in contacts_from_homepage:
        id_contact = contact_from_homepage.id
        for contact_from_db in contacts_from_db:
            id_contact2 = contact_from_db.id
            if id_contact == id_contact2:
                assert contact_from_homepage.last_name == contact_from_db.last_name
                assert contact_from_homepage.first_name == contact_from_db.first_name


def test_phones_on_contact_view_page(app):
    contact = app.contact.get_contacts_list()
    index = randrange(len(contact))
    contact_from_view_page = app.contact.get_contacts_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobile,
                                                            contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))
