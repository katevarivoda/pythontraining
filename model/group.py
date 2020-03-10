from sys import maxsize


class Group:
    def __init__(self, GroupName=None, GroupHeader=None, GroupFooter=None, id=None):
        self.GroupName = GroupName
        self.GroupHeader = GroupHeader
        self.GroupFooter = GroupFooter
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.GroupName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.GroupName == other.GroupName

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
