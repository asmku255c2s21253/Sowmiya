# 1.1 Inmpmement or recursive function to calculate the factorial of a given number 

"""
1!=1*1
2!=2*1!---2*1
3!=3*2!---3*2*1
.
.
10!=10*9!---10*9*8*7*6*5*4*3*2*1

formula-n*(n-1)!


def fact_ rec(n):
if n==0orn==1:
return1
else:
return n*fact_rec(n-1)

number=int (input("enter a value:"))
res=fact_rec(number)

print("thr factorial of{}is {}.".format(number,res))

