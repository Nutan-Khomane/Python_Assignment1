num = int(input("Enter a no ::"))

sum = 0
num1 = num

while(num1 > 0):
    d = num1 % 10
    num1 = int(num1/10)
    sum = sum + d*d*d
if(num == sum):
    print("Given no is ArmStrong no")
else:
    print(" Given no is Not ArmStrong no ")
