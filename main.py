from shop import (
    print_menu,
    print_originals,
    print_signatures,
    get_order,
    print_order,
)

print_menu()
print_originals()
print_signatures()
order_list = get_order()
print_order(order_list)