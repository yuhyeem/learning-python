board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]
# printing every game in the list board games
for game in board_games:
  print(game)
# printing every sport in the list sport games
for sport in sport_games:
  print(sport)

basketball_players = ["Lebron", "Westbrook", "I hate using the fucking arrow keys", "John Wall",]
# attempting to understand and run simple loops in one line for readability purposes
for players in basketball_players : print(players)
#Printing promise 5 times here
promise = "I will finish the python loops module!"
for temp in range(5):
  print(promise)

# doing my own version of this, printing 10 times
randomvariable = "arrow key spite"
for temp in range(10): print(randomvariable)


# Doing a while loop counting down from 10
countdown = 10
while countdown >= 0: 
  print(countdown);
  countdown -= 1
  
print("We have liftoff!")

# lets use a while loop to count down to 1 and then back up to 10
countdown2 = 10
while countdown2 >= 1:
    print(countdown2);
    countdown2 -= 1
while countdown2 <= 10:
    print(countdown2);
    countdown2 +=1
print("We down and up again")

# Here we mess with a while loop to print a statement that selects each element from the list using their index location 
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
  print("I am learning about", (python_topics[index]));
  index +=1 

# here I use a break and add an if statement for additional control in my loop
dog_breed_I_want = "dalmatian"
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    
    print("They have the dog I want!")
    break