character_name = "John"
character_age = 50
is_Male = False
print("There once was a man named " + character_name + ",")
print("He was about " + str(character_age) + " years old")
character_name = "Mike"
print("There once was a man named " + character_name + ",")
character_age = 50
print(f"his age was {character_age}")

# format will automatically do the conversion

character_name = "John"
character_age = 50
is_Male = False

print("There once was a person named {},".format(character_name))
print("They were about {} years old.".format(character_age))

character_name = "Mike"
print("There once was a person named {},".format(character_name))

