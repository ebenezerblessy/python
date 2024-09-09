import random

# random number from 0 to 1
print(random.random())
# Output 0.16123124494385477

# random number from 10 to 20
print(random.randint(10, 20))
# Output 18

# random number from 10 to 20 with step 2
print(random.randrange(10, 20, 2))


print(random.uniform(5.5, 25.5))



print(random.choice([10, 20, 30, 40, 50]))



print(random.sample([10, 20, 30, 40, 50], k=3))



print(random.choices([10, 20, 30, 40, 50], k=3))



x = [10, 20, 30, 40, 50, 60]
random.shuffle(x)
print(x)



random.seed(2)
print(random.randint(10, 20))

random.seed(2)
print(random.randint(10, 20))