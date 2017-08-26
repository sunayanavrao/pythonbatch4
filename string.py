def string(s):
    f=s.split(";")
    n=len(f)
    l={}
    for x in range(0,n):
        l[x]=f[x].split("=")
    for x in range(0,n):
        p[x]=((l[x][0]),(l[x][1]))
    return p

s=input("enter string")
p=string(s)
print (p)
