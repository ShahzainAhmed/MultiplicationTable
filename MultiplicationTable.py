# Program to find Multiplication table (from 1 to 10) of any number given by the user as input.

# To take input from the user

num = int(input("Enter any number you want to find multiplication table of: "))

# For loop will Iterate 10 times from i = 1 to 10.
for i in range(1, 11): # in ranges first one is inclusive, second one = 11, is excluded.
   print(num, 'x', i, '=', num*i)
