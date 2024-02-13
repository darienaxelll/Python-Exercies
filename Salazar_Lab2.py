##########################################################
#  Purpose: To calculate subtotal, total and grandtotal from a store visit.
#
#  Programmer: Darien Salazar
#  Date Written: 02/02/24
#  Version: 1.0.0
#
##########################################################
import datetime as dt

PEACHES_PRICE = 1.25
APPLE_PRICE = 0.75
PEARS_PRICE = 0.55
SALES_TAX = 0.0825
anwser = input("Would you like to shop?\n")

def shopping():
    print("Hello valued customer, welome to the grocery store! \n")

    today = dt.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    qtyPeaches = float(input("How many pounds of peaches do we have?\n"))
    qtyApples = float(input("How many pounds of apples do we have?\n"))
    qtyPears = float(input("How many pounds of pears do we have?\n"))
    total = (qtyApples * APPLE_PRICE) + (qtyPeaches * PEACHES_PRICE) + (qtyPears * PEARS_PRICE)
    taxes = (total * SALES_TAX)
    grandTotal = total + taxes

    print("\n")

    print(f"Date: {today}\n")
    print("Your total is: $" + "%.2f"%total + "\n")
    print("Your total taxes are: $" + "%.2f"%taxes + "\n")
    print("Your grand total is: $" + "%.2f"%grandTotal + "\n")

    print("Thank your for shopping with us! Come back soon.\n")

while anwser.lower() == "yes":
    shopping()
    anwser = input("Would you like to keep shopping?\n")
else:
    print("Thank your for shopping with us! Come back soon.\n")