# ---------------- SUPERMARKET BILLING SYSTEM ----------------

name = input("Enter your Name: ")

items_list = '''
------------------ ITEMS AVAILABLE ------------------
1: Rice               Rs 30/kg
2: Sugar              Rs 45/kg
3: Oil                Rs 140/kg
4: Salt               Rs 50/kg
5: Milk               Rs 40/packet
6: Water Bottle       Rs 20/bottle
7: Curd               Rs 35/packet
8: Meat               Rs 200/kg
-----------------------------------------------------
'''

print(items_list)

# Item dictionary
items = {
    1: ("Rice", 30),
    2: ("Sugar", 45),
    3: ("Oil", 140),
    4: ("Salt", 50),
    5: ("Milk", 40),
    6: ("Water Bottle", 20),
    7: ("Curd", 35),
    8: ("Meat", 200)
}

plist = []
qlist = []
pricelist = []

totalprice = 0
tax_rate = 0.18  # 18% GST

# ---------------- PURCHASE LOOP ----------------
while True:
    choice = input("Enter item number (0 to exit): ")

    if choice.isdigit():
        choice = int(choice)
    else:
        print("Invalid input! Enter a number")
        print('-' * 45)
        continue

    if choice == 0:
        break

    elif choice in items:
        quantity = input("Enter quantity: ")

        if quantity.isdigit():
            quantity = int(quantity)
        else:
            print("Invalid quantity")
            print('-' * 45)
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero")
            print('-' * 45)
            continue

        item_name, unit_price = items[choice]
        price = unit_price * quantity

        plist.append(item_name)
        qlist.append(quantity)
        pricelist.append(price)

        totalprice += price
        print(f"{quantity} {item_name}(s) added to cart")
        print('-' * 45)

    else:
        print("Item not available")
        print('-' * 45)

# ---------------- BILL GENERATION ----------------
if totalprice == 0:
    print("No items purchased.")
else:
    tax = totalprice * tax_rate
    finalprice = totalprice + tax

    print('-' * 45)
    print("       nikhiljagga SUPERMARKET")
    print('-' * 45)
    print(f"Customer Name : {name}")
    print('-' * 45)

    print("{:<15} {:>5} {:>7} {:>7}".format(
        "Item", "Qty", "Price", "Total"))
    print('-' * 45)

    i = 0
    while i < len(plist):
        print("{:<15} {:>5} {:>7} {:>7}".format(
            plist[i],
            qlist[i],
            pricelist[i] // qlist[i],
            pricelist[i]
        ))
        i += 1

    print('-' * 45)
    print(f"Subtotal     : Rs {totalprice:.2f}")
    print(f"GST (18%)    : Rs {tax:.2f}")
    print(f"Total Amount : Rs {finalprice:.2f}")
    print('-' * 55)
    print("Thank you for shopping with us pls visit us again")
    print('-' * 55)


