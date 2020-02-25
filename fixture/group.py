__author__ = 'Ekaterina'


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def redirect_to_groups_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.redirect_to_groups_tab()
        wd.find_element_by_name("new").click()
        self.fill_group(group)
        wd.find_element_by_name("submit").click()
        self.redirect_to_groups_tab()

    def delete_first_group(self):
        wd = self.app.wd
        self.redirect_to_groups_tab()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.redirect_to_groups_tab()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.redirect_to_groups_tab()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def fill_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.GroupName)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.GroupHeader)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.GroupFooter)
