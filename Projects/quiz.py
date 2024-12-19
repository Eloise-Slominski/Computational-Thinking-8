#Beginning
#starting values
winter_points = 0
summer_points = 0


#Middle
#question 1
answer = input("would you rather A) be cold, or B) be hot?")
if answer == "A":
    winter_points += 2
elif answer == "B":
    summer_points += 2

#question 2
answer = input("would you rather A) go swimming, or B) stay home and read?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

#question 3
answer = input("would you rather A) eat salad, or B) eat soup?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

#question 4
answer = input ("would you rather A) go skiing, or B) go surfing?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

#question 5
answer = input ("would you rather A) drink hot chocolate, or B) drink a milkshake?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

#question 6
answer = input ("would you rather A) listen to guitar, or B) listen to piano?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

#question 7
answer = input ("would you rather A) go to the mountains, or B) go to the beach?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

#End
#final score
if winter_points > summer_points:
    print ("You are a winter person!")
elif summer_points > winter_points:
    print ("You are a summer person")
elif winter_points == summer_points:
    print ("You are both!")
