__author__ = 'Ekaterina'

from model.group import Group


def test_edit_group(app):
    group = Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_groups_list()
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_header(app):
    group = Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer")
    if app.group.count() == 0:
        app.group.create(Group(GroupHeader="test"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first_group(Group(GroupHeader="Test Header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)