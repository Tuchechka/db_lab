class Test:
    def __init__(self, test_id, title, module_id, description, created_date):
        self.test_id = test_id
        self.title = title
        self.module_id = module_id
        self.description = description
        self.created_date = created_date

    def to_dict(self):
        return {
            'test_id': self.test_id,
            'title': self.title,
            'module_id': self.module_id,
            'description': self.description,
            'created_date': self.created_date,
        }