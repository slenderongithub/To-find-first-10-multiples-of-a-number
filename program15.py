#write a program to get the first 10 multiples of a number n

n=int(input("enter any number"))
for i in range(1,11):
    print(n, "X",i, "=", (n*i))
