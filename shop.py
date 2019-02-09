####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Tuwaiq Bakery"
signature_flavors = ["tuna", "salmon", "red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("\nOur menu:")
    for key in menu:
        print("\"%s\" (SR %s)" % (key, menu[key]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("\nOur original flavor cupcakes (SR %s each):" % original_price)

    for item in original_flavors:
        print("\"%s\"" % (item))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("\nOur signature flavor cupcake (SR %s each):" % signature_price)

    for item in signature_flavors:
        print("\"%s\"" % (item))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu or order in original_flavors or order in signature_flavors:
        return True

    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []

    print("\n   ---------------------------------")
    customer_input = input('\nWhat\'s your order? (Enter the exact spelling of the item you want. Type \'exit\' to end your order. \n')

    while customer_input.lower() != "exit":
        
        if is_valid_order(customer_input.lower()):
            order_list.append(customer_input)
            customer_input = input()

        else:
            customer_input = input('Sorry we don\'t have this item in our menu!, please try to enter another item. \n')

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total < 5:
        return False

    else:
        return True

    """ Anather way to write the condition """
    # return True if total > 5 else False 

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0.00

    for order in order_list:
        if order in menu:
            total += menu[order]

        elif order in original_flavors:
            total += original_price

        else:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print("\n   # --------------------------------- #")
    print("Your order is: ")

    for item in order_list:
        print("- %s" % item)

    total_price = get_total_price(order_list)
    print("That\'ll be SR %s" % total_price)
    if accept_credit_card(total_price) == True:
        print("This order is eligible for credit card payment.")

    else:
        print("This order is eligible for cash only.")

    print("Thank you for shopping at %s\n" % cupcake_shop_name)




