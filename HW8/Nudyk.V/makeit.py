# You were camping with your friends far away from home, but when it's time to go back, 
# you realize that your fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.



def zero_fuel(distance_to_pump, mpg, fuel_left):
    ''' Return true if it possible to get to the nearest 
        gas station before the car runs out of fuel'''

    return (True if (mpg * fuel_left >= distance_to_pump) else False)


print(zero_fuel(49, 25, 2))

def zero_fuel1(distance_to_pump, mpg, fuel_left):
    ''' Return true if it possible to get to the nearest 
        gas station before the car runs out of fuel'''

    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False

print(zero_fuel1(50, 25, 2))

def zero_fuel2(distance_to_pump, mpg, fuel_left):
    ''' Return true if it possible to get to the nearest    
        gas station before the car runs out of fuel'''

    return mpg * fuel_left >= distance_to_pump


print(zero_fuel2(51, 25, 2))
