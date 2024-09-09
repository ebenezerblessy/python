def infinite(start=2):
    while True:
        yield start
        start += 1

# Generators can be used to create infinite sequences.
my_num = infinite()
for num in my_num:
    if num > 7:
        break
    print(num)
