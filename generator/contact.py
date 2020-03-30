__author__ = 'Ekaterina'

import getopt
import os
import random
import string
import sys

import jsonpickle
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(last_name="", first_name="", homephone="", work="", mobile="", email="", email2="", middlename="",
                    nickname="", title="", company="", homepage="")] + [
               Contact(last_name=random_string("last_name", 15), first_name=random_string("first_name", 15),
                       middlename=random_string("middlename", 15), nickname=random_string("nickname", 15),
                       homephone=random_string("homephone", 10), work=random_string("work", 10),
                       title=random_string("title", 10),
                       mobile=random_string("mobile", 15), company=random_string("company", 15),
                       email=random_string("email", 15), email3=random_string("email2", 15),
                       homepage=random_string("homepage", 15))
               for i in range(5)
           ]

file = "C:\PycharmProjects\pythontraining\data\contacts.json"
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
