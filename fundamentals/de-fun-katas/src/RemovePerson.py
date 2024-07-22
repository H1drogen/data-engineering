def remove_person(people, id_to_remove):
    new_people = []
    for person in people:
        if person['id'] != id_to_remove:
            new_people.append(person)
    return new_people