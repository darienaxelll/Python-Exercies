############################################
#
#  Purpose: The purpose for this program is to calulate the tuition price change over the next 5 years. The tuition price will incerease 3% each year.
#  Developer: Darien Salazar
#  Date coded: 2/12/24
#  Verision 1.0.0
#
#############################################

tuition = float(8000)

print("Hello fellow student, here is an oversight of your tuition for the next 5 years.\n")
print(f"The current tution cost per semester is: ${tuition:,.2f}\n")

print("-" * 75)

for i in range(5):
    newTuitionPrice = tuition + (tuition * .03)
    print(f"On year {i + 1}, the tuition per semester will be: ${newTuitionPrice:,.2f}")
    tuition = newTuitionPrice

print("-" * 75)