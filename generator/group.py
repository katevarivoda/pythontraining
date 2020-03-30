__author__ = 'Ekaterina'

import getopt
import json
import os.path
import random
import string
import sys

import jsonpickle

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(GroupName="", GroupHeader="", GroupFooter="")] + [
    Group(GroupName=random_string("name", 10), GroupHeader=random_string("header", 10), GroupFooter=random_string("footer", 10))
    for i in range(n)
]

# .. в этом случаей - переход на корневую директорию:
file = 'C:/PycharmProjects/pythontraining/data/groups.json'
#file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# открываем файл на запись:
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
