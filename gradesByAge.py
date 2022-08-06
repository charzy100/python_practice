# Write a program that accepts input from user as age and places them in a school grade based on their input.Your codes should be 10 lines or less.
age = eval(input("Enter your age: "))
if age == 5:
    print("You should be in Kindergaten")
elif (age >= 6) and (age <= 17):
    print("You should be in grade school from 1 through 12")
elif (age > 17):
    print("Go to college")
