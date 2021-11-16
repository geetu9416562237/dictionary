# l=[1,2,1,4,5,3,2]
# a=[]
# for i in l:
#     if i  not  in a:
#         a.append(i)
        
# print(a)


str="MISSISSIPPI"
c=0
b={}
for i in str:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)