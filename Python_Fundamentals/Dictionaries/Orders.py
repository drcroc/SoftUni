# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
#     • If the product doesn't exist yet, add it with its starting quantity.
#     • If you receive a product, which already exists,
#     increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
#     • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
#     • The product data is always delimited by a single space.
# Output
#     • Print information about each product in the following format:
# "{product_name} -> {total_price}"
#     • Format the total price to the 2nd digit after the decimal separator.

command = ''
menu = {}
price = 'price'
quantity = 'quantity'

while command != 'buy':
    command = input()
    if command == 'buy':
        break

    product_name, product_price, product_quantity = command.split()
    product_price = float(product_price)
    product_quantity = int(product_quantity)

    menu[product_name] = menu.get(product_name, {})
    menu[product_name][price] = menu[product_name].get(price, 0)
    menu[product_name][quantity] = menu[product_name].get(quantity, 0)

    menu[product_name][price] = product_price
    menu[product_name][quantity] += product_quantity


for menu_items in menu:
    order = menu[menu_items][price] * menu[menu_items][quantity]
    print(f'{menu_items} -> {order:.2f}')























