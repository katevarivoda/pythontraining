__author__ = 'Ekaterina'

from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(GroupName="Edited", GroupHeader="Edited", GroupFooter="Edited"))


def test_edit_header(app):
    app.group.edit_first_group(Group(GroupHeader="Test Header"))
