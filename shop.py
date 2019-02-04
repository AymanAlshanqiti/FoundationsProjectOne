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
    # your code goes here!
    print("Our menu:")
    for key in menu:
        print("\"%s\" (KD %s)" % (key, menu[key]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print("\"%s\"" % (i))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print("\"%s\"" % (i))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
        return True

    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    customer_input = input('What\'s your order? (Enter the exact spelling of the item you want. Type \'Exit\' to end your order. \n')

    while customer_input != "Exit":
        
        if is_valid_order(customer_input) == True:
            order_list.append(customer_input)
            customer_input = input()

        else:
            customer_input = input('Sorry we don\'t have this item in our menu!, please try to enter another item. \n')

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total < 5:
        return False

    else:
        return True

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0.0
    # your code goes here!
    for order in order_list:
        if order in menu:
            total += menu[order]

        elif order in original_flavors:
            total += 2

        else:
            total += 2.750

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print("- %s" % i)

    total_price = get_total_price(order_list)
    print("That\'ll be KD %s" % total_price)
    if accept_credit_card(total_price) == True:
        print("This order is eligible for credit card payment.")

    else:
        print("This order is eligible for cash only.")

    print("Thank you for shopping at %s" % cupcake_shop_name)




