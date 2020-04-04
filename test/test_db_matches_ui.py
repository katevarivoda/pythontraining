__author__ = 'Ekaterina'

from model.group import Group


def test_group(app, db):
    ui_list = app.group.get_groups_list()
    def clean(group):
        return Group(id=group.id, GroupName=group.GroupName.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
