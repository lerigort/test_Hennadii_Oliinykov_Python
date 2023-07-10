import random
import time
# note: scroll to the bottom for the main()

def is_more_then_seven():
    # after 5 failed attempts cycle will be closed
    for i in range(5):
        answer = input("Input your number: ")

        # if left check fails, right part won't be executed, and invalid conversion won't cause crush
        # drop spaces and check if string is numeric
        if answer.strip().isnumeric():
            if int(answer) >= 7:
                print("Privet!")
            else:
                print("Number is less then seven.")
            break
        else:
            print("Your input is not a number.")
            print("But you can try again!")
            time.sleep(0.3)
    else:
        print("That was fun, but enough is enough.")


def are_u_the_Vyacheslav():
    compliments = ['Great', "Big", 'Casual', 'O\'Mighty',
                   "Mighty Burger Baron: The Revered Connoisseur of Grandiose Cheesemeals,\n \
                   Supreme Ambassador of Savory Delights, Champion of the Colossal Patty, and Guardian of the Gargantuan Buns"]

    # after 5 failed attempts user will be gently thrown out of asking cycle
    for i in range(5):
        # input is case-insensitive and resistant to leading and trailing whitespaces
        answer = input("Say your name (\"V\" is also valid if you don't want to be verbose): ").capitalize().strip()

        if answer == 'Vyacheslav' or answer == "V":
            # pick one random compliment for Vyacheslav
            random_integer = random.randint(0, len(compliments) - 1)
            print(f"You are Vyacheslav The {compliments[random_integer]}, indeed.")
            time.sleep(1)
            break
        else:
            print("There is no such name in guest list.\nTry again!\n")
            time.sleep(0.75)

        # I also wanted to add regex solution with fuzzy matching
        # for cases, when user misspelled 2 or 3 characters in name
        # but regex requires installation, so this functionality will not be added

    # gentle exit
    else:
        print("I see its kind of difficult to you. So let me handle it for you.")
        time.sleep(3)
        say_your_name = "Say your name (\"V\" is also valid if you don't want to be verbose): "
        name = 'Vyacheslav'

        # \r will clear line every iteration
        # end = "" won't allow to jump to the next line
        # say_your_name + name[:i] creates an illusion of input
        for i in range(len(name) + 1):
            print("\r", say_your_name + name[:i], end="")
            time.sleep(0.34)

        random_integer = random.randint(0, len(compliments) - 1)
        print(f"\nYou are Vyacheslav The {compliments[random_integer]}, indeed.")
        time.sleep(1)


def filter_dividable_by_three():
    # holder for numbers
    nums = []

    # create a list of numbers
    for i in range(100):
        manual_or_random = input("Do you want to use a random list (input \'r\') "
                                 "or insert numbers manually? (\'m\'): ").capitalize()

        # manual creation
        if manual_or_random == 'M':
            user_input = input("Please, print your numbers (use space for separation): ")
            is_there_invalid_inputs = False
            invalid_inputs = []

            # check all users inputs
            for number in user_input.split(" "):
                # some inputs may be valid, some not
                # we will omit invalid ones and collect all correct
                if number.isnumeric():
                    nums.append(int(number))
                else:
                    is_there_invalid_inputs = True
                    invalid_inputs.append(number)

            if is_there_invalid_inputs:
                print("\nSome of your numbers appears to be invalid (NaN of float).")
                print(f"This values will not be checked: {invalid_inputs}")
                time.sleep(1.5)
            # list of numbers has been created, proceed to check
            break

        # random generation
        elif manual_or_random == 'R':
            for _ in range(15):
                nums.append(random.randint(0, 100))
            # list of numbers has been created, proceed to check
            break

        # invalid input from user
        else:
            "Invalid input! Print 'm' to manually create list of integers, or 'r' to generate random numbers."
    else:
        print("Your persistence is admirable.")

    # if list is not empty
    if nums:
        print("\nThis is initial list of numbers: ")
        print(nums)
        print("This is all numbers in list, dividable by 3: ")
        print([x for x in nums if x % 3 == 0 and x != 0])
        time.sleep(4)
    # if list is empty
    else:
        print("\nThe list is empty.")
        time.sleep(0.5)


def main():
    print("Hello!")
    print("This is algorithm test from Hennadii Oliinykov.")
    print("I hope you'll enjoy this little application!)")
    time.sleep(1)

    user_input = ""
    while True:
        time.sleep(1)
        print("\nThere is three algorithms to work with.")
        print("Which one you want to choose?")
        print("1. More then seven.")
        print("2. Are you the Vyacheslav?")
        print("3. Find all dividable by three numbers.")
        print("0. Exit the application.\n")

        user_input = input("Please, choose one to proceed: ")
        user_input = user_input.strip()

        if user_input == "1":
            is_more_then_seven()
        elif user_input == "2":
            are_u_the_Vyacheslav()
        elif user_input == "3":
            filter_dividable_by_three()
        elif user_input == "0":
            break
        else:
            print("Invalid input! Please, try again.")

    print("\nGood luck, have a good day!")
    time.sleep(2)


main()
