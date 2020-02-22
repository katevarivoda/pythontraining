__author__ = 'Ekaterina'

from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(GroupName="Edited", GroupHeader="Edited", GroupFooter="Edited"))
    app.session.logout()
