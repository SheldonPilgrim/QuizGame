# This is a sample Python script.

print(f" Welcome to my computer game quiz!")
playing = input(" Do you want ot play the game? ")

# if playing does not equal yes then quiet the program or response is true
if playing != "yes":
    quit()
print(" Okey! lets play: ")
score = 0
answer = input(" What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print(" Correct!")
    score += 1
else:
    print("Incorrect")
answer = input(" What does RAM stand for? ")
if answer.lower() == "random access memory":
    print(" Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print(" inCorrect!")

answer = input("what does PC stand for? ")
if answer.lower() == "Personal Computer ":
    print(" Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("what does PSU stand for ")
if answer.lower() == "power supply":
    print(" Correct!")
    score += 1
else:
    print("Incorrect")
print(" You got " + str(score) + " questions correct!")
print(" You got " + str(score/5) * 100) + " %!")
