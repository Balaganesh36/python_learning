a=int(input("Enter A :"))
b=int(input("Enter B :"))
count=0
for i in range(a,b):
    if(i%2==0):
        count=count+1
        print(i)
print("number of even numbers is :",count)
