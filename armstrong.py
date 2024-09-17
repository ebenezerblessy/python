num = int(input("Enter a number"))
sum = 0
temp = num

while temp>0:
    sum = sum + ( (temp%10)**3 )
    temp = temp // 10

if sum == num:
    print("armstrong number", sum)
else:
    print("not an Armstrong number")