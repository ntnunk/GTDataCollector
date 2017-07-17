import re
import os

class Challenge(object):
    def __init__(self, name=None, allow_virtual=True, allow_trainer=True, 
                 group_id=None, group_name=None, db_path=None,
                 db_file=None, contact_list=None):
        self.name = name
        self.allow_virtual = allow_virtual
        self.allow_trainer = allow_trainer
        self.group_id = group_id
        self.group_name = group_name

        if db_path is not None and db_file is not None:
            self.db_path = os.path.join(db_path, db_file)

        if contact_list is None:
            self.contact_list = []
        else:
            self.contact_list = contact_list

        self.export_path = None
        self.export_prefix = None
        self.export_type = None
        self.export_append_date = True

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_allow_virtual(self, allow_virtual):
        self.allow_virtual = allow_virtual

    def get_allow_virtal(self):
        return self.allow_virtual

    def set_allow_trainer(self, allow_trainer):
        self.allow_trainer = allow_trainer

    def get_allow_trainer(self):
        return self.allow_trainer

    def set_group_id(self, group_id):
        self.group_id = group_id

    def get_group_id(self):
        return self.group_id

    def set_group_name(self, group_name):
        self.group_name = group_name

    def get_group_name(self):
        return self.group_name

    def set_db_path(self, db_path):
        self.db_path = db_path

    def get_db_path(self):
        return self.db_path

    def set_contact_list(self, contact_list):
        self.contact_list = contact_list

    def get_contact_list(self):
        return self.contact_list

    def add_contact(self, firstname, lastname, email):
        contact = Contact(firstname, lastname, email)
        self.contact_list.append(contact)

    def set_export_info(self, path, prefix, export_type, append_date):
        self.export_path = path # Need to verify path
        self.export_prefix = prefix
        self.export_type = export_type
        self.export_append_date = append_date

class Contact(object):
    def __init__(self, firstname=None, lastname=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        if self.email_is_valid(email):
            self.email = email
        else:
            self.email = None

    def email_is_valid(self, email):
        if re.match('[^@]+@[^@]+\.[^@]+', email):
            return True
        return False

