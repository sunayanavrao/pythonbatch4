dic={}
n=int(input("enter no. of inputs"))
for i in range (0,n):
    a=input("enter index")
    b=input("enter value")
    dic[a]=b

print (dic)
d=" " 
for i in dic:
     a=i
     b=dic[i]
     c=i+"="+dic[i]
     d=d+c+';'

d=d[:-1]
print (d) 
