# Comparisons
def biggest_param(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(biggest_param(3, 4, 5))


is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male")
elif is_male and not(is_tall):
    print("Great")
else:
    print("Your are not male")