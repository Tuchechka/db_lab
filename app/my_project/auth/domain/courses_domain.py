class Course:
    def __init__(self, course_id, title, description, duration_course):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.duration_course = duration_course

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'duration_course': self.duration_course
        }