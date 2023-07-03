import pytest 

@pytest.mark.marca1(reason="NAda que mostrar")
def test_prueba():
    assert 2 == 2

@pytest.fixture(scope="session")
def fixture_1():
    print("desde fixture")
    yield 2
    print("desde fixture after return")

@pytest.mark.marca1(reason="Nada que mostrar")
def test_prueba1(fixture_1):
    print("desde prueba1")
    variable = fixture_1
    assert variable == 2

@pytest.mark.marca1(reason="Nada que mostrar")
def test_prueba2(fixture_1):
    print("desde prueba2")
    variable = fixture_1
    assert variable == 2