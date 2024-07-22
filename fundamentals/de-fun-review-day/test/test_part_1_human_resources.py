from src.part_1_human_resources import make_name_tags, create_poll

# implement your tests here

def test_guest_returns_nothing_with_empty_list():
    guests = []
    assert make_name_tags(guests) == []

def test_guest_returns_name_tag():
    guests = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        }
    ]
    expected = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
            'name_tag': 'Mr Sam Caine, Northcoders'
        }
    ]

    assert make_name_tags(guests) == expected

def test_multiple_guests_returns_name_tag():
    guests = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
        },
    ]
    expected = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
            'name_tag': 'Mr Sam Caine, Northcoders'
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
            'name_tag': 'Mr Kermit The Frog, Jim Henson Studios'
        }
    ]
    assert make_name_tags(guests) == expected

def test_make_name_tags_is_pure():
    guests = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        }
    ]
    make_name_tags(guests)
    assert guests == [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        }
    ]

def test_make_name_tags_returns_output_in_different_location():
    guests = [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        }
    ]
    assert id(make_name_tags(guests)) != id(guests)

def test_create_poll_returns_single_item():
    items = ['apple']
    assert create_poll(items) == {'apple': 1}

def test_create_poll_counts_multiple_items():
    items = ["cake", "biscuit", "biscuit"]
    assert create_poll(items) == {'cake': 1, 'biscuit': 2}

def test_create_poll_can_read_from_file():
    with open('../data/poll_data.py', 'r') as file:
        file.readline()
        source = file.readlines()
        for i in range(0, len(source) - 1):
            source[i] = source[i].strip()[1:-2]
        del source[-1]
        source[-1] += 'e'
        assert create_poll(source) == {
          'apple': 276,
          'pear': 223,
          'banana': 263,
          'orange': 238,
          'lonesome plum': 1
        }
