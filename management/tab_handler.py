from menu import products


def get_product_price(id: int):
    for product in products:
        if product["_id"] == id:
            return product["price"]


def calculate_tab(tabs: list):
    subtotal = 0

    for tab in tabs:
        subtotal += tab["amount"] * get_product_price(tab["_id"])

    return {"subtotal": f"${round(subtotal, 2)}"}
