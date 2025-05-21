def query_gradebook(gradebook, student):
    return gradebook.get(student, "Student not found")
