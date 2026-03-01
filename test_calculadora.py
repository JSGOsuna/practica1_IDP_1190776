from calculadora import Calculadora
# Test para la función add de la clase Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculadora()
    assert calc.subtract(5, 2) == 5