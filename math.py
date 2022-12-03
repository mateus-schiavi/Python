"""
File: weather_temperature
Author: Mateus Schiavi

Purpose: Use functions to calculate temperatue.
"""

import math


def result(V,T,degree):
    if degree.upper() == 'C':
        T = (T * (9/5)) + 32
    elif degree.upper() == 'K':
        T = T - 273.15
    elif degree.upper() == 'R':
        T = (T * (9/4)) + 32
    elif degree.upper == 'Ra':
        T = T - 459.67
    elif degree.upper == 'N':
        T = (T *(5.4545)) + 32
    answer = 35.74 + (0.6215 * T) - (35.75*(V**.16)) + (0.4275*T*(V**.16))
    return answer



def main():
    wind_list = [5,10,15,20,25,30,35,40,45,50,55,60]
    temp = float(input(f"\nWhat is the temperature? "))
    degree = input(f"Fahrenheit, Celsius, Kelvin, Réaumur, Rankine or Newton (F/C/K/R/Ra/N)? ")
    for wind in wind_list:
        chill = result(wind, temp, degree)
        print(f"At temperature {temp:.0f}{degree}, and  speed {wind} mph, the windchill is: {chill:.2f}F")

main()

'''In the IS (International System) the scales used for temperature are Fahrenheit (°F), Celsius (°C) and Kelvin (K)
But, there are other temperature scales, like Newton (N), Rankine(Ra) and Réaumur(R)'''