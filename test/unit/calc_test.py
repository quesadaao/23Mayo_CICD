import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))        

    def test_substract_results(self):
        #Pruebas success 
        self.assertEqual(4, self.calc.substract(8, 4))
        self.assertEqual(0, self.calc.substract(10, 10))
        self.assertEqual(0, self.calc.substract(50, 50))
        self.assertEqual(1, self.calc.substract(1, 0))                
    
    def test_substract_results_failures(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object()) 

    def test_multiply_results(self):
        #Pruebas success 
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(10, 0))
        self.assertEqual(0, self.calc.multiply(50, 0))
        self.assertEqual(1, self.calc.multiply(1, 1))                
    
    def test_multiply_results_failures(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        
    def test_power_results(self):
        #Pruebas success 
        self.assertEqual(32, self.calc.power(2, 5))
    
    def test_power_results_failures(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        
    def test_raizCuadrada_results(self):
        #Pruebas success 
        self.assertEqual(3, self.calc.raizCuadrada(9))
    
    def test_raizCuadrada_results_failures(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.raizCuadrada, "2")
        self.assertRaises(TypeError, self.calc.raizCuadrada, -50)
        self.assertRaises(TypeError, self.calc.raizCuadrada, "8") 
        
    def test_log10_results(self):
        #Pruebas success 
        self.assertEqual(1, self.calc.log10(10))

    def test_log10_results_failures(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, -50)
        self.assertRaises(TypeError, self.calc.log10, "8")                

    def test_check_types_results(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.check_types, "2",2)
        self.assertRaises(TypeError, self.calc.check_types, object(),2)
        self.assertRaises(TypeError, self.calc.check_types, "8",2) 
    
    def test_check_type_results(self):
        #Pruebas with failures
        self.assertRaises(TypeError, self.calc.check_type, "2")
        self.assertRaises(TypeError, self.calc.check_type, object())
        self.assertRaises(TypeError, self.calc.check_type, "8")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
