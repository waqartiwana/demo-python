# ask 1st user for their name and age and other details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
phone = input("Enter your phone number: ")

# print the details
print(f"Name: {name}\nAge: {age}\nAddress: {address}\nPhone: {phone}")

# ask 2nd user for their name and age and other details
name2 = input("Enter your name: ")
age2 = int(input("Enter your age: "))
address2 = input("Enter your address: ")
phone2 = input("Enter your phone number: ")

# print the details
print(f"Name: {name2}\nAge: {age2}\nAddress: {address2}\nPhone: {phone2}")

if age > age2:
    print(f"{name} is older than {name2}")
else:
    print(f"{name2} is older than {name}")
