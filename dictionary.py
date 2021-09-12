
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