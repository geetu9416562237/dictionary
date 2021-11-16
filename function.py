# n=1
# def my():
#     def my1():
#         n=3
#         print(n)
#     my1()
# my()
# print(n)

# def add (x,y):  
#     z=x+y
#     return z
# def sub (a,b):
#     c=a+b+add(3,2)
#     return c
# p=sub(5,5)
# print(p)

# def add (x,y):
#     z=x*y
#     return z
# def sub (a,b):
#     c=a+b*add(2,2)
#     return c
# p=sub(5,5)
# print(p)

# def div(x,y):
#     z=x%y
#     return z
# def sub(a,b):
#     c=a+b+div(26,4)
#     return c
# d=sub(4+5,6)
# print(d)

# def add (x,y):
#     z=x+y
#     return z
# n=int(input("enter the number:"))
# m=int(input("enter the number:"))
# def sub (a,b):
#     c=a+b+add(n,m)
#     return c
# p=sub(5,5)
# print(p)

# def add (a,b):
#     c=a+b
#     return c
#     # n=int(input("enter the number:"))
#     # i=0
#     # while i<=n:
#     #     print(i)
#     #     i=i+1
# add (2,4)
# def sub (c,d):
#     c=c+d+ add (c)


# with open("council.txt","w") as f:
#     f.write ("Disco - deepa")
#     f.write("\n")
#     f.write("T&P - shireen")
#     f.write("\n")
# with open("council.txt","r") as file:
#     f=file.read()
#     print(f)


# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers great than 20",num_list_sub_20)


# def my_list():
#     a=[1,5,2,10,11,13,5]
#     b=[5,10,20,16,17,3,3]
#     i=0
#     c=[]
#     while i<len(a):
#         if a[i] not in c:
#             c.append (a[i])
#             c.append (b[i])
#             c.sort()
#         i=i+1
#     print(c)
# my_list()



# def my_function():
#     i=0
#     while i<=3:
#         print("1.Mark zuckerberg")
#         print("2.Abhishek")
#         print("3.Kcr")
#         print("4.gudio van rossum ")
#         i=i+1
# print("who is the funder of facebook?")
# my_function()




# def ask_question():
#     print("1.Mark zuckerberg")
#     print("2.Abhishek")
#     print("3.Kcr")
#     print("4.gudio van rossum ")
# print("who is the funder of facebook?")
# ask_question()
# print("who is the  of co_funder navgurukul?")
# ask_question()
# print("who is the cm of telangana?")
# ask_question()
# print("who is the father of python ?")
# ask_question()

# def greet(names):
#     for name in names:
#         print("Welcome", name)

# print("Rinki", "Vishal", "Kartik", "Bijender")



# def harsad_number(m):
#     n=1
#     while n<=m:
#         r=n
#         sum=0
#         while r>0:
#             rem=r%10
#             sum=sum+rem
#             r=r//10
#         if n%sum==0:
#             print(n,"harsad number")
#         n=n+1
# user=int(input("enter the number:"))
# harsad_number(user)


# def prime_number(n):
#     i=1
#     while i<=n:
#         j=1
#         count=0
#         while j<=i:
#             if i%j==0:
#                 count+=1
#             j=j+1
#         if count==2:
#             print(i,"prime")
#         i=i+1
# user=int(input("enter the number:"))
# prime_number(user)



# def my_perfect(a):
#     per=1
#     while per<a:
#         i=1
#         sum=0
#         while i<per:
#             if per%i==0:
#                 sum+=i
#             i+=1
#         if per==sum:
#             print(per,"perfect number")
#         per+=1
# user=int(input("enter the number:"))
# print(my_perfect(user))



# n=int(input("enter the number:"))
# per=1
# while per<n:
#   i=1
#   sum=0
#   while i<per:
#        if per%i==0:
#            sum+=i
#        i+=1
#   if per==sum:
#        print(per,"perfect number")
#   per+=1


# def strong_number(s):
#     n=1
#     while n<=s:
#         m=n
#         sum=0
#         while m>0:
#             i=1
#             fact=1
#             rem=m%10
#             while i<=rem:
#                 fact=fact*i
#                 i=i+1
#             sum=sum+fact
#             m=m//10
#         if sum==n:
#             print(n,"strong number")
#         n=n+1
# us=int(input("enter the number:"))
# strong_number(us)


# for i in range(1,11):
#         print(5*i)




# def my_function(num1,num2):
#     a=num1+num2
#     return a
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# # operator=input("enter the opertion:")
# print(my_function(num1,num2))


# def list_sum(l1,l2):
#     i=0
#     c=[]
#     while i<len(l1):
#         m=my_function(l1[i],l2[i])
#         i=i+1
#         c.append(m)
#     return c
# print(list_sum([50, 60, 10] ,[10, 20, 13]))





# def fun(n):
#     i=0
#     a=[]
#     while i<len(n):
#         n=list2+list1
#         n.sort()
#         # print(n)
#         if n[i] not in a:
#             a.append(n[i])
#         i=i+1
#     print(a)
# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# fun(list2)




# 
# def my_function(n,m):
#     i=0
#     while i<len(n):
#         if n[i]%2==0 and m[i]%2==0:
#             print(n[i],"dono even hai")
#         else:
#             print("dono even nahi hai")
#         i=i+1
# my_function([2,6,18,10,3,75], [6,19,24,12,3,87])





# str = "geetu sharma"
# ASCII_values = []
# for character in str:
#    ASCII_values.append(ord(character))
# print(ASCII_values)


# ch="my name is saiprya"
# ascii=[]
# i=0
# while i<len(ch):
#    if ch[i]!=" ":
#       ascii.append(ord(ch[i]))
#    else:
#       pass
#    i=i+1
# print(ascii)



# ch="my name is saiprya"
# a=[]
# for i in ch:
#     if i!=" ":
#         a.append(ord(i))
# print(a)



# import random
# NUMDIGITS = 3
# MAXGUESS = 10

# def getSecretNum():
#   numbers = list(range(10))
#   random.shuffle(numbers)
#   secretNum = ''
#   for i in range(NUMDIGITS):
#     secretNum += str(numbers[i])
#   return secretNum
# def getClues(guess, secretNum):
#   if guess == secretNum:
#     return 'You got it!'
#   clue = []
#   for i in range(len(guess)):
#     if guess[i] == secretNum[i]:
#       clue.append('Fermi')
#     elif guess[i] in secretNum:
#       clue.append('Pico')
#     elif guess[i]!= secretNum[i]:
#       clue.append("bagle")
#   return ' '.join(clue)
# def isOnlyDigits(num):
#   if num == '':
#     return False
#   for i in num:
#     if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#       return False
#   return True
# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')
# while True:
#   secretNum = getSecretNum()
#   print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
#   numGuesses = 1
#   while numGuesses <= MAXGUESS:
#     guess=""
#     print("guess",numGuesses)
#     guess=input("enter the guess again:")
#     clue = getClues(guess, secretNum)
#     print(clue)
#     numGuesses += 1
#     if guess == secretNum:
#       break
#   print ('You ran out of guesses. The answer was ' + secretNum)
#   print("Do you want play again?('yes or no:'):")
#   playAgain=input("enter the ('yes or no:'):")
#   if playAgain=="yes":
#     continue
#   else:
#     break




def factorial(number):
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
print(factorial(4))