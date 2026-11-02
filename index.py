b=  ("ä".encode("utf-8"))

# print(bytes.decode(b, "utf-8"))
# print(f"{45}\t{9}\n{36}\t{type(6)}")
# i =1
# while i*i < 1000:
#     print(f"Squar of {i} is {i*i}")
#     i=i+1

# print("Hello, World!")
#
# arr = [0,5,8,9,4,8,9,7,6,4]
# i =0
# for i in range(len(arr)):
#     print(arr[i])
#     i+=1

# print("Finished printing")

from math import sqrt, log
# l=[1,3,65,3,-1,56,-10]
# for x in l:
#     if x < 0:
#         continue
#     print(f"Square root of {x} is {sqrt(x):.3f}")
#     print(f"Natural logarithm of {x} is {log(x):.4f}")

# print(f"{sqrt(4):.3f}")

# c = int(input())
# i=0
# a = [0 for i in range(c)]
# for i in range(c):
#     print("even number" if i%2==0 else "odd number")
# print(a)


# def func(x):
#     "This function multiplies its argument by two."

#     print( """ this function retuen pta ni """)

 
# print(bytes.decode(b, "utf-8"))
# print(f"{45}\t{9}\n{36}\t{type(6)}")
# i =1
# while i*i < 1000:
#     print(f"Squar of {i} is {i*i}")
#     i=i+1

# print("Hello, World!")
#
# arr = [0,5,8,9,4,8,9,7,6,4]
# i =0
# for i in range(len(arr)):
#     print(arr[i])
#     i+=1

# print("Finished printing")

from math import sqrt, log
# l=[1,3,65,3,-1,56,-10]
# for x in l:
#     if x < 0:
#         continue
#     print(f"Square root of {x} is {sqrt(x):.3f}")
#     print(f"Natural logarithm of {x} is {log(x):.4f}")

# print(f"{sqrt(4):.3f}")

# c = int(input())
# i=0
# a = [0 for i in range(c)]
# for i in range(c):
#     print("even number" if i%2==0 else "odd number")
# print(a)


# def func(x):
#     "This function multiplies its argument by two."

#     print( """ this function retuen pta ni """)
#     return x*2
# print(func(4))

# print("The docstring is:", func.__doc__)


# def func(a,b):
#     "This function adds two numbers."
#     return a**2 + b**2
# print(func.__doc__)
# print(func(5,a=4))
# print(1, 2, 3, end=' |', sep=' -*- ')
# print("first", "second", "third", end=' |', sep=' -*- ')

# def func(*a, b=2):
#     "Computes the length of the vector given as parameter. By default, it computes"
    
#     s =0 
#     for x in a :
#         s += abs(x)**b
#         return s**(1/b)

# print(func.__doc__)
# print(func(-7,9,7,2, b=5))    


# i = 78
# def f():
#     global i
#     i=7
#     print("Inside the function:", i)

# f()
# print("Outside the function:", i)


# def square(a):
#     return a**2
# def triple(a):
#     return a*3

# for i in range(10):
#     a =square(i)
#     b =triple(i)
#     if (a>b):
#        break
#     else:
#      print(f" square :{a}")
#      print(f" triple :{b}")
#      continue

# n = "ajay"
# print(n[0:1])
# print([0,1,2,3,4,5,6,7,8,9][:5])

# def func(a,b,c):
#  x1 = (-b + (sqrt((b**2) - 4*a*c)))/2*a
#  x2 = (-b - (sqrt((b**2) - 4*a*c)))/2*a
#  return(x1, x2)


# print(func(1,2,1))

# L=[11,13,22,32]
# L[2]=10          # Changes the third element

# L[1:3] = [7,9,7,9,10]
# print(L)

# L=range(3)
# for i in L:
#     print(i)
# # Note that L is not a list!
# print(L)

# L=[5,3,7,1]
# L.sort()      # here we call the sort method of the object L
# print(L)
# L2=[6,1,7,3,6]
# # L2.sort()
# print(sorted(L2))
# print(L2)
# L1=[]
# L2=["first", "second", "third"]
# print(zip(L1, L2))               # Note that zip does not return a list
# print(list(zip(L1, L2))) 

# days="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
# weathers="rainy rainy sunny cloudy rainy sunny sunny".split()
# temperatures=[10,12,12,9,9,11,11]
# for day, weather, temperature in zip(days,weathers,temperatures):
#     print(f"On {day} it was {weather} and the temperature was {temperature} degrees celsius.")

# def func(*a):
#    ans = []
#    for i in zip(*a):
#      ans.append(i)
     
#    return ans 
    
 


# print(func ([1,2,3],[20,30,40],['a', 'b', 'c']))



# L=[1,2,98,5,-1,2,0,5,10]
# counter = 0
# for i, x in enumerate(L):
#     if x == 5:
#         counter += 1
#         if counter == 2:
#             break
#     # print (i)
# print(x)

# s = {1,1,1}
# print(s) # {1, 2, 4}

# s = set([2,2,2,'a'])
# print(s) # {1, 5, 8, 'a'}

# print(1 in [1,2])
# d=dict(a=1, b=3)
# print("a" in d)


# def func(d):
#     fori


# d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}

# print(1 in [1,2])
# d=dict(a=1, b=3)
# print("b" in d)
# s=set()
# print(1 in s)
# print("x" in "text")

# first, second = [4,5]
# a,b,c = "bye"
# print(c)
# d=dict(a=1, b=3)
# k, key2 = d
# print(k, key2)

# d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
# def reverse_dictionary(d):
#     b = {}
#     for k, v in d.items():
#         for i in v:
#             b[i] = k
#     return b
            
# print(reverse_dictionary(d))

# 8


# a = int(input("Give the number "))

# # for i in range(1,11):
# #     print(f"{a*i}")

# # b = 0
# # for i in range (1, a):
# #     if a%i == 0 :
# #         b = b + i


# # if(b==a):
# #     print("a complete number")
# # else:
# #     print("not a complete number") 

# b = 0 
# for i in range(1, a+1):
#     if a%i == 0:
#       b = b+1
# if b == 2 :
#      print("your numer is prime")
# else:
#     print("no")




# a = "Ajay"

# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b +a[i]

# print(b)


# a = int(input("tell your number"))
# b=0
# while a > 0:
#    a = a//10
#    b=a 

# import random 

# num = random.randint(1,10)
# count =0


# while True:
#     guess = int(input("guess the number"))
#     if(guess == num):
#         print("correct number")
#         count +=1
#         break
    
#     elif guess < num:
#         print("go little higher")
#         count +=1
#     elif guess > num:
#         print("go little lower")
#         count +=1
#     else:
#         count +=1
#         print("sorry you are wrong")


# def pallindrom(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev +st[i]

#     if rev == st :
#         print("pallindrom")
#     else:
#         print("not pallindrom")

    
# pallindrom("name")

# pallindrom("NAMAN")

a = [10,2,20,180,90]

# def greatestNum (a):
    # GNum =  a[0]
    # Sg =a[0]
    # index = 0

    # for i in a:
    #    if i >GNum:
    #          Sg = GNum
    #          GNum = i
    #    elif i > Sg:
    #        Sg = i

    # print(Sg)

    # print( GNum, index)

# greatestNum(a)
# b = []
# z = 0
# for i in a:
#    if i < z :
#     b.append(i)

# print(b)

# help(set)

# d = {1:10, 2: 20, 3:30}

# d2 = {4:40, 5: 50, 6:60}

# s = 0
# for i in d2:
#     d[i] = d2[i]
#     s = d[i] + s +d2[i] 

# print(s)


a = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]

d= {}

for i in a :
    if i in d.keys():
        d[i] += 1
        
    else:
        d[i] =1


print(d)

