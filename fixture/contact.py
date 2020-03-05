__author__ = 'Ekaterina'


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def redirect_to_contacts_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def redirect_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.first_name)
        self.change_field_value("lastname", address.last_name)
        self.change_field_value("address", address.address)
        self.change_field_value("mobile", address.phone)
        self.change_field_value("address2", address.address2)
        self.change_field_value("notes", address.note)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_contact(self, address):
        wd = self.app.wd
        self.redirect_to_contacts_tab()
        self.fill_contact(address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, address):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(address)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))
