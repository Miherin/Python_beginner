class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0        
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q. {self.question_number + 1}: {current_question.text} (true / false)?: ").lower()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_input, correct_answer ):
            if user_input == correct_answer.lower():
                self.score += 1
                print(f"Correct!. Score {self.score} / {self.question_number}\n")

            else:
                print(f"Incorrect!. Score {self.score} / {self.question_number}\n")
              