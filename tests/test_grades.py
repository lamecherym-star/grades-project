from grades import clean_grades, average, mention

def test_clean_grades():
    values = [10, 15, -2, 22, "abc", 18]
    assert clean_grades(values) == [10, 15, 18]

def test_average():
    assert average([10, 20]) == 15

def test_average_empty():
    assert average([]) is None

def test_mention():
    assert mention(None) == "Aucune note"
    assert mention(8) == "Insuffisant"
    assert mention(12) == "Moyen"
    assert mention(16) == "Bien"