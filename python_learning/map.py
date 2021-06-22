# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-pt


# syntax map
# map(function, iterable, [iterable 2, iterable 3, ...])


# with lambda
# map(lambda item: item[] expression, iterable)

numbers = [10, 15, 21, 33, 42, 55]
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
# print(mapped_numbers)  # [23, 33, 45, 69, 87, 113]


# --------------
aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]


def assign_to_tank(aquarium_creatures, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x
    return map(apply, aquarium_creatures)


assigned_tanks = assign_to_tank(aquarium_creatures, 42)
# print(list(assigned_tanks))  # all tank numbers are 42

# -----------------------
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))
# print(numbers_powers)  # [2, 16, 216, 4096, 100000]


# ------ one iterable that was longer than the other
base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))
# print(numbers_powers)  # [2, 16, 216, 4096, 100000]
# map() stopped calculating as soon as it reached the end of the shortest

# extras
# space-separated entry list
# A = list(map(int, input().split()))
