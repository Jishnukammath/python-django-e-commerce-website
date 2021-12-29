
terms=int(input("how many terms.. : "))

n1,n2=0,1
temp=0

while temp <terms:
    print(n1)
    temp1 = n1+n2
    n1=n2
    n2=temp1
    temp += 1


