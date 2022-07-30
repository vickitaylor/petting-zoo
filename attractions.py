from models import PettingZoo, SnakePit, Wetlands
from animals import (miss_fuzz, bacon, feta, briar, kabob, fluffy, medusa,
                     buttercup, spicy_noodle, slinky, fuzzy_wuzzy, quacks, goldie, flippy, pups)

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
