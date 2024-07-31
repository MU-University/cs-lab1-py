from main.main import my_sum


def test_add_with_four_numbers():
    assert 24 == my_sum(4, 5, 7, 8)

def test_add_with_three_numbers():
    assert 12 == my_sum(7, 3, 2)

def test_add_with_two_numbers():
    assert 20 == my_sum(12, 8)
