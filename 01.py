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

# ask 3rd user for their name and age and other details
name3 = input("Enter your name: ")
age3 = int(input("Enter your age: "))
address3 = input("Enter your address: ")
phone3 = input("Enter your phone number: ")

# print the details
print(f"Name: {name3}\nAge: {age3}\nAddress: {address3}\nPhone: {phone3}")

# comparing all 3 users' age
if age > age2 and age > age3:
    print(f"{name} is older than {name2} and {name3}")
elif age3 > age and age3 > age2:
    print(f"{name3} is older than {name} and {name2}")
else:
    print(f"{name2} is older than {name} and {name3}")


# comparing all 3 users' address
if address == address2 and address == address3:
    print("All users live at the same address.")
elif address == address2:
    print(f"{name} and {name2} live at the same address.")
elif address == address3:
    print(f"{name} and {name3} live at the same address.")
    

