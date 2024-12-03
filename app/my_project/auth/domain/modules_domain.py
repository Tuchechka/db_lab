class Module:
    def __init__(self, module_id, title, course_id, description_module):
        self.module_id = module_id
        self.title = title
        self.course_id = course_id
        self.description_module = description_module

    def to_dict(self):
        return {
            'module_id': self.module_id,
            'title': self.title,
            'course_id': self.course_id,
            'description_module': self.description_module
        }