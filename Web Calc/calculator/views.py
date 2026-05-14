from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operation = request.POST.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = "Cannot divide by zero" if num2 == 0 else num1 / num2

    return render(request, "calculator/home.html", {"result": result})
