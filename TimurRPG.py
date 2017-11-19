print ("Teymur:\nHello traveler. What is it you want from our kingdom?")
print ("- SUCCESS - Teymur has joined your party!")
print ("\nTeymur\n-Strength 8\n -Dexterity 3\n -Intelligence 195\n -Luck 1\n -Stamina 2\n -Vitality 4")
print ("\nYou have been attacked by the swamp goblin!")
print ("What shall Teymur use:\n -Dab\n -Monkey yell\n -Seizure\n -Anime")
operation = input("What shall Teymur use:\n -Dab\n -Monkey yell\n -Seizure\n -Anime")

moves = ["Dab", "Monkey Yell", "Seizure", "Anime"]


if operation not in moves:
    print ("Please enter one of Teymur's abilities")
