from app import add,multiply,add_str

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert multiply(2, 3) == 6

def test_add_str():
    assert add_str("Hello, ","World!") == "Hello, World!"