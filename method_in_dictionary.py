# a={"f":6,"g":4,"h":2}
# a=a.remove("h")
# print(a)

# a=int(input("enter a value"))
# i=0
# sum=0
# while i<a:

#     if a%i==0:
#         sum+=i
#     i+=1
# if sum ==a:
#     print("prefect num")


# a={1:[1,2,3],2:[5,5,6],5:[7,8,9]}
# sum=0
# for i  in a:
#     for j in a[i]:
#         sum+=j
#     print(sum)


a={3,4,5,6,7,8,9}
b={4,5,6,7,8,2,3}
c={3,4,5,6,2,1,8}
d={}
# for i in a:
    # for j in b:
        # for k in c:
d.update(a)
print(d)