import random
from pyscript import display, document


def handle_order(e):
    name = document.getElementById("customerName").value
    email = document.getElementById("customerEmail").value
    coffee_type = document.querySelector('input[name="coffeeType"]:checked').value
    quantity = document.getElementById("orderQuantity").value
    calculate_price = lambda coffee_type, quantity: {
        "Espresso": 35,
        "Latte": 35,
        "Cappuccino": 40,
        "Americano": 35
    }.get(coffee_type, 0) * int(quantity)
    sku_number = f"{coffee_type[:3].upper()}-{random.randint(100000, 999999)}"

    display(f"Name: {name}", target="summaryName", append=False)
    display(f"Email: {email}", target="summaryEmail", append=False)
    display(f"Coffee Ordered:{coffee_type}", target="summaryCoffeeType", append=False)
    display(f"Quantity: {quantity}", target="summaryQuantity", append=False)
    display(
        f"Total Price: ${calculate_price(coffee_type, quantity)}",
        target="summaryTotalPrice",
        append=False,
    )
    display(f"SKU Number: {sku_number}", target="summarySkuNumber", append=False)
