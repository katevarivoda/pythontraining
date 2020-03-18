from sys import maxsize


class Address:
    def __init__(self, last_name=None, first_name=None, address=None, homephone=None, work=None, mobile=None,
                 fax=None, address2=None, note=None, id=None, email=None):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.address2 = address2
        self.note = note
        self.id = id
        self.email = email

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
