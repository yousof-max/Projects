import random

animals = ("Elephant", "Giraffe", "Kangaroo", "Cheetah", "Penguin", "Rhinoceros", "Flamingo", "Crocodile", "Hippopotamus", "Octopus",
"Panther", "Chimpanzee", "Ostrich", "Porcupine", "Squirrel", "Walrus", "Seahorse", "Armadillo", "Peacock", "Raccoon")
vehicles = ("Motorcycle", "Helicopter", "Ambulance", "Bulldozer", "Firetruck", "HotAirBalloon", "Hovercraft", "Limousine", "Snowmobile", "Submarine",
"Spaceship", "Tractor", "Convertible", "Scooter", "JetSki", "CableCar", "Biplane", "Minivan", "PickupTruck", "Tanker")
fruits = ("Strawberry", "Blueberry", "Blackberry", "Pineapple", "Watermelon", "Papaya", "Cantaloupe", "Dragonfruit", "Pomegranate", "Kiwi",
"Raspberry", "Coconut", "Avocado", "Guava", "Lychee", "Passionfruit", "Durian", "Mulberry", "Fig", "Tamarind")
all_words = (
    # Animals
    "Elephant", "Giraffe", "Kangaroo", "Cheetah", "Penguin", "Rhinoceros", "Flamingo", "Crocodile",
    "Hippopotamus", "Octopus", "Panther", "Chimpanzee", "Ostrich", "Porcupine", "Squirrel",
    "Walrus", "Seahorse", "Armadillo", "Peacock", "Raccoon",

    # Vehicles
    "Motorcycle", "Helicopter", "Ambulance", "Bulldozer", "Firetruck", "HotAirBalloon", "Hovercraft",
    "Limousine", "Snowmobile", "Submarine", "Spaceship", "Tractor", "Convertible", "Scooter",
    "JetSki", "CableCar", "Biplane", "Minivan", "PickupTruck", "Tanker",

    # Fruits
    "Strawberry", "Blueberry", "Blackberry", "Pineapple", "Watermelon", "Papaya", "Cantaloupe",
    "Dragonfruit", "Pomegranate", "Kiwi", "Raspberry", "Coconut", "Avocado", "Guava", "Lychee",
    "Passionfruit", "Durian", "Mulberry", "Fig", "Tamarind"
)

random_words = (animals, vehicles, fruits)

random = random.choice(random_words)

hangman_art = {0: (" | ",
                   "   ",
                   "   ",
                   "   "),
               1: (" | ",
                   " o ",
                   "   ",
                   "   "),
               2: (" | ",
                   " o ",
                   " | ",
                   "   "),
               3: (" | ",
                   " o ",
                   "/| ",
                   "   "),
               4: (" | ",
                   " o ",
                   "/|\\",
                   "   "),
               5: (" | ",
                   " o ",
                   "/|\\",
                   "/  "),
               6: (" | ",
                   " o ",
                   "/|\\",
                   "/ \\"),
               7: (" o ",
                   "/|\\",
                   "/ \\")}