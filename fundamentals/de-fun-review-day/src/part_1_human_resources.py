from copy import deepcopy


def make_name_tags(guests):
    guests_copy = deepcopy(guests)
    for guest in guests_copy:
        title = guest.get('title')
        forename = guest.get('forename')
        surname = guest.get('surname')
        company = guest.get('company')
        guest['name_tag'] = f'{guest.get("title")} {forename} {surname}, {company}'
    return guests_copy



def create_poll(items):
    poll = {}
    for item in items:
        if item not in poll:
            poll[item] = 0
        poll[item] += 1
    return poll

