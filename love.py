print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine the names and convert to lowercase
combined_string = name1.lower() + name2.lower()

# Count the occurrences of each letter in combined_string
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e

# Calculate the love predictor score
love_predictor = int(str(true) + str(love))

# Check the love predictor score and give a corresponding message
if love_predictor < 10 or love_predictor > 90:
    print(f"Your score is {love_predictor}, you go together like coke and mentos.")
elif 40 < love_predictor < 50:
    print(f"Your score is {love_predictor}, you are alright together.")
else:
    print(f"Your score is {love_predictor}.")
