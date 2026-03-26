# 1.
"""
def calculate_bil(price):
    vat=10.5
    price=price+vat
    print(f"price is {price}")
calculate_bil(100)
"""
#2.
"""
def greet_users(name):
    prefix="Mr."
    full_name=prefix + name
    print(f"your full name is {full_name}")
greet_users("Sudipto Mandal")
"""
#3.
""" 
def dhaka_coffe(price):
    vat=20/100
    new_price= vat + price
    print(f"Dhaka coffe price is {new_price}")

def gopalganj_coffe(price):
    vat=10/100
    new_price=vat + price 
    print(f"the Gopalganj coffe price is {new_price}")

dhaka_coffe(100)
gopalganj_coffe(80)

"""
# 4.
def even_odd(number):
    status=""
    if number%2==0:
        status="even"
        print(status)
    else:
        status="odd"
        print(status)
even_odd(9)
