list1 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the number: ")
for i in range(0, n): 
    num = int(input()) 
    list1.append(num) 
print(list1) 
for j in list1:
    if (j>=0):
        print(j, end = " ")
