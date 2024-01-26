print("Quiz Number 1")

playing = input("Do you want to be quizzed?: ")

if playing != "yes":
    quit()
print("lets go to the quiz! ")
score = 0
answer = input("Number 1 - What is the capital of France?:  ")
if answer == "Paris":
    print("Correct")
    score += 5
else:
    print("Incorrect")
answer = input("Number 2 - What is the largest planet in our solar system?:  ")
if answer == "Jupiter":
    print("Correct")
    score += 5
else:
    print("Incorrect")
answer = input("Number 3 - What is the chemical symbol for gold?:  ")
if answer == "Au":
    print("Correct")
    score += 5
else:
    print("Incorrect")
answer = input("Number 4 - In physics, what is the formula for calculating force?:  ")
if answer == "F=ma":
    print("Correct")
    score += 5
else:
    print("Incorrect")
answer = input("Number 5 - Solve for x: 2x + 5 = 15:  ")
if answer == "5":
    print("Correct")
    score += 5
else:
    print("Incorrect")
print("you got " + str(score) + " out of 5 questions correct")
print("you got " + str(score/5 * 100) + "%")







