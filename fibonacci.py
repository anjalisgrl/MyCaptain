a=0
b=1
n=int(input("Enter the number of terms:"))

if n<0:
    print("Input invalid")
elif n==1:
    print(a)
else:
    print("The fibonacci sequence is: ")
    print(a, b , end=" ")
    for n in range (0,n):
        c=a+b
        a=b
        b=c
        print(c ,end=" ")
