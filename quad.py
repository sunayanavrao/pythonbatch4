import cmath
def quad(a,b,c):
    t=((b*b)-(4*a*c))
    d=cmath.sqrt(t)
    r1=((-b)+d)/(2*a)
    r2=((-b)-d)/(2*a)
    return r1,r2
    
    

a=int(input("enter coeff of x2"))
b=int(input("enter coeff of x"))
c=int(input("enter coeff of x0"))
r1,r2=quad(a,b,c)
print (r1,r2)

