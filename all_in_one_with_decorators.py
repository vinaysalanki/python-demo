//////// palendrome with decorators/////

import time
def timer(func):
    def wrapper(*arg,**kwargs):
        start=time.time()
        func(*arg,**kwargs)
        end=time.time()
        print("execution time:", {end-start}, "seconds")
    return wrapper
@timer
def pal(num):
    # num=input("enter the numb:")
    if num==num[::-1]:
        print("pal")
    else:
        print("not")
pal('234')
    
	
	////max and minimum with decorators////

import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func()
        end=time.time()
        print("execution time :",{end-start},"seconds")
    return wrapper
    
@timer
def max_min():
    a=list(map(int,input("enter the number:").split()))
    max=a[0]
    min=a[0]
    for num in a:
        if num > max:
            max=num
        else:
            num < min
            min=num
    print("maximum number:",max)
    print("minimum number:",min)
max_min()

//// even and odd with decorator///
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start =time.time()
        func(*args,**kwargs)
        end=time.time()
        print("execution time:",end-start,"seconds")
    return wrapper
@timer
def even_odd():
    num=list(map(int,input("enter the numbers:").split()))
    even=0
    odd=0
    even=sum([1 for i in num if i%2==0])
    odd=sum([1 for i in num  if i%2!=0])
    print(even)
    print(odd)
even_odd()

//// armstrong with decorators///

import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("execution time:",end-start)
    return wrapper
@timer
def arm():
    
    num = int(input("enter the number:"))
    total=0
    temp=num
    while temp > 0:
        digit=temp%10
        total=total+digit**3
        temp=temp//10
    if total==num:
        print("num is arm")
    else:
        print("num is not arm")
            
arm()

////prime with decorators///
import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("execution time:",end-start)
    return wrapper
@timer
def prime():
    num=int(input("enter the num:"))
    for i in range(2,num):
        if num%i==0:
            print("not a prime")
            break
    else:
        print("prime")
prime()


/// palendrome with decorators//
import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("execution time:",end-start)
    return wrapper
@timer
def pal():
    a=input("enter a string:")
    if a==a[::-1]:
        print("pal")
    else:
        print("not a pal")
pal()

///with decorators in frequency/////
import time 
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("execution time:",{end-start},"seconds")
    return wrapper

@timer
def frequency():
    num=input("enter the numbers:")
    freq={}
    for number in num:
        if number in freq:
            freq[number]=freq[number]+1
        else:
            freq[number]=1
    print(freq)
frequency()
    
        


    

    


    

    