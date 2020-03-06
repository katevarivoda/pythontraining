__author__ = 'Ekaterina'


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def redirect_to_groups_tab(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.redirect_to_groups_tab()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.redirect_to_groups_tab()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.GroupName)
        self.change_field_value("group_header", group.GroupHeader)
        self.change_field_value("group_footer", group.GroupFooter)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.redirect_to_groups_tab()
        return len(wd.find_elements_by_name("selected[]"))
