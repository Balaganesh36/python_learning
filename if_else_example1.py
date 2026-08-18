salary=int(input("Enter the salary :"))
age=int(input("Enter the age :"))
if(salary>=20000 or age<=25):
    loan_amount=int(input("Enter the loan amount :"))
    if(loan_amount<50000):
        print("Eligible for loan")
    else:
        print("maximum amount is 50000")
else:
    print("not eligible for loan")
