__author__ = 'Ekaterina'

from model.group import Group
from random import randrange


# randrange генерирует случайное целое число

def test_del_some_group(app):
    app.group.group_count()
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
