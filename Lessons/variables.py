# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

#swapping the values of a and b
temp = a
a = b
b = temp


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#OR

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

# Initialize a list to hold the values of a and b
values = [a, b]

# Loop through the values and swap them
for i in range(len(values) // 2):
    values[i], values[-i - 1] = values[-i - 1], values[i]

# Assign the swapped values back to a and b
a, b = values

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
