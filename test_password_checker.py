from password_checker import is_valid_password

def test_is_valid_password():
    assert is_valid_password("Abcdef1!") == True

def test_too_short():
    assert is_valid_password("Ab1!") == False

def test_no_number():
    assert is_valid_password("AbcdefG") == False

def test_no_lowercase():
    assert is_valid_password("ABCDEFG1!") == False

def test_no_uppercase():
    assert is_valid_password("abcdefg1!") == False
