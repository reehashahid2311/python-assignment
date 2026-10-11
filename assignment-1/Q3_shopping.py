products = []

def bill(products):
    return sum(item[1] * item[2] for item in products)


for i in range(5):
    print("\nProduct", i + 1)
    name = input("Product: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    products.append([name, price, quantity])

total = bill(products)
discount = total * 0.10 if total > 10000 else 0
final = total - discount
expensive = max(products, key=lambda item: item[1])

print("Total:", total)
print("Discount:", discount)
print("Final bill:", final)
print("Most expensive:", expensive[0])

with open("bill.txt", "w", encoding="utf-8") as file:
    for item in products:
        file.write(item[0] + " = " + str(item[1] * item[2]) + "\n")
    file.write("Total: " + str(total) + "\n")
    file.write("Discount: " + str(discount) + "\n")
    file.write("Final bill: " + str(final) + "\n")
    file.write("Most expensive: " + expensive[0])
