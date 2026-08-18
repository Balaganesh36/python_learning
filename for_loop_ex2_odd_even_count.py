a=int(input("Enter A :"))
b=int(input("Enter B :"))
e_count=0
o_count=0
for i in range(a,b):
    if(i%2==0):
        e_count=e_count+1
    else:
         o_count=o_count+1
print("The number of even numbers are",e_count)
print("the number of odd numbers are",o_count)
