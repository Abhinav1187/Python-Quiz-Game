questions = ("Q1 : Python is an: ",
                       "Q2 : Python is designed by: ",
                       "Q3 : Python first appeared in: ",
                       "Q4 : Python filename extensions is/are: ",
                       "Q5 : Python influenced by: ")

options = (("A. interpreted, high-level, general-purpose programming language",
            "B. object-oriented programming language",
            "C. procedural, functional, structured, and reflective programming language",
            "D. All of the above"),
                   ("A. Guido van Rossum",
                    "B. James Gosling",
                    "C. Dennis Ritchie",
                    "D. Google"),
                   ("A. January 1982",
                    "B. February 1991",
                    "C. December 1987",
                    "D. July 2001"),
                   ("A. .py", "B. .pyi", "C. .pyc and .pyd", "D. All of the above"),
                   ("A. C and C++", "B. Java and Perl", "C. Lisp and Haskell", "D. All the above"))
answers = ("D", "A", "A", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
