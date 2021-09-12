
#combining lists into dictionary

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key,value in zipped_drinks}
print(drinks_to_caffeine)

# .get function practice

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

#used .pop to remove key:value from dictionary after retrieving it
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20 

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items, health_points)

# .values to return list of values in a dictionary
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exer in num_exercises.values():
  total_exercises += exer

print(total_exercises)

#using .items to grab key + values in a dictionary and printed a statement the exercise wanted including the keys/values.
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for women,occupation in pct_women_in_occupation.items():
  print("Women make up " +str(occupation) + " percent of " + women + "s.")



#made a list used a for loop to print using key:value
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)

spread["present"] = tarot.pop(22)

spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " +key+ " is the "+ value + " card.")

#Converted players and words in a key:value dictionary to calculate score
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters, points in zip(letters,points)}
letter_to_points[""] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE","TENNIS","EXIT"] , "wordNerd":["EARTH", "EYES", "MACHINE"],
"Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points+= score_word(word)
  player_to_points[player] = player_points
print(player_to_points)