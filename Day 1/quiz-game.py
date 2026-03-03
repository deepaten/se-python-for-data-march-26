
#Make a quiz app using Python!

#Store questions and answers in a list of dictionaries.
#Use a loop to ask each question.
#Keep score and display at the end.

quiz = [
    {"question": "What is 2 + 2?", "answer": "4", "category": "maths"},
    {"question": "What is the capital of France?", "answer": "Paris", "category": "geography" },
    {"question": "Is Python a snake or a programming language?", "answer": "programming language", "category": "programming"}
]
score = 0

# storing the category from user input
category = (input("Please choose category for the quiz (Maths, Geography, Programming): ). ")).lower()

category_cnt = 0

for q in quiz:
    if category in q["category"]:
        category_cnt+=1
        user_answer = input(q["question"] + " ")

        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")


print("Your score:", score, "/", category_cnt)