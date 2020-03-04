__author__ = 'Ekaterina'


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def redirect_to_contacts_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact(self, address):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % address.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % address.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % address.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % address.phone)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % address.address2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % address.note)

    def add_contact(self, address):
        wd = self.app.wd
        self.redirect_to_contacts_tab()
        self.fill_contact(address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, address):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(address)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
