# Multiplication table (from 1 to 10)

num = 2

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11): # in ranges first one is inclusive, second one = 11, is excluded.
   print(num, 'x', i, '=', num*i)
