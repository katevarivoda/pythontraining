__author__ = 'Ekaterina'

from model.contact import Contact
from model.group import Group
import pymysql

class DBFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), GroupName=name, GroupHeader=header, GroupFooter=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, `firstname`, `lastname` from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_tel_list(self):
        list_tel = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2) = row
                list_tel.append(
                    Contact(id = str(id), first_name = firstname, last_name = lastname, homephone=home,
                            mobile = mobile,
                            work = work, phone2 = phone2))
        finally:
            cursor.close()
        return list_tel

    def get_contact_mail_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2, email3) = row
                list.append(Contact(id = str(id), first_name = firstname, last_name = lastname, homephone=home,
                            mobile = mobile,
                            work = work, phone2 = phone2))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()
