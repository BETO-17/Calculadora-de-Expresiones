from django.shortcuts import render
from .calculator import evaluate_expression, CalculatorError

def index(request):
    result = None
    error = None

    if request.method == "POST":
        expr = request.POST.get("expr", "")
        try:
            result = evaluate_expression(expr)
        except CalculatorError as e:
            error = str(e)

    return render(request, "index.html", {"result": result, "error":error})