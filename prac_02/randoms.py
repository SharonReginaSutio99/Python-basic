import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# What did you see on line 1? (random numbers ranging from 5-20)
# What was the smallest number you could have seen, what was the largest? (smallest 5, largest 20)


# What did you see on line 2? (random numbers of either 3,5,7,9)
# What was the smallest number you could have seen, what was the largest? (smallest 3, largest 9)
# Could line 2 have produced a 4? (no, because starting with 3, and stepping up 2 numbers. number after 3 will be 5)

# What did you see on line 3? (random decimal numbers ranging from 2.5 to 5.5, but all in 15 decimal places) What was
# the smallest number you could have seen, what was the largest? (smallest number would be 2.500000000000000 and
# largest number would be 5.500000000000000)

print(random.randint(1, 100))

# NOTES: random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# so random.randint(1,10) will produce a number from 1 to 10 inclusive eg. 1 or 3 or 10
