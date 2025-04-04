# Write a program that prints numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)


# Given a list of colors, print each color along with its index.
# colors=['red','pink','yellow','green']
# for index,item in enumerate(colors):
#     print(f"{index}={item}")


# Ask the user to enter a word, then print its reverse using a for loop.
# word=input("enter word")
# reverse = ""
# for char in word:
#     print(char)
#     reverse = char + reverse
# print(reverse)


# Ask the user to enter a number (1-7), then print the corresponding day of the week.
# user_action=input("enter the number")
# match user_action:
#     case '1':
#         print("Monday")
#     case '2':
#         print("Tuesday")
#     case '3':
#         print("Wednesday")
#     case '4':
#         print("Thursday")
#     case '5':
#         print("Friday")
#     case '6':
#         print("Saturday")
#     case '7':
#         print("Sunday")
#     case _:
#         print("Not day found")


# Ask the user to enter a number n and print the sum of the first n natural numbers.
# number=int(input("Enter the number"))
# sum=0
# for i in range(number+1):
#     sum=i+sum
#
# print(sum)


# Ask the user to enter a sentence and count how many vowels
# sentence = input("Enter the sentence: ")
# count = 0
# for i in sentence:
#     if i in 'aeiouAEIOU':
#         count=count+1
# print( count)


# Ask the user to enter a number and calculate its factorial.
# number=int(input("Enter the number"))
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
# print(fact)


# FizzBuzz Game (For Loop & match-case)
# for number in range(1, 21):
#     match (number % 3 == 0, number % 5 == 0):
#         case (True, True):
#             print("FizzBuzz")
#         case (True, False):
#             print("Fizz")
#         case (False, True):
#             print("Buzz")
#         case (False, False):
#             print(number)



# Ask the user to enter a number and print its multiplication table (up to 10)
# number=int(input("Enter the number"))
# for i in range(1,11):
#     print(number*i)


# Given a list of numbers, find the largest one using a for loop.
# numbers=['10','44','5362','12']
# max=0
# for i in numbers:
#     if int(i)>max:
#         max=int(i)
# print(max)