'''
Unit test the calculator class

Created Summer, 2015

@author: kvlinden
'''
import unittest

from old.lab11 import Calculator


class Test(unittest.TestCase):

    def setUp(self):
        ''' 
        Set up the calculator for each of the unit tests 
        This function is run once, before each of the test methods below.
        '''
        self.calc = Calculator()

    def test_addition(self):
        try:
            assert self.calc.calculate('0', '+', '1') == 1
            assert self.calc.calculate('3', '+', '9') == 12
            assert self.calc.calculate('-4', '+', '-8') == -12
            assert self.calc.calculate('-7', '+', '9') == 2
            assert self.calc.calculate('3', '+', '0') == 3
            assert self.calc.calculate('2.0', '+', '5.3') == 7.3
        except:
            self.fail('This should not raise an exception.')
            
    def test_subtraction(self):
        try:
            assert self.calc.calculate('3', '-', '9') == -6
            assert self.calc.calculate('-4', '-', '-8') == 4
            assert self.calc.calculate('-7', '-', '9') == -16
            assert self.calc.calculate('3', '-', '0') == 3
            assert self.calc.calculate('2.0', '-', '5.3') == -3.3
        except:
            self.fail('This should not raise an exception.')
            
    def test_division(self):
        try:
            assert self.calc.calculate('3', '/', '12') == 0.25
            assert self.calc.calculate('-4', '/', '-8') == 0.5
            assert self.calc.calculate('16', '/', '-8') == -2
            assert self.calc.calculate('0', '/', '3') == 0
            assert self.calc.calculate('-5.0', '/', '2') == -2.5
        except:
            self.fail('This should not raise an exception.')

    def test_multiplication(self):
        try:
            assert self.calc.calculate('3', '*', '9') == 27
            assert self.calc.calculate('-4', '*', '-8') == 32
            assert self.calc.calculate('-7', '*', '9') == -63
            assert self.calc.calculate('3', '*', '0') == 0
            assert self.calc.calculate('2.0', '*', '5.3') == 10.6
        except:
            self.fail('This should not raise an exception.')
        
    def test_exceptions(self):
        # Test the bad operator exception.
        try:
            self.calc.calculate(4, 'f', '9')
            self.fail('This should raise an exception.')
        except Exception as e:
            assert isinstance(e, ValueError)
            assert e.__str__() == 'Invalid operation: f'
        
        # Test the divide by zero exception.
        try:
            self.calc.calculate(5, '/', 0)
            self.fail('This should raise an exception.')
        except Exception as e:
            assert isinstance(e, ZeroDivisionError)
            assert e.__str__() == 'float division by zero'
            
        # Test the bad operand exception
        try:
            self.calc.calculate('hi', '+', '9')
            self.fail('This should raise an exception.')
        except Exception as e:
            assert isinstance(e, ValueError)
            assert e.__str__() == "could not convert string to float: 'hi'"


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
