from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

EPSILON = 0.0001
MAX_ORDER_TOTAL = 999999.99

def validorder(order: Order):
    """Validates an order by checking:
       - All items are of valid type.
       - Amounts and quantities are appropriate.
       - Payments match product total (within EPSILON).
       - Total payable does not exceed MAX_ORDER_TOTAL.

    Args:
        order: An Order instance containing items.

    Returns:
        A status string indicating whether the order is valid or specifying the error.
    """
    total_products = 0.0
    total_payments = 0.0
    total_payable = 0.0

    for item in order.items:
        # Ensure item type is either 'payment' or 'product'.
        if item.type not in {'payment', 'product'}:
            return "Invalid item type: %s" % item.type

        # Validate amount and quantity types and constraints.
        if not isinstance(item.amount, (int, float)):
            return "Invalid amount: %s" % item.amount
        if not isinstance(item.quantity, (int, float)) or item.quantity < 0:
            return "Invalid quantity: %s" % item.quantity

        if item.type == 'product':
            total_products += item.amount * item.quantity
            # Defensive: Only count positive values towards payable total.
            if item.amount * item.quantity > 0:
                total_payable += item.amount * item.quantity

        elif item.type == 'payment':
            total_payments += item.amount
            # Defensive: Only count positive payments towards payable total.
            if item.amount > 0:
                total_payable += item.amount

    net = total_payments - total_products

    # Check if payment matches product total (allowing for float error margin).
    if abs(net) > EPSILON:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)

    # Ensure total payable is within allowed limit.
    if total_payable > MAX_ORDER_TOTAL:
        return "Total amount payable for an order exceeded"

    return "Order ID: %s - Full payment received!" % order.id
