# slicing strings 
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]

#slicing strings and used a function to return 
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)