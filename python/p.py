list=[]
print("enter 5 numbers")
list.append(int(input()))
for i in range(5):
    if i%2==0:
        print("the number from the list in {} and it is EVEN".format(i))
    else:
        print("the number from the list is {} and it is ODD".format(i))