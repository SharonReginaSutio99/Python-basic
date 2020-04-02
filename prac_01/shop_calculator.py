def calculation(number_of_items):
    total_price = 0
    for i in range(number_of_items):
        price_input = float(input("Price of item: "))
        total_price += price_input
    return total_price


def main():
    number_of_items = int(input("Number of items: "))

    while number_of_items <= 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    else:
        total_price = calculation(number_of_items)
        print("Total price for", number_of_items, "items is ${:.2f}".format(total_price)+str("."))


main()
