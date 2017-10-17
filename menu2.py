class menu:
        def __init__(self):
            self.Menu = {'Plain dosa':'25','Idly':'20','Upma':'30'}
        def show(self):
                print ('\n')
                print (self.Menu)
        def add(self,s,n):
                self.Menu[s] = n


c=menu()
class order:
        def __init__(self):
             self.ORDER= {}
        def  check(self,Menu,dish,count):
            for i in Menu:
                if i==dish:
                    self.ORDER[i]=Menu[i]
                    print (i,"is added to your order\n")
                    print (self.ORDER)
                    return count+int(Menu[i])
            print("given dish is not in the menu\n")
            return 0

o=order()
count=0
while(1):
    a = int(input("\n1.Display menu.\n2.order item.\n3.Exit with bill.\n"))
    if a==1:
        c.show()
    elif a==2:
        dish=input("enter the dish")
        count=o.check(c.Menu,dish,count)
    elif a==3:
        print ("amount:",count)
        break
    else: print("wring choice")
