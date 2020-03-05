__author__ = 'Ekaterina'

from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(GroupName="test"))
    app.group.edit_first_group(Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer"))


def test_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(GroupHeader="test"))
    app.group.edit_first_group(Group(GroupHeader="Test Header"))
