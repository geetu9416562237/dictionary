list1=["one","two","thhree","four","five"]
list2=[1,2,3,4,5,] 
b={}
for i in list1:
    for j in list2:
        b[i]=j
        list2.remove(j)  
        break
print(b)

