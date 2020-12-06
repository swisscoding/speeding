#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored

# decoration
print(colored.stylize("\n---- | Calculate saved time because of speeding | ----\n", colored.fg("red")))

speed_limit = int(input("Speed limit (mph): "))
avg_speed = int(input("Average speed (mph): "))
distance = float(input("Distance travelled at average speed (miles): "))
print()

def time_saved(sL, aS, d):
    normal_speed = d/sL
    speeding = d/aS
    return round(60*abs(normal_speed-speeding), 3)

minutes = colored.stylize(time_saved(speed_limit, avg_speed, distance), colored.fg("green"))
print(f"Due to speeding, you have saved {minutes} minutes.\n")
