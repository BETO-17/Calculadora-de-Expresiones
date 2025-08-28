import math

class CalculatorError(Exception):
    """Excepción personalizada para errores en la calculadora."""
    pass

class SafeEvaluator:
    """Clase para evaluar expresiones matemáticas de forma segura."""

    def __init__(self):
        self.allowed_names = {
            name: obj for name, obj in math.__dict__.items()
            if not name.startswith("__")
        }

    def evaluate(self, expression: str) -> float:
        try:
            return eval(expression, {"__builtins__": None}, self.allowed_names)
        except ZeroDivisionError:
            raise CalculatorError("Error: División por cero.")
        except Exception:
            raise CalculatorError("Error: Expresión inválida.")
# Función con el mismo nombre que antes, para no romper el resto del código
def evapression(expr: str) -> float:
    return SafeEvaluator().evaluate(expr)
