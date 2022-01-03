num1 = int(input("Starting no ::"))
num2 = int(input("Ending no ::"))

for i in range(num1, num2):
    n = i
    s = 0
    while(n > 0):
        d = n % 10
        n = int(n/10)
        s = s + (d*d*d)
    if(s == i):
        print(i)
