#Start
import random
import math
import PyQt5



#variables
gender_choice = ["male", "female"]
tile_choice = ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AO", "AP"]
gene_choice = ["speed", "strength", "health", "looks"]
hair_colour_choice = ["brown", "blonde", "black", "ginger", "white"]
eye_colour_choice = ["brown", "blue", "green", "grey"]
settlement_tiles = []

#small variables
a = 1
character_count = 0

#Data
character_data = {

}

character_chromosome = {

}

#Functions
def create_character():
    gender = random.choice(gender_choice)
    tile = random.choice(tile_choice)
    update_dict(gender, tile)


def initialization():
    create_character()
    starting_gene = random.choice(gene_choice)
    hair_colour = random.choice(hair_colour_choice)
    eye_colour = random.choice(eye_colour_choice)
    global speed
    speed = False
    global strength
    strength = False
    global health
    health = False
    global looks
    looks = False
    if starting_gene == "speed":
        speed = True

    elif starting_gene == "strength":
        strength = True

    elif starting_gene == "health":
        health = True

    elif starting_gene == "looks":
        looks = True

    chromosome_creation(hair_colour, eye_colour, speed, strength, health, looks)


def update_dict(gender,tile):
    global character_count
    character_count = character_count + 1
    character_data.update({character_count: "dict"})
    character_data[character_count] = {"gender": gender, "age": "0", "children": [], "tile": tile, "livechance": "75", "reprochance": "50"}



def settlement_start():
    start_tile = random.choice(tile_choice)
    settlement_tiles.append(start_tile)


def chromosome_creation(hair,eye,speed, strength, health, looks):
    character_chromosome.update({character_count: "dict"})
    character_chromosome[character_count] = {"speed": speed, "strength": strength, "health": health, "looks": looks, "hair": hair, "eyes": eye}

def check_gene(character, gene):
    if character_chromosome[character][gene] == True:
        return True

    else:
        return False

def age_update(character):
    x = character_data[character]["age"]
    x = int(x)
    x = (x + 1)
    character_data[character]["age"] = x
    y = character_data[character]["livechance"]
    y = int(y)
    y = (y - 5)
    character_data[character]["livechance"] = y

def live():
    z = random.randint(0,100)
    if z < 76:
        return True

    else:
        return False

county = 0
#Code
initialization()
initialization()
print(character_data)

for i in range(character_count):
    age_update(a)
    a = (a + 1)


print(character_data)

