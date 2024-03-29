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
# nested loop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)

# making our for code more "elegant"
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

#using conditionals in our "elegant loops"
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height * 1 for height in heights if height >161]
print(can_ride_coaster)

#loops module review
single_digits = range(0,10)
cubes = [digit * digit* digit for digit in single_digits ]
squares = []
for digit in single_digits:
  squares.append(digit * digit)
  print(digit)
  print(squares)
  print(cubes)


#final loops project
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)
new_prices = [price - 5 for price in prices]
print(new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)