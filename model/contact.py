from sys import maxsize


class Contact:
    def __init__(self, last_name=None, first_name=None, address=None, homephone=None, work=None, mobile=None,
                 phone2=None, address2=None, note=None, id=None, email=None, email2=None, email3=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.address2 = address2
        self.note = note
        self.id = id
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
                    self.last_name == other.last_name) and (self.first_name == other.first_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
