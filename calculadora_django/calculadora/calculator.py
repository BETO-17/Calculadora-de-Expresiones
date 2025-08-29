import math

class CalculatorError(Exception):
    """Excepción personalizada para errores en la calculadora."""
    pass

class SafeEvaluator:
    """Clase para evaluar expresiones matemáticas de forma segura."""

    def _init_(self):
        self.allowed_names = {
            name: obj for name, obj in math._dict_.items()
            if not name.startswith("")
        }

    def evaluate(self, expression: str) -> float:
        try:
            return eval(expression, {"_builtins_": None}, self.allowed_names)
        except ZeroDivisionError:
            raise CalculatorError("Error: División por cero.")
        except Exception:
            raise CalculatorError("Error: Expresión inválida.")
# Función con el mismo nombre que antes, para no romper el resto del código
def evapression(expr: str) -> float:
    return SafeEvaluator().evaluate(expr)