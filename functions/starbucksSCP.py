"""
Programmer: Jace Horn
Program: starbucksSCP
Program Version: 3.10.2
Created On: 10/21/2022
Last Modified: 10/21/2022
"""

def espresso(quantity, coffee, water):
    '''
    :param quanity: number of orders of espresso
    :param coffee: parameter keeping track of total coffee
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity*espresso servings
    '''
    coffee = coffee - (quantity*8)
    water = water - (quantity*1.5)

def americano(quantity, size, coffee, water):
    '''
    : Americano mix: 1 shot of espresso and 3 oz. of hot water
    :param quantity: number of orders of americano
    :param size: serving size (Tall / Grande / Venti / Trenta)
    :param coffee: keeping track of total coffee powder
    :param water: parameter of keeping track of total water
    :return: updated resources after serving quantity * size * americano servings
    '''

    coffee = coffee - (quantity*8)
    water = water - (quantity*1.5)

print("Program to keep track of Starbucks supply chain")
print("Enter the quantities of the raw materials at the beginning of the day")

coffee = float(input("Enter the Coffee Quantity: \t"))
milk = float(input("Enter the Milk Quantity: \t"))
water = float(input("Enter the Water Quantity: \t"))
icecream = float(input("Enter the icecream Quantity: \t"))
chocolate = float(input("Enter the Chocolate Quantity: \t"))
whiskey = float(input("Enter the Whiskey Quantity: \t"))

#Coffee Sizes
tall= 12
grande= 16
venti= 24
trenta= 31

espresso(2, coffee, water)
americano(2, venti, coffee, water)
cappuccino(2, venti, coffee, milk)
mocha(2, venti, coffee, chocolate, milk)
cortado(2, venti, coffee, milk)

print("Remnainig supplies")

