class User:
    def __init__(self, user_id, name, email, phone_number, registration_date):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.registration_date = registration_date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'registration_date': self.registration_date
        }