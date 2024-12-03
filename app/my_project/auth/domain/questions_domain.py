class Question:
    def __init__(self, question_id, test_id, question_text, correct_answers):
        self.question_id = question_id
        self.test_id = test_id
        self.question_text = question_text
        self.correct_answers = correct_answers 

    def to_dict(self):
        return {
            'question_id': self.question_id,
            'test_id': self.test_id,
            'question_text': self.question_text,
            'correct_answers': self.correct_answers
        }