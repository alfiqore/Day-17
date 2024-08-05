class QuizBrain:

    def __init__(self, question_data):
        self.question = None
        self.choice = None
        self.number_question = 0
        self.question_list = question_data
        self.score = 0

    def next_question(self):
        self.question = self.question_list[self.number_question]
        self.choice = input(f"Q.{self.number_question + 1} : {self.question.text} (True/False)? ")
        self.number_question += 1
        self.check_answer()

    def still_has_question(self):
        if self.number_question < len(self.question_list):
            return True
        else:
            print("That's all the questions!")
            print(f"Your final Score is {self.score}/{self.number_question}")

    def check_answer(self):
        if self.choice[0].lower() == self.question.answer[0].lower():
            self.score += 1
            print(f"That's right the answer is {self.question.answer}")
            print(f"Score: {self.score}/{self.number_question}")
        else:
            print(f"No, the answer is {self.question.answer}")
            print(f"Score: {self.score}/{self.number_question}")