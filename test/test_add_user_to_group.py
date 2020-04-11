__author__ = 'Ekaterina'

import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname", last_name="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(GroupName="gr_name", GroupHeader="gr_header", GroupFooter="gr_footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(first_name="Kate"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)


def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname", last_name="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(GroupName="testname", GroupHeader="testheader", GroupFooter="testfooter"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)
