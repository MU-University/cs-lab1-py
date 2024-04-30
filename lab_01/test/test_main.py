from lab_01.main.main import add


def test_main():
    assert 9 == add(4, 5)
    
def test_fail():
    assert 9 == add(2, 4)

def test_add_with_odd_numbers():
    assert 10 == add(7, 3)

def test_add_with_even_numbers():
    assert 20 == add(12, 8)
