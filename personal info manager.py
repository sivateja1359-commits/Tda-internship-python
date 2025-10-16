#personal info manager 

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city:  ")
hobbies = input("Enter your hobbies : ")

print("\n--- Personal Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobbies: {hobbies}")

hobby_list = hobbies.split(",")
for hobby in hobby_list:
    print(f" - {hobby.strip()}")

print("\nThank you for using the Personal Information Manager!")