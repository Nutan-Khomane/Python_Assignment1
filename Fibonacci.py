# write a python program to print the fibonacci series
f = 0
s = 1

print("Fibonacci series::", f, s, end="\t")

for i in range(1, 10):
    t = f+s
    print(t, end="\t")
    f = s
    s = t
