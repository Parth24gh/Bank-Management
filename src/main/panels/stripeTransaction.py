import stripe
from Stripe import detail
from Stripe import transfer
def panel():
    while(True):
        print("\n--------------Stripe Dash--------------")
        print("1. Transfers related.")
        print("2. Balance related.")
        print("Enter ~ to end process.")
        a=input("\nEnter your choice:")

        if a=='1':
            transfer.relatedTransfer()
    
        elif a=='2':
            detail.relatedBalance()
                
        elif a=='~':
            print("\nShutting down the program.")
            break
            
        else:
            print("\nWrong input!")