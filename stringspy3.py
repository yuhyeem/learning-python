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

#spliced last 3 letters in strings 
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  last3f = first_name[len(first_name)-3:]
  last3L = last_name[len(last_name)-3:]
  temp = last3f + last3L
  return temp

temp_password = password_generator(first_name,last_name)

#forgot to commit, last exercise in multiple section string lesson. generating user and pass using more string slice techniques
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
