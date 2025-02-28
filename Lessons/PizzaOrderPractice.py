# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

S = 15
M = 20
L = 25

add_pepperoni_S_Y = 2
add_pepperoni_ML_Y = 3
extra_cheese_cost = 1

bill = 0

if size == 'S':
    bill += S
    if add_pepperoni == 'Y':
        bill += add_pepperoni_S_Y
    if extra_cheese == 'Y':
        bill += extra_cheese_cost

if size == 'M':
    bill += M
    if add_pepperoni == 'Y':
        bill += add_pepperoni_ML_Y
    if extra_cheese == 'Y':
        bill += extra_cheese_cost

if size == 'L':
    bill += L
    if add_pepperoni == 'Y':
        bill += add_pepperoni_ML_Y
    if extra_cheese == 'Y':
        bill += extra_cheese_cost
      
print(f"Your final bill is: ${bill}.")

###########################OR############################################

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")