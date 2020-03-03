# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(GroupName="Test1", GroupHeader="Test", GroupFooter="Footer"))


def test_add_empty_group(app):
    app.group.create(Group(GroupName="", GroupHeader="", GroupFooter=""))

