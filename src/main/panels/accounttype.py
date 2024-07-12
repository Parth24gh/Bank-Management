from panels import adminpanel
from panels import employeepanel
from panels import clientpanel
from panels import stripeTransaction
def acctype(query,cur):
    while True:
        print("\n-------------Selector Menu--------------")
        print("1.Admin Acc.")
        print("2.Employee Acc.")
        print("3.Client Acc.")
        print("4.Stripe Transaction.")
        print("Enter ~ to end process.")
        a=input("\nEnter your choice:")
        
        if a=='1':
            b=input("\nEnter admin password:")
            if b=="admin123":
                adminpanel.ap(query,cur)
            else:
                print("\nWrong password!\n") 
            
        elif a=='2':
            b=input("\nEnter employee password:")
            if b=="emp123":
                employeepanel.ep(query,cur)
            else:
                print("\nWrong password!\n")
        
        elif a=='3':
            clientpanel.cp(query,cur)

        elif a=='4':
            stripeTransaction.panel()
            
        elif a=='~':
            print("\nShutting down the program.")
            break
        
        else:
            print("\nWrong input!")