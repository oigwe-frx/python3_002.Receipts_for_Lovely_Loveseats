# Item 1
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.""";

lovely_loveseat_price = 254.00;


# Item 2
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.""";

stylish_settee_price = 180.50


# Item 3
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.""";

luxurious_lamp_price = 52.15;


# Sales Tax - 8.8%
sales_tax = .088 


# Customer 1 Purchases:
customer_one_total = 0;
customer_one_itamization = "";

# Loveseat
customer_one_total += lovely_loveseat_price;

customer_one_itamization += lovely_loveseat_description;

# Lamp
customer_one_total += luxurious_lamp_price;

customer_one_itamization += luxurious_lamp_description;

# Sales Tax
customer_one_tax = customer_one_total * sales_tax;

customer_one_total += customer_one_tax;

print("Customer One Items:");
print(customer_one_itamization)
print("Customer One Total:");
print(customer_one_total);

