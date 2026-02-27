# By Nolan Nelsen
# Written on 2/27/2026
# Tax Rate

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def tax_calculator(total_sales):
    state_sales_tax = 0.05
    county_sales_tax = 0.025

    total_state_tax = state_sales_tax * total_sales
    total_county_tax = county_sales_tax * total_sales
    total_tax = total_state_tax + total_county_tax

    return total_state_tax, total_county_tax, total_tax

total_sales = float(input("Enter the total sales this month: $"))

total_state_tax, total_county_tax, total_tax = tax_calculator(total_sales)

print("Total sales tax is: $", format(total_state_tax, '.2f'))
print("Total county tax is: $", format(total_county_tax, '.2f'))
print("Total tax is: $", format(total_tax, '.2f'))
