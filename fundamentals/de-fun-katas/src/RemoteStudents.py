def update_remote_students(students):
    updated_students = []
    for student in students:
        if 'location' not in student:
            student['location'] = 'remote'
            updated_students.append(student)
        else:
            updated_students.append(student)
    return updated_students