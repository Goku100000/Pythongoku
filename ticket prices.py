# Write a python program to calculate te ticket price for a movie theatre based on the age of the customer
# 0-5 free
# 6-12 500
# 13-17 1000
# 18+ 1500

age = int(input("Enter age:"))
if age >= 18:
    print("price 1500")
if age >= 0 and age <= 5:
    print("price free")
if age >= 6 and age <= 12:
    print("price 500")
if age >= 13 and age <= 17:
    print("price 1000")
