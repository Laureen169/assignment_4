#assignment 4 on Introduction to Python
#Enter the price of the house you wish to buy.
print("Enter the house price")
Price = int(input())

#Enter the credit score
print("Enter the credit score")
CreditScore = int(input())

#Enter the first name
print("Enter first name")
First_name = input()

#Enter the last name
print("Enter last name")
Last_name = input()

Fullnames = First_name + " " + Last_name

#Enter the email
print("Enter the email address")
Email_address = input()

#Enter the phone number
print("Enter the phone number")
Phone_no = input()

#Enter mailing address
print("Enter the mailing address")
Mailing_address = input()

#Enter the mailing
print("Enter the city")
City = input()

#Enter the mailing
print("Enter the zipcode")
Zipcode = input()


#Quality for loans with the best interest rate
if int(CreditScore >= 780 and 850):
    print("Extent credit")
    print("Zero down payment")
    Downpayment = 0.0 * Price


#Usually qualify loans with the best interest rate
elif int(CreditScore >= 740 and 779):
    print("Very Good")
    Downpayment = 0.2 * Price

#May face slightly higher loan interest
elif int(CreditScore >=720 and 739):
    print("Above average")
    Downpayment = 0.3 * Price

#May qualify for most loans of higher interest rates
elif int(CreditScore >= 680 and 719):
    print("Average")
    Downpayment = 0.6 * Price

#May qualify for most loans at significant higher interest rates
elif int(CreditScore >= 620 and 679):
    print("Bellow Average")
    Downpayment = 0.18 * Price

#Usually has some credit issues; will probably not qualify for most loans
elif int(CreditScore >= 580 and 619):
    print("Poor credit score")
    Downpayment = 0.20 * Price

#Facing extreme credit issues
else:
    int(CreditScore < 580)
    print("Poor credit score")
    Downpayment = 0.25 * Price
 

