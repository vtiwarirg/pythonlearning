from question_model import Question
from quiz_brain import QuizBrain
from data import question_data, computer_science_questions

question_bank = []
for question in computer_science_questions["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
