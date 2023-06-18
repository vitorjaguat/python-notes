from question_model import Question
from data import question_data, question_data2
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

question_bank_2 = []
for question in question_data2:
    q = Question(question["question"], question["correct_answer"])
    question_bank_2.append(q)

quiz = QuizBrain(question_bank_2)

while quiz.still_has_questions():
    quiz.next_question()

print("Your've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print("")