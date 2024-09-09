import random

random.seed(20)

for i in range(2):
    my_list = [10, 20, 30, 40]
    random.shuffle(my_list)
    print(my_list)
