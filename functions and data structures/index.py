def calculate_tax(bill, tax_rate):
    total_tax = bill * tax_rate / 100
    total_tax = round(total_tax, 2)
    print('Total_tax :', total_tax)


calculate_tax(175.00, 15)
calculate_tax(162.50, 25)
