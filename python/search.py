list=[]
print("enter 10 numbers")
for i in range(10):
  list.append(int(input()))

print("enter the number to be searched")
num=int(input())
flag=0
i=0
for i in range(len(list)):
    if list[i]==num:
        flag=1
        break
    i=i+1
if flag==1:
    print("found")
else:
        print("not found")

    
        


