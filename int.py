# a={"a":[1,2,3,4,5,6],"b":[7,8,9,10,11,12,13]}
# sum=0
# for i in a:
#     for j in a[i]:
#         sum=sum+j
# print(sum)

# a={"a":"geetu","sharma":"b"}
# b={}
# for i,j in a.items():
#     b[j]=[i]
# print(b)


# a="geetu"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# a="Geetu"
# s=a.split()                        
# p={}
# c=0
# for i in a:
#     p[c]=i
#     c+=1
# print(p)


# strong=input("enter something for strong password: ")
# if len(strong)>=6 and len(strong)<=12:
#     if ('a' in strong or 'b' in strong or 'c' in strong or 'd' in strong or 'e' in strong or 'f' in strong or 'g' in strong or 'h' in strong or 'i' in strong or 'j' in strong or 'k' in strong or 'l' in strong or 'm' in strong or 'n' in strong or 'o' in strong or 'p' in strong or 'q' in strong or 'r' in strong or 's' in strong or 't' in strong or 'u' in strong or 'v' in strong or 'w' in strong or 'x' in strong or 'y' in strong or 'z' in strong) and ('A' in strong or 'B' in strong or 'C' in strong or 'D' in strong or 'E' in strong or 'F' in strong or 'G' in strong or 'H' in strong or 'I' in strong or 'J' in strong or 'K' in strong or 'L' in strong or 'M' in strong or 'N'in strong or 'O' in strong or 'P' in strong or 'Q' in strong or 'R' in strong or 'S' in strong or 'T' in strong or 'U' in strong or 'V' in strong or 'W' in strong or 'X' in strong or 'Y' in strong or 'Z' in strong) and ('0' in strong or '1' in strong or '2' in strong or '3' in strong or '4' in strong or '5' in strong or '6' in strong or '7' in strong or '8' in strong or '9' in strong) and ('@' in strong or '$' in strong or '#' in strong):
#         print("strong password")
#     else:
#         print("wrong password")
# else:
#     print("invalid lenth")



# user=int(input("enter:"))
# k={}
# i=0
# t=1
# while i<=user:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         k[t]=i
#         t=t+1
#     i=i+1
# print(k)
# #         t+=1
# #         d[t]=i
# #     else:
# #         t+=1 
# #     i+=1
# # c=1
# # for i in d:
# #     k[c]=d[i]
# #     c+=1
# # print(k)


# n=int(input("enter a num:"))
# d={}
# i=1
# k=1
# while k<=n:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         d[k]=i
#         k=k+1
#     i=i+1
# print(d)

# a={"a":"geetu","b":"sharma","g":{"v":5,"c":7}}
# b={}
# for i,j in a.items():
#     b[i]=j
#     print(b)


# a=[["asuraj","hr",21,22000],["pawan","manager",22,20000],["ashok","fm",19,10000]]
# b=["name","desig","age","salary"] 
# c=["emp1","emp2","emp3"]
# d={}
# e={}
# for i in a:
#     for m in i:
#         for j in b:
#             for k in c:
#                 d[m]=k
#                 e[d[m]]=i
# print(e)



# a=[["suraj","HR",21,22000],["Pawan","manager",22,20000],["ashok","fm",19,10000]]
# b=["NAME","DESIG","AGE","SALARY"]
# c=["emp1","emp2","emp3"]
# dic0={}
# ic=0
# for i in a:
#     j=zip(b , i)
#     dic0[c[ic]]=dict(j)
#     ic+=1
# print(dic0)


# user=input("enter value")
# d=[{"name":"shailu","cash":40},{"name":"shailubujji","cash":50},{"name":"geethu","cash":60}]
# for i,j in d.values():
#     if user in i:
#         print(d[i])


# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")




