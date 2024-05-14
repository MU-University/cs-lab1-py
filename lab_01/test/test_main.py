from lab_01.main.main import add


def test_add_with_four_numbers():
    assert 24 == add(4, 5, 7, 8)

def test_add_with_three_numbers():
    assert 12 == add(7, 3, 2)

def test_add_with_two_numbers():
    assert 20 == add(12, 8)
