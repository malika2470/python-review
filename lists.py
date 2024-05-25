friends = ["mini", "po", "dips", "twink"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[:3])

friends[1] = "Mike"
print(friends[1])

# Functions
lucky_num = [1, 2, 3, 4, 5]
friends = ["mini", "po", "dips", "twink"]
friends.extends(lucky_num)  # Add two lists together
friends.append("Creed")  # Add item to end of list
friends.insert(1, "Kelly")  # Add items to specific spots
friends.remove("Jim")  # Remove an element
friends.clear()  # Empty list


