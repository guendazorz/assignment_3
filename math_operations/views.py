from django.shortcuts import render
from django.http import HttpResponseBadRequest

def math_form(request):
    return render(request, 'math_form.html')

def math_result(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid method")

    try:
        x = float(request.POST.get('x', 0))
        y = float(request.POST.get('y', 0))
        z = float(request.POST.get('z', 0))
    except ValueError:
        return HttpResponseBadRequest("Inputs must be numbers")

    steps = []
    steps.append(f"Initial value of x: {x}")
    x += y; steps.append(f"After x += y: {x}")
    x -= z; steps.append(f"After x -= z: {x}")
    x *= y; steps.append(f"After x *= y: {x}")
    x = (x % z) if z != 0 else x; steps.append(f"After x %= z: {x}")
    if z != 0:
        x /= z; steps.append(f"After x /= z: {x}")

    final_result = x + y + z

    context = {
        "orig": {"x": request.POST['x'], "y": request.POST['y'], "z": request.POST['z']},
        "steps": steps,
        "final": final_result,
    }
    return render(request, 'result.html', context)

# Create your views here.
