__author__ = 'Ekaterina'

import random

from model.group import Group
from random import randrange

def test_edit_group(app, db, check_ui):
    group = Group(GroupName="Edited_Name", GroupHeader="Edited_Header", GroupFooter="Edited_Footer")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
