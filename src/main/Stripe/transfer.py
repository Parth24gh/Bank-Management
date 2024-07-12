import stripe
import time

def relatedTransfer():
    print("\n--------------Stripe Authenticate--------------")
    key=input("\nEnter your Secret API key :")
    stripe.api_key = key

    print("\n--------------Choose Below for Transfer--------------")
    print("1. Create Transfer.")
    print("2. Retrieve Transfer details.")
    print("3. Veiw all transfers.")
    print("4. Reverse a Transfer.")
    print("Enter ~ to quit")
    a=input("\nEnter your choice:")

    if a=='1':
        print("Please provide details for Transfer.")
        curr = input("Currency (3-letter ISO code for currency)\n 'usd' 'inr' 'gbp' etc. :")
        amountValue = float(input("Amount to transfer: "))
        amountCents = amountValue*100
        dest = input("The ID of a connected Stripe account: ")

        '''use of srcTransc variable:
        The default behavior is to transfer funds from the platform account's available balance. 
        Attempting a transfer that exceeds the available balance fails with an error. 
        To avoid this problem, when creating a transfer, tie it to an existing charge 
        by specifying the charge ID as the source_transaction parameter
        '''

        srcTransc = input("Give Source Transaction (Charge ID) (optional): ")

        srcType = input("Source Type (bank_account, card, or fpx) (optional): ")

        transferGrp = input("Transfer Group (optional): ")

        try:
            stripe.Transfer.create(
                amount=amountCents,
                currency=curr,
                destination=dest,
            )
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
            print("Some error occured, completely unrelated to Stripe")
            pass

        time.sleep(2)
        
    elif a=='2':
        id = input("Provide the transfer id. : ")
        try:
            retrieved = stripe.Transfer.retrieve(id,)
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

        amount = retrieved["amount"]
        currency = retrieved["currency"]
        id = retrieved["id"]
        destination = retrieved["destination"]
        transferGrp = retrieved["transfer_group"]
        srcType = retrieved["source_type"]

        print("Transfer data : " , amount , " " , currency , " , id. ", id , ", destination: " , destination , " , Transfer Group: " , transferGrp , " , Source Type: ", source_type)

        time.sleep(2)

    elif a=='3':
        try:
            transferHistory = stripe.Transfer.list(limit=3)
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
        
        length = len(transferHistory["data"])
        if(length==0):
            print("No Transfer History Found.")
        for i in range(length):
            amount = transferHistory["data"]["amount"]
            currency = transferHistory["data"]["currency"]
            id = transferHistory["data"]["id"]
            destination = transferHistory["data"]["destination"]
            transferGrp = transferHistory["data"]["transfer_group"]
            srcType = transferHistory["data"]["source_type"]
            print("Transfer data : " , amount , " " , currency , " , id. ", id , ", destination: " , destination , " , Transfer Group: " , transferGrp , " , Source Type: ", source_type)
        time.sleep(2)

    elif a=='4':
        print("Remember: Transfer reversals add to the platform's balance and subtract from the destination account's balance. \nReversing a transfer that was made for a destination charge is allowed only up to the amount of the charge. It is possible to reverse a transfer_group transfer only if the destination account has enough balance to cover the reversal.")
        amountValue = input(float("Enter the amount: "))
        amountCents = amountValue*100
        id = input("Provide the transfer id. : ")

        try:
            stripe.Transfer.create_reversal(
                id,
                amount=amountCents,
            )
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

        time.sleep(2)