class menu:
        def __init__(self):
                self.Menu = {'Plain dosa':'25','Idly':'20','Upma':'30'}
        def show(self):
                print '\n'
                print self.Menu
        def add(self,s,n):
                self.Menu[s] = n


c=menu()
while(1):
    a = int(input("\n1.Display menu.\n2.Add item.\n3.Exit.\n"))
    if a==1:
        c.show()
    elif a==2:
        item=raw_input("enter the item")
        price=input("enter the price")
        c.add(item,price)
    elif a==3:
        break
    else: print("wring choice")
    
