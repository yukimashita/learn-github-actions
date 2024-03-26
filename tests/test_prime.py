from prime import is_prime


def test_1_is_not_prime():
    assert not is_prime(1)


def test_2_is_prime():
    assert is_prime(2)


def test_3_is_prime():
    assert is_prime(3)


def test_4_is_not_prime():
    assert not is_prime(4)


def test_5_is_prime():
    assert is_prime(5)


def test_6_is_not_prime():
    assert not is_prime(6)


def test_7_is_prime():
    assert is_prime(7)


def test_8_is_not_prime():
    assert not is_prime(8)


def test_9_is_not_prime():
    assert not is_prime(9)


def test_10_is_not_prime():
    assert not is_prime(10)
