scoresList = [0, 0, 0, 0]

optionList = ["Blazing", "Hot", "Cold", "Freezing"]

print("When you are in a resturant on a summer day")
def ask(scroesList):
    print("A: Super hot")
    print("B: I'm ok, but it feels a bit on the warm inside")
    print("C: it's kinda of chilly, close the door")
    print("D: It's soo cold I need to get out of heere.")
    answer1 = input("answer")
    if answer1 == "A":
        scroesList[0] += 1
    if answer1 == "B":
        scroesList[1] += 1
    if answer1 == "C":
        scroesList[2] += 1
    if answer1 == "D":
        scroesList[3] += 1
    return scroesList

scroesList = ask(scoresList)
print("You are in your room on a winter day")
scoresList = ask(scroesList)
print("You go to take a shower at Mills Locker room")
scoresList = ask(scoresList)
print("You are on a 8 hour road trip to Navada")
scoresList = ask(scoresList)
print("You go to school, but weather is 50 degrees Farenhieght")
scoresList = ask(scoresList)
print("You run for 80 hours straight and you walk into the sauna")
scoresList = ask(scoresList)

print("Score for cool: {}\nScore for Hot: {}\nScore for Freezing: {}\nScore for Blazing: {}".format(scroesList[2], scoresList[1], scoresList[3], scoresList[0]))
