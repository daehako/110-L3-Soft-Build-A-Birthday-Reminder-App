user_input = input("Which birthday are you looking for? ")
if user_input == "Jack":
  print("Birthday is 04/15/92!")
elif user_input == "Graham":
  print("Birthday is 07/12/89!")
else:
  print("Can't find a birthday for this person...")

# Prints "Can't find a birthday for this person..." when the user inputs a name that isn't in the dictionary is true. If the varable is False, it will print the birthday of the person that the user inputted.