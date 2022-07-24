from models import (Copperhead, Cottonmouth, Hellbender, Hognose, Timberrattlesnake)
from models import (Duck, Koi, Polarbear, Seal, Turtle)
from models import (Alpaca, Goat, Llama, Pig, Pony)

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Midday")
print(miss_fuzz.name, miss_fuzz.species, miss_fuzz.date_added)

bacon = Pig("Bacon", "Pig", "Morning")
print(f"{bacon.name} the {bacon.species} is avaiable to pet during the {bacon.shift} shift.")

feta = Goat("Feta", "Goat", "Afternoon")

briar = Alpaca("Briar", "Alpaca", "Midday")

kabob = Pony("Kabob", "Pony", "Morning")

fluffy = Hellbender("Fluffy", "Hellbender")

medusa = Hognose("Medusa", "Hognose Snake")

buttercup = Cottonmouth("Buttercup", "Cottonmouth Snake")

spicy_noodle = Timberrattlesnake("Spicy Noodle", "Timber Rattlesnake")

slinky = Copperhead("Slinky", "Copperhead Snake")

fuzzy_wuzzy = Polarbear("Fuzzy Wuzzy", "Polar Bear")

quacks = Duck("Quacks", "Duck")

goldie = Koi("Goldie", "Koi Fish")

flippy = Turtle("Flippy", "Red Belly Slider")

pups = Seal("Pups", "Seal")
