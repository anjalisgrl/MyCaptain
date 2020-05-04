#Assigning elements in list
list1 = ["Python", "Java", 45, 66]
print(list1)
list2 = [4, 9, 16, 25, 36 ]
print(list2)
list3 = ["Neeti", "Sanjana", "Sneha", "Myra"]
print(list3)
#copying or assigning a list to another list
#method1
list5 = list1.copy()
print(list5)
#method2
list6=[]
list6= list2[:] #slicing
print(list6)
#user input
list4 = []   
n = int(input("Enter number of elements : ")) 
print("Enter the number: ")
for i in range(0, n): 
    num = int(input()) 
    list4.append(num) 
print(list4)
 

#Acessing elements from tuple
tup1 = ("Python", "Java", 45, 66)
tup2 = (4, 9, 16, 25, 36, 49, 64)
print(tup1)
print(tup2)
#accessing through indexing
print ("tup1[0]: ", tup1[0])
#accessing through negative indexing
print ("tup1[-3]: ", tup1[-3])
#accessing through slicing
print ("tup2[2:6]: ", tup2[2:6])
print ("tup2[:]: ", tup2[:])


#Deleting different dictionary elements
#initialing dictionary items
dict1 = {"Name": "Anjali Bera",
        "Age": 20,
        "Branch": "IT",
        "State":"West Bengal"} 

print("Printing the dictionary items:")
print(dict1)
#removing entry with key "Name"
print("Printing the dictionary items after deleting the key \"Name\":")
del dict1["Name"]   
print(dict1)
#popping out with key "Branch"
print("Printing the dictionary items after popping the key \"Branch\"")
dict1.pop("Branch")  
print(dict1)
# removing all entries from dict1
print("Printing the dictionary after clearing all the dictionary items:")
dict1.clear()     
print(dict1)
# deleting the whole dictionary
print("Deleting the entire dictionary:")
del dict1        
print(dict1)

