#24331A05G8
#to calculate compound interest
p=float(input("enter the principal amount:"))
r=float(input("enter the annual interest rate (in %):"))
t=float(input("enter the time (in years):"))
n=int(input("enter the number of times interest is compound per year:"))
amount=p*(1+r/(100*n))**(n*t)
compoundinterest=amount-p
print("compound interest is:", compound interest)
print("total amount after ",t, "year is: ",amount)
