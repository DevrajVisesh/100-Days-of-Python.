#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

#The last line of your program should print the result.

#Example 1 Input
#39

#Example 1 Output
#12

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

print(type(two_digit_number))
result = int(two_digit_number[0]) + int(two_digit_number[1])

print(result)