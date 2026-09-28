time_travelr_toolkit.py


import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module 

dt.datetime.now().time()

print(dt.datetime.now().time())

base_cost = Decimal("1000.00")

current_year = dt.datetime.now().year
target_year = randint(1, 3000)
year_difference = abs(current_year - target_year)

cost_multiplator = Decimal(year_difference) * Decimal("1000.00")
final_cost = base_cost + cost_multiplator 
print(final_cost)

value = 1234.5
f"{value:.2f}"
print(f"Traveling to {target_year} will cost ${final_cost:.2f}")

possible_destination = ["Ancient Rome", "Medieval England", "The Renaissance", "2050 New York", "Dinosaur Age"]

selected_destination = choice(possible_destination)
print(selected_destination)

message = custom_module.generate_time_travel_message(target_year,selected_destination, final_cost)

print(message)
