"""Shopping Cart
Add items, remove them, see your cart and total price."""

def add_items(cart, *items):
    for item in items:
        cart.append(item)
        print(f"✅ {item['name']} added to cart!")
    
def remove_items(cart, name):
    for item in cart:
        if name.lower()== item["name"].lower():
            cart.remove(item)
            print(f"🗑️ {name} removed from cart!")
            return
    print(f"❌ {name} not found in cart!")

def show_cart(cart):
    if not cart:
        print("\n🛒 Your cart is empty!")
        return
    print("\n🛒 Your cart:")
    print("-"*30)
    for item in cart:
        print(f" {item['name']:<15} ${item['price']:.2f} ")
    print("-"*30)

def get_total(cart):
    prices=list(map(lambda item:item["price"], cart))
    return sum(prices)

def main():
    cart=[]
    print("🛍️ Welcome to the Shopping Cart!")
    while True:
        print("\nWhat do you want to do?")
        print("1) Add item(s)")
        print("2) Remove item")
        print("3) View cart")
        print("4) Checkout")
        print("5) Exit")
        
        choice=input("\nYour choice:")
        
        if choice == "1":
            name=input("Item name:")
            price=float(input("Price: $"))
            item={"name": name, "price": price}
            add_items(cart, item)
            
        elif choice== "2":
            name=input("Item name to remove:")
            remove_items(cart, name)
        
        elif choice== "3":
            show_cart(cart)
        
        elif choice== "4":
            show_cart(cart)
            if cart:
                total= get_total(cart)
                print(f"💰 Total: ${total:.2f}")
                print("Thanks for shopping!")
                break
        elif choice== "5":
            print("Goodbye!👋")
            break
        
        else:
            print("Invalid choice, try again!")
main()       
