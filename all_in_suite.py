////////count the digits without using inbuilt functions//

num=int(input("enter the number:"))
count=0
while num >0:
    num=num//10
    count=count+1
print("count:",count)


///////check the palendrome without using inbuilt function//

a=str(input("enter the word:"))
if str(a)==str(a)[::-1]:
    print("palendrome")
else:
    print("not")

/////////check the palendrome without using inbuilt function//

num=input("enter the number:")
if num == num[::-1]:
    print("palendrome")
else:
    print("not")

////////factorial without using inbuilt function//

num=int(input("enter the number:"))
fact=1
for i in range(2,num+1):
    fact=fact*i
print(fact)

/////// check the prime number using without using inbuilt functions///


num=int(input("enter the number:"))
for i in range(2,num):
    if num%i==0:
        print("not a prime")
        break
else:
    print("prime")

/////////// check the armstrong without using in built function//////

num=int(input("enter the number:"))
sum=0
temp=num
while temp > 0:
    digit=temp%10
    sum =sum+digit**3
    temp=temp//10
if sum==num :
    print ("armstrong")
else:
    print("not a armstrong")

////// sum of digits without using inbuilt function///////

num =int(input("enter the number:"))
sum=0
while num > 0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)

////////// count the digits without using inbuilt functions/////
num =int(input("enter the number:"))
count=0
while num > 0:
    num=num//10
    count=count+1
print(count)

//////// second largest number without using inbuilt function////
num =list(map(int,input("enter the numbers:").split()))
largest=num[0]
second=num[0]
for number in num:
    
    
    if number > largest:
        second= largest
        largest=number
    elif number > second and number != largest:
        second = number
print("largest number:",largest)
print("second number :",second)


///////// remove duplicates from list////

numbers=list(map(int,input("enter the number:").split()))
dup=[]
for num in numbers:
    if num not in dup:
        dup.append(num)
print(dup)

////////// even and odd in separate list ////////

num=list(map(int,input("enter the numbers:").split()))
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


///////// even and odd count check////

num=list(map(int,input("enter the numbers:").split()))
even=0
odd=0
for i in num:
    if i%2==0:
        even =even +1
    else:
        odd=odd+1
print(even)
print(odd)


