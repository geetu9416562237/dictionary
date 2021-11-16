# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in a:
#     for j in a:
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)



a={1:2,3:4,6:8,4:0}
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)