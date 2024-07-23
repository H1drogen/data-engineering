

def format_stalls(stalls, parks):
    lookup = {park["park_name"]: park["park_id"] for park in parks}

    formatted_stalls = [dict(stall, park_id=lookup[stall["park_name"]]) for stall in stalls]

    for stall in formatted_stalls:
        del stall["park_name"]
        del stall["foods_served"]

    return formatted_stalls

def format_stalls_foods(og_stalls, stalls, foods):
    lookup_stall = {stall[1]: stall[0] for stall in stalls}
    lookup_food = {food[1]: food[0] for food in foods}

    all_rows = []
    for stall in og_stalls:
        food_served = stall["foods_served"]

        id_tuples = [(lookup_stall[stall["stall_name"]], lookup_food[food]) for food in food_served]
        all_rows += id_tuples

    return all_rows