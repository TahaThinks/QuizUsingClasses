
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        selected_question = self.question_list[self.question_number]
        print(selected_question.text)
        received_answer = input("(True/False)")