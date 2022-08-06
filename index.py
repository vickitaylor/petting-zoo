from animals import (Copperhead, Cottonmouth, Hellbender,
                     Hognose, Timberrattlesnake)
from animals import (Duck, Koi, Polarbear, Seal, Turtle)
from animals import (Alpaca, Goat, Llama, Pig, Pony)
from attractions import PettingZoo, SnakePit, Wetlands, wetlands

bob = Duck("Bob", "Duck", "watercress sandwiches", 456789)
bob.run()
bob.swim()
print(bob)
bob.quack()

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama",
                  "Midday", "Llama chow", 123456)
print(miss_fuzz.name, miss_fuzz.species, miss_fuzz.date_added)

bacon = Pig("Bacon", "Pig", "Morning", "not Bacon", 456789)
print(f"{bacon.name} the {bacon.species} is available to pet during the {bacon.shift} shift.")

feta = Goat("Feta", "Goat", "Afternoon", "Corn", 987654)
print(feta)

briar = Alpaca("Briar", "Alpaca", "Midday", "Grains", 789654)
briar.feed()
print(briar.name)

kabob = Pony("Kabob", "Pony", "Morning", "Hay", 321654)

fluffy = Hellbender("Fluffy", "Hellbender", "Tadpoles", 632485)

medusa = Hognose("Medusa", "Hognose Snake", "Field Mice", 754369)

buttercup = Cottonmouth("Buttercup", "Cottonmouth Snake", "Fish", 127953)

spicy_noodle = Timberrattlesnake(
    "Spicy Noodle", "Timber Rattlesnake", "Rabbit", 456753)

slinky = Copperhead("Slinky", "Copperhead Snake", "Rats", 987654)
print(f"{slinky.name} has a chip number of {slinky.chip_number}.")
slinky.chip_number = 123456
print(f"{slinky.name} has a chip number of {slinky.chip_number}.")

fuzzy_wuzzy = Polarbear("Fuzzy Wuzzy", "Polar Bear", "Big Fish", 753952)

quacks = Duck("Quacks", "Duck", "Small Fish", 159357)

goldie = Koi("Goldie", "Koi Fish", "Bugs", 853421)

flippy = Turtle("Flippy", "Red Belly Slider", "Grass", 657985)

pups = Seal("Pups", "Seal", "Small Fish", 741852)

varmint_village = PettingZoo(
    "Varmint Village", "Cute and fuzzy critters to cuddle")
slither_inn = SnakePit(
    "Slither Inn", "Slithery critters that are dangerous if cuddled")
wild_wetlands = Wetlands(
    "Wild Wetlands", "Critters that like to swim in the water")


varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(bacon)
varmint_village.add_animal(feta)
varmint_village.add_animal(briar)
varmint_village.add_animal(kabob)
slither_inn.add_animal(fluffy)
slither_inn.add_animal(medusa)
slither_inn.add_animal(buttercup)
slither_inn.add_animal(spicy_noodle)
slither_inn.add_animal(slinky)
wild_wetlands.add_animal(fuzzy_wuzzy)
wild_wetlands.add_animal(quacks)
wild_wetlands.add_animal(goldie)
wild_wetlands.add_animal(flippy)
wild_wetlands.add_animal(pups)

# print (varmint_village.attraction_name, varmint_village.description, varmint_village.animals)

# for animal in varmint_village.animals:
# print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')

# for animal in slither_inn.animals:
#     print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}.')

# for animal in wild_wetlands.animals:
# print(f'You can find {animal.name} the {animal.species} in {wild_wetlands.attraction_name}.')

print(f"{varmint_village.attraction_name} is where you will find {varmint_village.description} Like:")
for animal in varmint_village.animals:
    print(f"    * {animal.name} the {animal.species}")

print(f"{slither_inn.attraction_name} is where you will find {slither_inn.description} Like:")
for animal in slither_inn.animals:
    print(f"    * {animal.name} the {animal.species}")

print(f"{wild_wetlands.attraction_name} is where you will find {wild_wetlands.description} Like:")
for animal in wild_wetlands.animals:
    print(f"    * {animal.name} the {animal.species}")

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(wild_wetlands.last_critter_added)

fuzzy_wuzzy.feed()
miss_fuzz.feed()
kabob.ney()

dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Koi("Snappy", "Koi", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
slither_inn.add_animal_pythonic(dolly)
wild_wetlands.add_animal_pythonic(dolly)

varmint_village.add_animal_pythonic(snappy)
slither_inn.add_animal_pythonic(snappy)
wild_wetlands.add_animal_pythonic(snappy)

slither_inn.add_animal_pythonic(medusa)
wild_wetlands.add_animal_pythonic(medusa)
varmint_village.add_animal_pythonic(medusa)

slither_inn.add_animal_pythonic(quacks)
wild_wetlands.add_animal_pythonic(quacks)
varmint_village.add_animal_pythonic(quacks)