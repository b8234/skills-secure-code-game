from collections import namedtuple
from decimal import Decimal, InvalidOperation

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_TOTAL = Decimal('999999.99')
MAX_QUANTITY = 100
MIN_QUANTITY = 1

def validorder(order: Order) -> str:
    """Validates an order according to business and security rules.

    - Only 'product' and 'payment' item types are allowed.
    - Amounts must be valid numbers convertible to Decimal.
    - Product quantity must be int and between MIN_QUANTITY and MAX_QUANTITY.
    - Payment quantity must be exactly 1.
    - Payments must exactly match product cost.
    - No order may exceed MAX_ORDER_TOTAL.

    Args:
        order: An Order object.

    Returns:
        A status string describing if the order is valid or specifying the error.
    """
    total_products = Decimal('0')
    total_payments = Decimal('0')

    for item in order.items:
        # Check type validity
        if item.type not in {'payment', 'product'}:
            return f"Invalid item type: {item.type}"

        # Validate amount
        try:
            amount = Decimal(str(item.amount))
        except (InvalidOperation, TypeError, ValueError):
            return f"Invalid amount: {item.amount}"

        # Validate quantity
        if not isinstance(item.quantity, int):
            return f"Invalid quantity type: {item.quantity} ({type(item.quantity)})"

        if item.type == 'product':
            if not (MIN_QUANTITY <= item.quantity <= MAX_QUANTITY):
                return f"Quantity out of range: {item.quantity}"
            total_products += amount * item.quantity
        elif item.type == 'payment':
            if item.quantity != 1:
                return f"Payments must have quantity 1, got: {item.quantity}"
            total_payments += amount

    if total_products > MAX_ORDER_TOTAL:
        return "Total amount payable for an order exceeded"

    if total_payments != total_products:
        diff = total_payments - total_products
        return f"Order ID: {order.id} - Payment imbalance: ${diff:.2f}"

    return f"Order ID: {order.id} - Full payment received!"
