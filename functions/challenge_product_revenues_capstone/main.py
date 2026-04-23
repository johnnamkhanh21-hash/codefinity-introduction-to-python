# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
 #wirte code here

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, qyt in zip(prices, quantities_sold):
       revenue.append(price * qyt)
    return revenue
def formatted_output(revenue):
    for product, rev in sorted(revenue):
    # Example of expected output line (do not remove):
        print(f"{product} has total revenue of ${rev}")
    
revenue_value = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue_value))
formatted_output(revenue_per_product)



