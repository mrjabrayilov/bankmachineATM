import time

print("Welcome to Gasim ATM senter")
time.sleep(3)

print("Please insert the card")
time.sleep(2)

def checking_PIN(pin):
    if len(pin) != 4:
        print("PIN is wrong, please try again")
        time.sleep(1)
        return False

    else:
        print("Now you can withdrawal cash")
        time.sleep(3)
        return True


while True:
    pin = input("Please enter PIN: ")
    time.sleep(2)
    if checking_PIN(pin):
        break
    time.sleep(1)
#to show the user that in his accaout there is 500 euro
print("Your bank account balance: 500 euro")
time.sleep(2)



def checking_amount(amount):
    if int(amount) % 10 != 0:
        print("Sorry, we can provide only 10, 20, 50 and 100 euro papers. ")
        time.sleep(2)
    elif int(amount) > 500:
        print("Sorry on your bank account there is not this much money>")
        return False


    else:
        print("\nPlease wait while your transaction is being processed  ")
        time.sleep(5)
        return True



while True:
    amount = input("\nPlease enter amount in multiples of 10 euro: ")
    if checking_amount(amount):
        break
    time.sleep(3)

print("\nPlease take your card back")
time.sleep(3)
print("\nPlease take money.")
time.sleep(4)

print("\nThank you for choosing Gasim ATM")
time.sleep(2)







