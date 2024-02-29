from lab_01.main.main import add


def test_main():
    assert 9 == add(4, 5)
    assert 8 == add(4, 4)