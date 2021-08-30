i=[]
n=int(input('enter how many numbers in list'))
for a in range(0,n):
    s=input(("numbers"))
    i.append(s)
    
set_r=set(i)
new_list=list(set_r)    
new_list.sort()
print(new_list[-2])