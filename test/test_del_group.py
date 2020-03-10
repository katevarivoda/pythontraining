__author__ = 'Ekaterina'

from model.group import Group


def test_del_first_group(app):
    old_groups = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(GroupName="test"))
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

