from src.RemoteStudents import update_remote_students


def test_update_student_works_with_one_entry():
    assert update_remote_students([{"name": 'Euler', "age": 27}]) == [{"name": 'Euler', "age": 27, "location": 'remote'}]

def test_update_student_works_with_two_entries():
    entry = [{"name": 'Euler', "age": 27}, {"name": 'Gauss', "age": 30}]
    output = [{"name": 'Euler', "age": 27, "location": 'remote'}, {"name": 'Gauss', "age": 30, "location": 'remote'}]
    assert update_remote_students(entry) == output

def test_update_student_does_not_update_existing_locations():
    output = update_remote_students([
    { "name": 'Hypatia', "age": 31, "location": 'leeds' },
    { "name": 'Ramanujan', "age": 22 },
    { "name": 'Tao', "age": 47, "location": 'manchester' }])
    assert output == [
    { "name": 'Hypatia', "age": 31, "location": 'leeds' },
    { "name": 'Ramanujan', "age": 22, "location": 'remote' },
    { "name": 'Tao', "age": 47, "location": 'manchester' }]
