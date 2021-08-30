#in this program it will tell in wich year your will turn 100 



name = input("what is your name")
user_age = int(input("what is your age"))
how_many_time = int(input("how many time you want to print the sentence"))
year = 2021 - user_age + 100
y="Hello",name,"you will turn 100 in this year",year
if how_many_time > 999999:
    print("the number can not be more than 999999")
else:
    print(y*how_many_time)
 

