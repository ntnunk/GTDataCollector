class Challenge(object):
    def __init__(name=None, allow_virtual=True, allow_trainer=True, 
                 group_id=None, group_name=None, db_path=None,
                 db_file=None, contact_list=None):
        self.name = name
        self.allow_virtual = allow_virtual
        self.allow_trainer = allow_trainer
        self.group_id = group_id
        self.group_name = group_name
        self.dp_path = os.path.join(db_path, db_file)
        contact_list = contact_list

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

    def set_contact_list(self, contact_list):
        self.contact_list = contact_list

    def get_contact_list(self):
        return self.contact_list

