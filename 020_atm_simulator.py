"""ATM Simulator
Deposit, withdraw, and check your balance.
Uses functions, error handling(try/except/else/finally), and while loops.
"""

def deposit(balance):
    try:
        amount= float(input("Amount to deposit: $"))
        
        if amount<=0:
            raise ValueError("Amount must be positive!")
            
        balance += amount
        
    except ValueError as e:
        print(f"❌ {e}")
    else:
        print(f"✅ Deposited ${amount:.2f}!  New balance: ${balance:.2f}")
    finally:
        print("Deposit attempt finished.\n")
    return balance

def withdraw(balance):
    try:
        amount= float(input("Amount to withdraw: $"))
        
        if amount<=0:
            raise ValueError("Amount must be positive!")
        if amount> balance:
            raise ValueError(f"Insufficient funds! Balance: ${balance:.2f}")
            
        balance -= amount
        
    except ValueError as e:
        print(f"❌ {e}")
    else:
        print(f"✅ withdrew ${amount:.2f}!  New balance: ${balance:.2f} ")
    finally:
        print("withdrawal attempt finished.\n")
    return balance

def check_balance(balance):
    print(f"💰 Current balance: ${balance:.2f}")
    
def main():
    print("🏦 Welcome to the ATM!")
    balance = 100.0
    
    while True:
        print("\nWhat do you want to do?")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Check balance")
        print("4) Exit")
        
        choice=input("\nYour choice: ")
        
        if choice == "1":
            balance = deposit(balance)
        elif choice =="2":
            balance = withdraw(balance) 
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print(f"Goodbye! Final balance: {balance:.2f}")
            break
        else:
            print("Invalid choice, try again!")
            
main()



