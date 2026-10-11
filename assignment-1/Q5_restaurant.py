menu = {
    1: ("Burger", 500),
    2: ("Pizza", 800),
    3: ("Fries", 250),
    4: ("Drink", 150)
}

orders = []

def bill(orders):
    return sum(item[1] * item[2] for item in orders)


while True:
    print("\n1. Burger - Rs. 500")
    print("2. Pizza - Rs. 800")
    print("3. Fries - Rs. 250")
    print("4. Drink - Rs. 150")
    print("0. Finish")

    choice = int(input("Choice: "))

    if choice == 0:
        break
    elif choice in menu:
        quantity = int(input("Quantity: "))
        orders.append([menu[choice][0], menu[choice][1], quantity])
    else:
        print("Invalid choice")


total = bill(orders)

for item in orders:
    print(item[0], item[1] * item[2])

print("Total bill:", total)

with open("orders.txt", "w", encoding="utf-8") as file:
    for item in orders:
        file.write(item[0] + " = " + str(item[1] * item[2]) + "\n")
    file.write("Total bill: " + str(total))
