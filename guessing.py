# Specify a secret word then user will keep guessing until they get the secret word right
# Password checker

password = "Blue"
guess = " "
guess_count = 0
guess_limit = 2
out_of_guesses = False


while guess != password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your password ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Incorrect password")
else:
    print("Password correct")



