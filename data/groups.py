# -*- coding: utf-8 -*-
from model.group import Group



testdata = [
    Group(GroupName="Name1", GroupHeader="Header1", GroupFooter="Footer1"),
    Group(GroupName="Name2", GroupHeader="Header2", GroupFooter="Footer2")
]

# testdata = [
#     Group(GroupName=name, GroupHeader=header, GroupFooter=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]
