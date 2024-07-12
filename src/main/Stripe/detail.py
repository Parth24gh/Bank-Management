import stripe
import time

def relatedBalance():
    print("\n--------------Stripe Authenticate--------------")
    key=input("\nEnter your Secret API key :")
    stripe.api_key = key
    
    try:
        balanceDetails = stripe.Balance.retrieve()
    except stripe.error.CardError as e:
        print('Status is: %s' % e.http_status)
        print('Code is: %s' % e.code)
        print('Param is: %s' % e.param) # param is '' in this case
        print('Message is: %s' % e.user_message)
    except stripe.error.RateLimitError as e:
        print("Too many requests made to the API too quickly. Please Try again.")
        pass
    except stripe.error.InvalidRequestError as e:
        print("Invalid parameters were supplied to Stripe's API")
        pass
    except stripe.error.AuthenticationError as e:
        print("Authentication with Stripe's API failed")
        print("maybe you changed API keys recently")
        pass
    except stripe.error.APIConnectionError as e:
        print("Network communication with Stripe failed")
        pass
    except stripe.error.StripeError as e:
        print("Some error occured")
        pass
    except Exception as e:
        print("Some error happened, completely unrelated to Stripe")
        pass

    print("\n--------------Choose Below--------------")
    print("1. See full Details.")
    print("2. Check Primary Balance.")
    print("Enter ~ to quit")
    a=input("\nEnter your choice:")

    if a=='1':
        length = len(balanceDetails["available"])
        for i in range(length):
            amount = balanceDetails["available"][i]["amount"]
            currency = balanceDetails["available"][i]["currency"]
            bank = ''
            card = ''
            if "bank_account" in balanceDetails["pending"][i]["source_types"]:
                bank = balanceDetails["pending"][i]["source_types"]["bank_account"]
            if "card" in balanceDetails["pending"][i]["source_types"]:
                card = balanceDetails["pending"][i]["source_types"]["card"]
            print("Available Balance: " , amount , " " , currency , " Source Type: Bank Acc. ", bank , ", card " , card)
        
        if "connect_reserved" in balanceDetails:
            length = len(balanceDetails["connect_reserved"])
            print("\nConnect Reserved:")
            for i in range(length):
                amount = balanceDetails["connect_reserved"][i]["amount"]
                currency = balanceDetails["connect_reserved"][i]["currency"]
                print("Amount: " , amount , " " , currency)
        
        print("\nlivemode : " , balanceDetails["livemode"])

        length = len(balanceDetails["pending"])
        print("\nPending:")
        for i in range(length):
            amount = balanceDetails["pending"][i]["amount"]
            currency = balanceDetails["pending"][i]["currency"]
            bank = ''
            card = ''
            if "bank_account" in balanceDetails["pending"][i]["source_types"]:
                bank = balanceDetails["pending"][i]["source_types"]["bank_account"]
            if "card" in balanceDetails["pending"][i]["source_types"]:
                card = balanceDetails["pending"][i]["source_types"]["card"]
            print("Amount: " , amount , " " , currency , " Source Type: Bank Acc. ", bank , ", card " , card)

    elif a=='2':
        amount = balanceDetails["available"][0]["amount"]
        currency = balanceDetails["available"][0]["currency"]
        print("Available Balance: " , amount , " " , currency)

    elif a=='~':
        print("Exiting")

    else:
        print("Enter a valid input")
