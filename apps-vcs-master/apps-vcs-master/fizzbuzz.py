#in this code when the user enter a number, if the number is divided by 3 it will print fizz 
#if the number is divisible by 5 it will print buzz 
# if the number is divisible by both 3 and 5 it will print "fizzbuzz"

a=int(input("enter number"))
if a%3 == 0 and a%5 == 0:
    print("fizzbuzz")
if a%3 == 0:
    print("fizz")
elif a%5==0:
    print("buzz")
else:
    print("invalid entry")