__author__ = 'Ekaterina'

from model.group import Group
from random import randrange


def test_edit_group(app):
    group = Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_header(app):
#     group = Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer")
#     if app.group.count() == 0:
#         app.group.create(Group(GroupHeader="test"))
#     old_groups = app.group.get_groups_list()
#     app.group.edit_first_group(Group(GroupHeader="Test Header"))
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_groups_list()
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
