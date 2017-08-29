def dictionary(dic,n):
    d=" " 
    for i in dic:
         a=i
         b=dic[i]
         c=i+"="+dic[i]
         d=d+c+';'
    d=d[:-1]
    return d
    
n=int(input("enter no. of inputs"))
dic={}
for i in range (0,n):
    a=input("enter index")
    b=input("enter value")
    dic[a]=b

print (dic)
print (dictionary(dic,n)) 
