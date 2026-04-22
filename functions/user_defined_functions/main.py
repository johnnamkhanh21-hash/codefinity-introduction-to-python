# Call the function and print the result

def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost


apples_total_cost = calculate_total_cost(price = 1.50, quantity = 10)
print(f"The total cost for apples is ${apples_total_cost}")

