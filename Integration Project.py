#Name: Chris Pilavis
#This program in intended to incorporate and diplay some of the basic functions and uses when programming in 'Python 3'.
#Aid for this assignment was obtained from the course website
#(https://sites.google.com/view/profosheroff/courses/cop1500/integration-project) as well as geeksforgeeks.org.
#This program is simply a complaition of learned skills so far; the ultimate idea for this project has yet to be determiend.

print("Hello! Welcome to the Program.")
visitor_status = int(input("How are you doing today on a scale from 1 - 10?: "))
if visitor_status <= 0:
    print("Uh oh! That is not good.")
elif visitor_status <= 4:
    print("It will hopefully get better!")
elif visitor_status <= 7:
    print("That's not too bad!")
elif visitor_status <= 10:
    print("It sounds like your'e having a great day!")
else:
    print("That is crazy!")

print("'Sep' Example: ") #Sep example below(formats sapcing)
numLaptops = int(input("How many laptops do you want to buy? #"))
laptopCost = float(input("How much does the laptop cost? $"))
price = numLaptops * laptopCost
print('Total cost of laptops: $', format(price,'.2f'), sep='')

print("'End' Example: ") #End example below(adds space instead of newline)
print("Hello! Welcome to the Program.", end = ' ')
print("I think im on a different line, even though I'm really not!")

#Basic Calculations Section

    #Numeric Operators
num_decision = int(input("Do you wish to exectue the series of calculations? Type '1' for Yes or '2' for No. "))
if num_decision == 1:
    print("Okay then! Here is the sample list:")
    print(2 ** 4)
#Multiplies exponentially; will output 16, as 2 to the fouth power equals 16.
    print(2 * 4)
#Multiplies 2 and 4 to produce 8 as a result.
    print(10 / 2)
#Outputs the result of dividing 10 by 2, which is 5.
    print(10 % 3)
#Outputs the remainder after division, producing 1 as the result.
    print(10 // 3)
#Divides and removes any decimal points, producing 3 as the result.
    print(10 + 1)
#Adds 10 and 1, giving 11.
    print(10 - 1)
#Subtracts 1 from 10, giving 9.
else:
    print("Okay, I will not do that then.")

    #String Operators
print("Is it time?" * 4)
#prints the string 4 times back-to-back.
print("Oh wow, " + "look at the time!")
#prints the first string followed by the second string.
print("Thank you for visiting this iteration of the Program! Next time you visit there will be a lot more!")

print("Hello! Welcome back to Part 2 of the Integration Project.")
print("For this section, lets create a program designed around working out and hitting personal records.")

#below is an example of an 'if-else' statement & the '>' operator.
print("Let's begin with a comparison of weights for the bicep curl exercise.")
set1 = int(input("Enter the amount of weight just performed for this exercise: "))
max1 = int(input("Enter the maximum weight performed for this exercise: "))
if set1 > max1:
    print("Nice! Looks like that is a new personal record.")
else:
    print("That is not a new personal record for this exercise.")
    
#below is an example of an 'if' statement & the '!=' operator.
print("Lets look at the number of reps performed between 2 sets.")
set2 = int(input("Enter the amount of reps performed for the first set: "))
set3 = int(input("Enter the amount of reps performed for the second set: "))
if set2 != set3:
    print("You didn't perform the same amount of reps in both sets!")

#below is an example of an 'if-elif' statement & the '==' operator.
if set2 == set3:
    print("Good job! You did the same amount of reps.")
elif set2 < set3:
    print("You did less in the first set!")

#below is an example of an 'if-elif-else' statement.
if set3 < set2:
    print("You did more in the first set.")
elif set3 == set2:
    print("You did the same amount of reps for both!")
else:
    print("You did more in the second set.")

#'not' example
if not set2 > 10:
    print("You did less than 10 reps for the first set.")
else:
    print("You didn't do less than 10 reps for the first set.")
#'and' example
if set2 > 10 and set3 > 10:
    print("Nice! You did more than 10 reps for both sets.")

#'or' example
if set2 or set3 == 10:
    print("It looks like you did 10 reps for at least one of the sets!")

#Below is a 'while' and a shortcut operator example
print("Lets count the reps for this set together.")
count = 0
reps1 = int(input("How many reps are we going to do for this exercise?: "))
print("Lets begin!")
while count < reps1 + 1:
    print(count)
    count += 1
print("Okay, this set is all done!")

#Below example inlcudes 'for', 'range()', and 'in'.
squatReps = int(input("Enter the amount of squats we're going to do: "))
print("Lets count em' together!")
for squatCount in range(squatReps + 1):
    print(squatCount)
print("Wow, that was a lot!")

#Lets define and call a function used to help us increase the number of reps we perform.

print("Sometimes the best way to achieve comes from trying to overachieve; lets try to go for double the amount of reps.")
repsWeHope = int(input("How many did you think of doing initially?: "))

def moreReps(e):
    return 2*e
a = moreReps(repsWeHope)
print("Okay, lets double that and do ", a,".", sep = '')
print("Phew! That was pretty tiring wasn't it. Thanks for checking out the Integration Project, there will be more the next time you visit!")
