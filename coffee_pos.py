MENU = {
    "americano": 50,
    "latte": 65,
    "cappuccino": 65,
    "mocha": 70,
    "matcha": 75,
}


def calculate_total(order_items, is_member=False):
    """คำนวณราคารวมค่ากาแฟ หักส่วนลดสมาชิก 10% และบวก VAT 7%"""
    if not order_items:
        raise ValueError("Order cannot be empty")

    subtotal = 0
    for item, qty in order_items:
        key = item.lower()
        if key not in MENU:
            raise KeyError(f"Menu item not found: {item}")
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")
        subtotal += MENU[key] * qty

    discount = subtotal * 0.10 if is_member else 0.0
    after_discount = subtotal - discount
    vat = after_discount * 0.07
    total = round(after_discount + vat, 2)

    return {
        "subtotal": subtotal,
        "discount": round(discount, 2),
        "vat": round(vat, 2),
        "total": total,
    }


def main():
    sample_order = [("Americano", 2), ("Latte", 1)]
    receipt = calculate_total(sample_order, is_member=True)
    print("=== SAU Coffee POS Receipt ===")
    print(f"Subtotal : {receipt['subtotal']} THB")
    print(f"Discount : -{receipt['discount']} THB")
    print(f"VAT (7%) : +{receipt['vat']} THB")
    print(f"Total    : {receipt['total']} THB")


if __name__ == "__main__":
    main()
    