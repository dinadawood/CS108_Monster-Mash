#################################################
# Do not modify this section
# You must place 'monster_mash.json' in the same
# directory as this file.
from cisc108 import assert_equal
import json

with open('monster_mash.json') as data_file:
    MONSTER_MASH = json.load(data_file)

#################################################
# Your code goes below

## Party
'''
A Party is a dictionary with four fields:
* "type": The type of party that it is
* "werewolves": The number of werewolves in attendance
* "vampires": The number of vampires in attendance
* "witches": The number of witches in attendance
'''

Party = {"werewolves": int, "vampires": int, "witches": int,
         "type": str}


"""
P1. Define a function `sum_guests` that consumes a Party and
produces an integer representing the total number of
guests attending (including werewolves, vampires, and witches).
"""
def sum_guests(a_party: Party) -> int:
    return a_party["werewolves"]+ a_party["vampires"]+ a_party["witches"]

assert_equal(sum_guests(MONSTER_MASH["party 1"]), 20)
assert_equal(sum_guests(MONSTER_MASH["party 2"]), 25)
assert_equal(sum_guests(MONSTER_MASH["party 3"]), 19)
assert_equal(sum_guests(MONSTER_MASH["party 4"]), 33)
assert_equal(sum_guests(MONSTER_MASH["party 5"]), 50)

"""
P2. Define a function `were_only_werewolves` that consumes a Party and
produces a boolean indicating whether or not the only guests were
werewolves.
"""

def were_only_werewolves(a_party: Party) -> bool:
    if  a_party["vampires"] ==0 and a_party["witches"] ==0:
        return True
    else: 
        return False

assert_equal(were_only_werewolves(MONSTER_MASH["party 1"]), True) 
assert_equal(were_only_werewolves(MONSTER_MASH["party 2"]), False) 
assert_equal(were_only_werewolves(MONSTER_MASH["party 3"]), False) 
assert_equal(were_only_werewolves(MONSTER_MASH["party 4"]), True) 
assert_equal(were_only_werewolves(MONSTER_MASH["party 5"]), False) 

'''
P3. Witches and vampires always bring a date, but werewolves prefer to
come to parties alone (because they're lone wolves). Define a function
`total_folks` that consumes a Party and produces an integer representing
the total number of folks who were present.
'''

def total_folks (a_party: Party) -> int:
    vampires = (2 * a_party["vampires"])
    witches = (2 * a_party["witches"])
    new_party = vampires + witches + a_party["werewolves"]
    return new_party

assert_equal(total_folks(MONSTER_MASH["party 1"]), 20)
assert_equal(total_folks(MONSTER_MASH["party 2"]), 45)
assert_equal(total_folks(MONSTER_MASH["party 3"]), 38)
assert_equal(total_folks(MONSTER_MASH["party 4"]), 33)
assert_equal(total_folks(MONSTER_MASH["party 5"]), 85)

'''
P4. A "small" party has 20 or fewer guests, a "big" party has 40 or more,
and otherwise the party is "medium". Define a function `check_party_size`
that consumes a Party and produces a string indicating whether the party
is "small", "medium", or "big". Note that we're counting guests, not folks,
so don't include witches' and vampires' dates.
'''

def check_party_size(a_party: Party) -> str:
    total = sum_guests(a_party)
    if (total <= 20):
        return "small"
    elif (total >= 40):
        return "big"
    else: 
        return "medium"
    
assert_equal(check_party_size(MONSTER_MASH["party 1"]), "small")
assert_equal(check_party_size(MONSTER_MASH["party 2"]), "medium")
assert_equal(check_party_size(MONSTER_MASH["party 3"]), "small")
assert_equal(check_party_size(MONSTER_MASH["party 4"]), "medium")
assert_equal(check_party_size(MONSTER_MASH["party 5"]), "big")


'''
P5. If a party has both werewolves and vampires, there should be
more werewolves than vampires. Define a function `check_party_ratio`
that consumes a Party and produces a float indicating the number of
werewolves divided by the number of vampires. If there are no vampires
or no vampires, produce the value 0.
'''

def check_party_ratio(a_party: Party) -> float:
    if a_party["vampires"] ==0 or a_party["werewolves"] == 0:
        return 0.0
    else: 
        return (a_party["werewolves"]) / (a_party["vampires"])
    
assert_equal(check_party_ratio(MONSTER_MASH["party 1"]), 0.0)
assert_equal(check_party_ratio(MONSTER_MASH["party 2"]), 0.25)
assert_equal(check_party_ratio(MONSTER_MASH["party 3"]), 0.0)
assert_equal(check_party_ratio(MONSTER_MASH["party 4"]), 0.0)
assert_equal(check_party_ratio(MONSTER_MASH["party 5"]), 3.0)


## Monsters
'''
A Monster is a dictionary with four fields:
* "name": The name of this particular monster (string)
* "kind": A str representing the type of the monster (e.g., "vampire", "werewolf")
* "spookyiness": An integer from 0-4 indicating its spookiness
* "undead?": A boolean indicating whether or not this monster is undead.
'''

Monster = {"name": str, "kind": str, "spookiness": int, "undead?": bool}

'''
M1. Define a function `count_monsters` that consumes a list of monsters and
produces an integer indicating how many monsters there are.
'''

def count_monsters(monsters: [Monster]) -> int:
    if not monsters:
        return 0
    count = 0
    for monster in monsters:
        count = count + 1
    return count
    
assert_equal(count_monsters(MONSTER_MASH["monsters 1"]), 4)
assert_equal(count_monsters(MONSTER_MASH["monsters 2"]), 4)
assert_equal(count_monsters(MONSTER_MASH["monsters 3"]), 5)
assert_equal(count_monsters(MONSTER_MASH["monsters 4"]), 5)
assert_equal(count_monsters(MONSTER_MASH["monsters 5"]), 5)
assert_equal(count_monsters(MONSTER_MASH["monsters 6"]), 0)


'''
M2. Define a function `count_undead_monsters` that consumes a list
of monsters and produces an integer indicating how many undead
monsters there are.
'''

def count_undead_monsters(monsters: [Monster]) -> int:
    count = 0
    for monster in monsters:
        count = count + monster["undead?"]
        if "undead?" == True:
            return count
    return count

assert_equal(count_undead_monsters(MONSTER_MASH["monsters 1"]), 0)
assert_equal(count_undead_monsters(MONSTER_MASH["monsters 2"]), 4)
assert_equal(count_undead_monsters(MONSTER_MASH["monsters 3"]), 2)
assert_equal(count_undead_monsters(MONSTER_MASH["monsters 4"]), 4)
assert_equal(count_undead_monsters(MONSTER_MASH["monsters 5"]), 3)
assert_equal(count_undead_monsters(MONSTER_MASH["monsters 6"]), 0)


'''
M3. Define a function `average_spookiness` that consumes a list of monsters
and produces a float representing their average spookiness. If the list
is empty, produce the special value `None` instead.
'''

def average_spookiness(monsters: [Monster]) -> float:
    if not monsters:
        return None
    count = 0 
    average = 0 
    sum = 0 
    for monster in monsters:
        count = count + 1
        sum = sum + monster["spookiness"]
        average = sum / count
    return average
        
assert_equal(average_spookiness(MONSTER_MASH["monsters 1"]), 0.0)
assert_equal(average_spookiness(MONSTER_MASH["monsters 2"]), 1.0)
assert_equal(average_spookiness(MONSTER_MASH["monsters 3"]), 1.8)
assert_equal(average_spookiness(MONSTER_MASH["monsters 4"]), 1.6)
assert_equal(average_spookiness(MONSTER_MASH["monsters 5"]), 0.4)
assert_equal(average_spookiness(MONSTER_MASH["monsters 6"]), None)

'''
M4. Define a function `average_undead_spookiness` that consumes a list of monsters
and produces a float representing the average spookiness of the undead monsters
in the list. If there are no undead monsters, produce the special value `None`
instead.
'''

def average_undead_spookiness(monsters: [Monster]) -> float:
    count = 0 
    average = 0 
    sum = 0
    for monster in monsters:
        if monster["undead?"] == True: 
            count = count + 1
            sum = sum + monster["spookiness"]
    if count == 0:
        return None
    average = sum / count 
    return average
    
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 1"]), None)            
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 2"]), 1)            
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 3"]), 0.6)            
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 4"]), 1.6)            
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 5"]), 0.4)            
assert_equal(average_undead_spookiness(MONSTER_MASH["monsters 6"]), None)            

'''
M5. Define a function `count_spooky_monsters` that consumes a list of monsters
and produces an integer indicating how many monsters have a spookiness of
2 or more.
'''

def count_spooky_monsters(monsters: [Monster]) -> int:
    count = 0
    for monster in monsters:
        if monster["spookiness"] >= 2:
            count = count + 1
    return count

assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 1"]), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 2"]), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 3"]), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 4"]), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 5"]), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH["monsters 6"]), 0)


'''
M6. Define the function `count_vampires` that consumes a list of monsters
and produces an integer indicating how many monsters are of the kind
"vampire".
'''

def count_vampires(monsters: [Monster]) -> int:
    count = 0
    for monster in monsters:
        if monster["kind"] == "vampire":
            count = count + 1
    return count

assert_equal(count_vampires(MONSTER_MASH["monsters 1"]), 0)
assert_equal(count_vampires(MONSTER_MASH["monsters 2"]), 4)
assert_equal(count_vampires(MONSTER_MASH["monsters 3"]), 0)
assert_equal(count_vampires(MONSTER_MASH["monsters 4"]), 0)
assert_equal(count_vampires(MONSTER_MASH["monsters 5"]), 2)
assert_equal(count_vampires(MONSTER_MASH["monsters 6"]), 0)

## Costumes
'''
A Costume is a dictionary with 3 keys:
* 'label': A string representing the name of the costume.
* 'price': An integer representing the cost of the costume in dollars.
* 'sizes': A list of strings representing the available sizes ('S', 'M', 'L').
'''

Costume = {'label': str, 'price': int, 'sizes': [str]}


'''
C1. Define a function `count_costumes` that consumes a list of costumes
and produces an integer representing the number of costumes in the list.
'''

def count_costumes(costumes: [Costume]) -> int:
    if not costumes:
        return 0
    count = 0 
    for costume in costumes:
        count = count + 1
    return count
       
assert_equal(count_costumes(MONSTER_MASH["costumes 1"]), 4)
assert_equal(count_costumes(MONSTER_MASH["costumes 2"]), 3)
assert_equal(count_costumes(MONSTER_MASH["costumes 3"]), 4)
assert_equal(count_costumes(MONSTER_MASH["costumes 4"]), 5)
assert_equal(count_costumes(MONSTER_MASH["costumes 5"]), 4)
assert_equal(count_costumes(MONSTER_MASH["costumes 6"]), 0)

'''
C2. Define a function `total_price` that consumes a list of costumes
and produces an integer representing the total price of all the
costumes in the list.
'''

def total_price(costumes: [Costume]) -> int:
    sum = 0 
    for costume in costumes:
        sum = sum + costume["price"]
    return sum

assert_equal(total_price(MONSTER_MASH["costumes 1"]), 180)
assert_equal(total_price(MONSTER_MASH["costumes 2"]), 105)
assert_equal(total_price(MONSTER_MASH["costumes 3"]), 21)
assert_equal(total_price(MONSTER_MASH["costumes 4"]), 340)
assert_equal(total_price(MONSTER_MASH["costumes 5"]), 130)
assert_equal(total_price(MONSTER_MASH["costumes 6"]), 0)

'''
C3. Define a function `count_sizes` that consumes a list of costumes and
produces an integer indicating the total number of sizes that are
available across all the costumes.
'''

def count_sizes(costumes: [Costume]) -> int:
    pass

assert_equal(count_sizes(MONSTER_MASH["costumes 1"]), )
assert_equal(count_sizes(MONSTER_MASH["costumes 2"]), )
assert_equal(count_sizes(MONSTER_MASH["costumes 3"]), )
assert_equal(count_sizes(MONSTER_MASH["costumes 4"]), )
assert_equal(count_sizes(MONSTER_MASH["costumes 5"]), )
assert_equal(count_sizes(MONSTER_MASH["costumes 6"]), )

'''
C4. Define a function `max_price` that consumes a list of costumes
and produces an integer indicating the price of the most expensive
costume. If there are no costumes in the list, produce the special
value `None`.
'''


'''
C5. Define a function `most_expensive_costume` that consumes
a list of costumes and produces a string representing the label
of the costume with the highest price. In the event of a tie,
give the label of the item later in the list. If there are no
costumes, return the special value None.
'''


'''
C6. Define a function `find_last_medium` that consumes a list of costumes
and produces the label of the last costume that is available in a medium.
If no medium costumes are found, produce the special value `None`.
'''


'''
C7. Define a function `find_first_small` that consumes a list of costumes
and produces the label of the first costume that is available in a small.
If no small costumes are found, produce the special value `None`.
'''


## Tombstones

'''
A Grave is a dictionary with two keys:
* 'Name': A string value with the grave's occupant's name
* 'Message': A string value with the grave's message
'''

Grave = {'name': str, 'Message': str}


'''
G1. Define the function `count_grave_all` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Include spaces and new lines.
'''


'''
G2. Define the function `count_grave_characters` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Do not count spaces and new lines.
'''


'''
G3. Define a function named `estimate_grave_cost` that consumes a list of graves
and produces an integer representing the total estimate lettering cost by
multiplying the number of letters on the grave (ignoring spaces and newlines) by
the cost of writing a letter ($2).
'''


"""
G4. Define a function named `count_shouters` that consumes a list of graves
and produces an integer representing the number of graves that had their
messages in all capital letters. Hint: use the `.upper()` method.
"""


## Treats

'''
A Treat is a dictionary with the following keys
* "name": A string value indicating the name of the treat
* "chocolate?": A boolean indicating whether the treat involves chocolate
* "calories": An integer representing how many calories are in the treat
* "quantity": An integer indicating the typical serving size of the treat.
'''

Treat = {'name': str, 'chocolate?': bool, 'calories': int, 'quantity': int}



'''
T1. You are going through a series of houses and you get a treat from
each one. Define a function `eat_treats` that consumes a list of treats and
produces the total number of calories in all the treats.
'''


'''
T2. Define a function `find_most_calorific_ratio` that consumes a list
of treats and produces a float representing the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''


'''
T3. Define a function `find_most_calorific` that consumes a list
of treats and produces a string representing the name of the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''


'''
T4. Define a function named `count_chocolates` that consumes a list of treats
and produces the number of treats that are made of chocolate.
'''


'''
T5. Define a function named `get_choco_quantity` that consumes a list
of treats and produces an integer representing the total quantities
of all the chocolate treats.
'''


## Media

'''
A Media is a dictionary with the following keys:
* "name": The name of this media
* "kind": Either "movie", "song", or "game"
* "duration": The length of this media in minutes
'''

Media = {'name': str, 'kind': str, 'duration': int}


'''
E1. Define a function `total_duration` that consumes a list of Media
and produces their total duration.
'''


'''
E2. Define the function `count_not_long` that consumes a list of media
and produces the number of items that are less than 100 minutes long.
'''

'''
E3. Define the function `take_until_long` that consumes a list of media
and counts elements until it encounters something that is 100 minutes
longer or more, and then stops and returns the number counted so far.
'''

'''
E4. Define the function `longest_kind` that consumes a list of Media
and produces a string value representing the kind that had the highest
duration. If the list is empty, return the value None.
'''



'''
E5. Define the function `same_kind_of_media` that consumes a list
of Media and produces a boolean indicating whether all of the
kinds of media are the same as each other. If the list is empty,
the result is True.
'''



## Brewing Potions

'''
An Ingredient has the following keys:
* 'name': The name of the ingredient
* 'rare?': Whether the ingredient is rare

A Potion has the following keys:
* 'effect': The effect of the potion
* 'ingredients': The required ingredients of the potion
* 'time required': How many minutes it takes to brew the potion
'''

Ingredient = {'name': str, 'rare?': bool}
Potion = {'effect': str, 'ingredients': [Ingredient], 'time required': int}



'''
B1. Define the function `total_ingredients` that consumes a list
of potions and produces the total number of required ingredients.
Include duplicates in your total.
'''


'''
B2. Define the function `count_rare_ingredients` that consumes a list
of potions and produces the total number of required ingredients that
are rare.
'''



'''
B3. Define the function `get_ingredients` that consumes a list of
potions and produces a list of strings (representing ingredient names)
in the order that the ingredients are listed in the potions.
Do not include duplicate ingredients.
'''

'''
B4. Define the function `get_brewing_time` that consumes a list of
potions and produces an integer representing the total time required
to brew all the potions.
'''


'''
B5. Define the function `brew_time_per_ingredient` that consumes a list
of potions and produces a float representing the average amount of
time spent brewing overall. To do so, add up the time spent brewing
and divide it by the number of ingredients. If there are no ingredients,
return the value None.
'''



'''
B6. Define the function `get_rarest_potion` that consumes a list of potions
and returns the effect of the potion that requires the most rare ingredients.
If there are no rare ingredients in any of the potions, then return None instead.
'''

