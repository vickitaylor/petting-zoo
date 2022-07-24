from models import (Copperhead, Cottonmouth, Hellbender, Hognose, Timberrattlesnake)
from models import (Duck, Koi, Polarbear, Seal, Turtle)
from models import (Alpaca, Goat, Llama, Pig, Pony)

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Midday", "Llama chow")
print(miss_fuzz.name, miss_fuzz.species, miss_fuzz.date_added)

bacon = Pig("Bacon", "Pig", "Morning", "not Bacon")
print(f"{bacon.name} the {bacon.species} is available to pet during the {bacon.shift} shift.")

feta = Goat("Feta", "Goat", "Afternoon", "Corn")
print(feta)

briar = Alpaca("Briar", "Alpaca", "Midday", "Grains")
print(briar.feed())

kabob = Pony("Kabob", "Pony", "Morning", "Hay")

fluffy = Hellbender("Fluffy", "Hellbender", "Tadpoles")

medusa = Hognose("Medusa", "Hognose Snake", "Field Mice")

buttercup = Cottonmouth("Buttercup", "Cottonmouth Snake", "Fish")

spicy_noodle = Timberrattlesnake("Spicy Noodle", "Timber Rattlesnake", "Rabbit")

slinky = Copperhead("Slinky", "Copperhead Snake", "Rats")

fuzzy_wuzzy = Polarbear("Fuzzy Wuzzy", "Polar Bear", "Big Fish")

quacks = Duck("Quacks", "Duck", "Small Fish")

goldie = Koi("Goldie", "Koi Fish", "Bugs")

flippy = Turtle("Flippy", "Red Belly Slider", "Grass")

pups = Seal("Pups", "Seal", "Small Fish")
