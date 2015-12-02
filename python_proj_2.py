#!/usr/bin/env python
'''
1 gallon is equivalent to 3.7854 liters
1 barrel of oil produces 19.5 gallons of gas (approximately, can vary depending on the oil source. This number will work for us). FYI, a barrel is 42 gallons.
1 gallon of gas produces approximately 20 pounds of CO2. Again, good enough
1 gallon of gas produces 115,000 BTU (British Thermal Units). 1 gallon of ethanol produces 75,700 BTU.
Cost is $4.00/gallon
'''
gallons = 0
def get_gallons():
    try:
        global gallons
        gallons = float(raw_input('Enter the number of gallons of gasoline: '))
    except:
        print 'Incorrect entry'
        get_gallons()

def convert_liters(gallons):
    #converts to liters
    return gallons * 3.7854

def convert_barrels_oil(gallons):
    #converts to barrels of oil (barrels of oil required)
    return gallons / 19.5

def convert_CO2(gallons):
    #converts to pounds of CO2 produced
    return gallons * 20

def convert_ethanol(gallons):
    #converts to ethanol gallons
    '''
    1 gallon of gas produces 115,000 BTU (British Thermal Units)
    1 gallon of ethanol produces 75,700 BTU
    '''
    return gallons * 115000 / 75700

def calculate_price(gallons):
    #price in US dollars
    return gallons * 4.00

get_gallons()
print 'You have entered in ' + str(gallons) + ' gallons of gasoline.'
print 'This converts to ' + str(convert_liters(gallons)) + ' liters of gasoline.'
print str(convert_barrels_oil(gallons)) + ' barrels of oil are required to produce this amount of gas.'
print str(convert_CO2(gallons)) + ' pounds of CO2 are produced by using this amount of gas.'
print 'This amount of gas is equivalent to ' + str(convert_ethanol(gallons)) + ' gallons of ethanol.'
print 'The price of this amount of gas is $' + str(("%.2f" % calculate_price(gallons))) + '.'
print '---------'