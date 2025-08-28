from django.test import TestCase
from .calculator import evaluate_expression, CalculatorError

class CalculatorTests(TestCase):
    def test_precedence(self):
        self.assertEqual(evaluate_expression("2+3*4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate_expression("(2+3)*4"), 20)

    def test_invalid_expr(self):
        with self.assertRaises(CalculatorError):
            evaluate_expression("2+*3")
