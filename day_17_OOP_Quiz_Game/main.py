from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# import random
# rand_data = random.choice(question_data)
# new_question = Question(rand_data['text'], rand_data['answer'])
# print(new_question.text)

question_bank = []

for entry in question_data:
    # question_text = entry['text']
    # question_answer = entry['answer']
    questions_list = Question(entry['text'], entry['answer'])
    question_bank.append(questions_list)

quiz = QuizBrain(question_bank)

while quiz.question_number < len(question_bank):
    quiz.next_question()
print(f"You completed the Quiz. Your final score is {quiz.score} / {quiz.question_number}")