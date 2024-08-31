from collections import OrderedDict

orders = OrderedDict()

def manage_orders(operation, product_name=None, quantity=None):
    """ Управление заказами с различными операциями: добавление, подсчет и список. """
    if operation == "add":
        if product_name and quantity is not None:
            if product_name in orders:
                orders[product_name] += quantity
            else:
                orders[product_name] = quantity
    elif operation == "total":
        return sum(orders.values())
    elif operation == "list":
        return list(orders.items())
    else:
        raise ValueError("Invalid operation. Use 'add', 'total', or 'list'.")

# Пример использования функции manage_orders
manage_orders("add", "Apples", 5)
manage_orders("add", "Bananas", 3)
manage_orders("add", "Oranges", 8)
manage_orders("add", "Apples", 2)  # Увеличиваем количество яблок

print(manage_orders("list"))   # Выводит список заказов в порядке добавления
print("Total products:", manage_orders("total"))  # Выводит суммарное количество всех продуктов
