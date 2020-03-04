__author__ = 'Ekaterina'

from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(GroupName="test"))
    app.group.delete_first_group()
