__author__ = 'Ekaterina'

import random

from model.group import Group
from random import randrange


# randrange генерирует случайное целое число

def test_del_some_group(app, db):
    app.group.group_count()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
