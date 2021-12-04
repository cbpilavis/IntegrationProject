_author_ = "ChrisPilavis"


# Name: Chris Pilavis
# This program in intended to incorporate and display
# some of the basic functions and uses when programming in 'Python 3'.
# Aid for this assignment was obtained from the course website
# (https://sites.google.com/view/profosheroff/courses/cop1500/integration-project) as well as geeksforgeeks.org.
# This program is simply a compilation of learned skills so far;
# the ultimate idea for this project has yet to be determined.

def number_input(prompt_here):
    """This function makes sure the input from the user is returned as an integer.

    Parameters -- Prompt entered asking the user a question
    Returns -- Any integer value entered by the user
    """
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input(prompt_here))
            valid_input = True
        except ValueError:
            print("Sorry, please enter a valid number.")
    return user_input


def main():
    """Compiles parts 1 & 2 of the integration project to be executed from calling Main."""
    print("Hello! Welcome to Part 1 of the Program.")
    visitor_status = number_input("How are you doing today on a scale from 1 - 10?: ")
    if visitor_status <= 0:
        print("Uh oh! That is not good.")
    elif visitor_status <= 4:
        print("It will hopefully get better!")
    elif visitor_status <= 7:
        print("That's not too bad!")
    elif visitor_status <= 10:
        print("It sounds like you're having a great day!")
    else:
        print("Greater than 10? That is crazy!")

    print("'Sep' Example: ")  # Sep example below(formats spacing)
    print("Let's say that you want to buy some laptops for Christmas.")
    print("We should find out the total cost! (including the sales tax of course)")
    num_laptops = number_input("How many laptops do you want to buy? #")
    laptop_cost = number_input("How much does the laptop cost? $")
    price = (num_laptops * laptop_cost) * 1.07
    print('Total cost of laptops: $', format(price, '.2f'), sep='')

    print("'End' Example: ")  # End example below(adds space instead of newline)
    print("This example shows how even if print statements ")
    print("are executed on different lines, they may not appear to be that way.")
    print("Hello! Welcome to the Program.", end=' ')
    print("I think im on a different line, even though I'm really not!")

    # Basic Calculations Section

    # Numeric Operators
    print("Next, let's practice doing some math.")
    num_decision = number_input(
        "Do you wish to execute the series of calculations? Type '1' for Yes or any other number for No. ")
    if num_decision == 1:
        print("Okay then! Here is the sample list:")
        print(2 ** 4)
        # Multiplies exponentially; will output 16, as 2 to the fourth power equals 16.
        print(2 * 4)
        # Multiplies 2 and 4 to produce 8 as a result.
        print(10 / 2)
        # Outputs the result of dividing 10 by 2, which is 5.
        print(10 % 3)
        # Outputs the remainder after division, producing 1 as the result.
        print(10 // 3)
        # Divides and removes any decimal points, producing 3 as the result.
        print(10 + 1)
        # Adds 10 and 1, giving 11.
        print(10 - 1)
        # Subtracts 1 from 10, giving 9.
    else:
        print("Okay, I will not do that then.")

    # String Operators
    print("Is it time?" * 4)
    # prints the string 4 times back-to-back.
    print("Oh wow, " + "look at the time!")
    # prints the first string followed by the second string.
    print("Thank you for visiting this sprint of the Project! Next time you visit there will be a lot more!...")
    # SPRINT 2
    print("...")
    print("Hello! Welcome back to Part 2 of the Integration Project.")
    print("For this section, lets create a program designed around working out and hitting personal records.")

    # below is an example of an 'if-else' statement & the '>' operator.
    print("Let's begin with a comparison of weights for the bicep curl exercise.")
    set1 = number_input("Enter the amount of weight (lbs) just performed for this exercise: ")
    max1 = number_input("Enter the maximum weight (lbs) ever performed for this exercise: ")
    if set1 > max1:
        print("Nice! Looks like that is a new personal record.")
    else:
        print("That is not a new personal record for this exercise.")

    # below is an example of an 'if' statement & the '!=' operator.
    print("Lets look at the number of reps performed between 2 sets.")
    set2 = number_input("Enter the amount of reps performed for the first set: ")
    set3 = number_input("Enter the amount of reps performed for the second set: ")
    if set2 != set3:
        print("You didn't perform the same amount of reps in both sets!")

    # below is an example of an 'if-elif' statement & the '==' operator.
    if set2 == set3:
        print("Good job! You did the same amount of reps.")
    elif set2 < set3:
        print("You did less in the first set!")

    # below is an example of an 'if-elif-else' statement.
    if set3 < set2:
        print("You did more in the first set.")
    elif set3 == set2:
        print("You did the same amount of reps for both!")
    else:
        print("You did more in the second set.")

    # 'not' example
    if not set2 > 10:
        print("You did less than 10 reps for the first set.")
    else:
        print("You didn't do less than 10 reps for the first set.")
    # 'and' example
    if set2 > 10 and set3 > 10:
        print("Nice! You did more than 10 reps for both sets.")

    # 'or' example
    if set2 or set3 == 10:
        print("It looks like you did 10 reps for at least one of the sets!")

    # Below is a 'while' and a shortcut operator example
    print("Lets count the reps for this set together.")
    count = 0
    reps1 = number_input("How many reps are we going to do for this exercise?: ")
    print("Lets begin!")
    while count < reps1 + 1:
        print(count)
        count += 1
    print("Okay, this set is all done!")

    # Below example includes 'for', 'range()', and 'in'.
    squat_reps = number_input("Enter the amount of squats we're going to do: ")
    print("Lets count em' together!")
    for squatCount in range(squat_reps + 1):
        print(squatCount)
    print("Wow, that was a lot!")

    # Lets define and call a function used to help us increase the number of reps we perform.

    print("Sometimes the best way to achieve comes from trying to overachieve;")
    print("lets try to go for double the amount of reps.")
    reps_we_hope = number_input("How many did you think of doing initially?: ")

    def more_reps(reps):
        """This function takes the number of reps from the user and doubles that number"""
        return 2 * reps

    a = more_reps(reps_we_hope)
    print("Okay, lets double that and do ", a, ".", sep='')
    print("Phew! That was pretty tiring wasn't it. Thanks for checking out the Integration Project.")
    print("There will be more the next time you visit!")


if __name__ == "__main__":
    main()
