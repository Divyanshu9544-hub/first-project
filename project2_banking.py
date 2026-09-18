balance = 0.0
kyc_documents = {}


def check_balance():
    print(f"Your current balance is {balance}")
    print("=========================")



def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposit a negative or zero amount")
        print("=========================")

    


def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw a negative or zero amount")
        print("=========================")
    elif amount >balance:
        print("Cannot  withdraw. Insufficient balance.")
        print("=========================")
    else:
        balance -= amount
    

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)



def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("=========================")

    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

        print("=========================")
    
        
    

def main():
    print("=========================")
    print("Welcome to SBI bank!!!!")
    print("=========================")

    while True:
        print("1. check your balance")
        print("2. Deposit an amount")
        print("3. withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")
        print("=========================")
        
        
        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = float(input("Emter the amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
            print("=========================")
        elif choice == "3":
            amt = float(input("Emter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdraw successfull")
            print("=========================")
        elif choice == "4":
            check_kyc()
        elif choice == "5":
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("Enter the documents type: ")
                value = input("Enter the documents number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYC updated!")
            print("=========================")

        
        elif choice == "6":
            print("Quiting, have a nice day. ")
            break
        else:
            print("Invalid choice!!! Re-try.")
            print("=========================")
        
        
        print("Thank you for banking with us! ")


if __name__ == "__main__":
    main()
