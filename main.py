from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    new_text = i["question"]
    new_answer =i["correct_answer"]
    new_q = Question(new_text, new_answer)
    question_bank.append(new_q)
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"well done ypur score is {quiz_brain.score} over {quiz_brain.question_number}")
