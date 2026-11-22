"""Canary: price helper."""


def total_price(items):
    total = 0
    for item in items:
        total = total + item["price"] * item["qty"]
    return total


def totalPrice(items):  # duplicate of total_price under a different naming style
    return total_price(items)
# post-review fix push
