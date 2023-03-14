from menu import products
from collections import Counter


def get_product_by_id(id: int):
    if not type(id) == int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type_of_prod: str):
    if not type(type_of_prod) == str:
        raise TypeError("product type must be a str")

    found_products = []

    for product in products:
        if product["type"] == type_of_prod:
            found_products.append(product)

    return found_products if len(found_products) > 0 else []


def generate_new_id(menu: list):
    big_id = 0

    for item in menu:
        if item["_id"] > big_id:
            big_id = item["_id"]

    return big_id + 1


def add_product(menu_to_insert: list, **kwargs):
    kwargs["_id"] = generate_new_id(menu_to_insert)
    menu_to_insert.append(kwargs)
    return kwargs


def get_most_common_type():
    all_types = list(prod["type"] for prod in products)
    ocurrency_count = Counter(all_types)
    max_ocurrency = 0
    most_common_type = ""

    for tp in ocurrency_count:
        if max_ocurrency < ocurrency_count[f"{tp}"]:
            max_ocurrency = ocurrency_count[f"{tp}"]
            most_common_type = tp

    return most_common_type


def menu_report():
    prod_count = len(products)
    prod_average = round(sum(prod["price"] for prod in products) / prod_count, 2)
    most_common_type = get_most_common_type()

    return f"Products Count: {prod_count} - Average Price: ${prod_average} - Most Common Type: {most_common_type}"
