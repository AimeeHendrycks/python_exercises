#!/usr/bin/env python
'''
There are 1609.34 meters in a mile
A barleycorn is a (very old) English measure of length. 1 meter is equal to 117.647 barleycorns
1 mile is 1760 yards
A furlong is measure of distance, 220 yards
A fortnight is a measure of time, 2 weeks
1 mile is 5280 feet
The mach number is a measure of speed, the percentage of the speed of sound. 
    Mach 1 is a speed equal to the speed of sound in air, which is 1130 feet/second. 
    Mach 1.5 would be 1.5 times the speed of sound.
PSL is a speed, the percentage of the speed of light in a vacuum. 
    The speed of light is 299,792,458 meters/second. 
'''

mph = 0
def get_mph():
    try:
        global mph
        mph = float(raw_input('Enter your miles per hour: '))
    except:
        print 'Incorrect entry'
        get_mph()

def convert_bpd(mph):
    #convert to barleycorns/day
    meter_per_hour = mph * 1609.34
    barleycorns_per_hour = meter_per_hour * 117.647
    barleycorns_per_day = barleycorns_per_hour * 24
    return barleycorns_per_day

def convert_fpf(mph):
    #convert to furlongs/fortnight
    yards_per_hour = mph * 1760
    furlong_per_hour = yards_per_hour / 220
    furlong_per_day = furlong_per_hour * 24
    furlong_per_fortnight = furlong_per_day * 14
    return furlong_per_fortnight

def convert_mach(mph):
    feet_per_hour = mph * 5280
    feet_per_sec = feet_per_hour / 3600
    mach = feet_per_sec/1130
    return mach

def convert_psl(mph):
    meter_per_hour = mph * 1609.34
    meter_per_sec = meter_per_hour / 3600
    psl = meter_per_sec / 299792458
    return psl

get_mph()
print 'Your miles per hour is ' + str(mph) + ' mph.'
print 'This mph converts to ' + str(convert_bpd(mph)) + ' barleycorns/day.'
print 'This mph converts to ' + str(convert_fpf(mph)) + ' furlongs/fortnight.'
print 'The Mach number of this mph is ' + str(convert_mach(mph)) + '.'
print 'The PSL of this mph is ' + str(convert_psl(mph)) + '.'
print '---------'
