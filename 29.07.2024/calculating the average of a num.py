n = int(input("Number of Elements : "))  
l=[]  
for i in range(1,n+1):  
    element = int(input("Enter the element: "))  
    l.append(element)  
average = sum(l)/n  
print("Average of the elements in list",round(average,2))
