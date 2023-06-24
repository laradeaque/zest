from django.shortcuts import render
from .models import Order

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        if len(email) > 64:
            email = email[:63]
            
        size = request.POST.get("size")
        occasion = request.POST.get("occasion")
        specs = request.POST.get("specs")
        delivery_date = request.POST.get("d-day")
        
        if not (size is None and occasion is None and delivery_date is None):
            order = Order(
                email = email,
                size = size,
                occasion = occasion,
                specs = specs,
                delivery_date = delivery_date
            )
            order.save()
            return render(request, "order_placed.html")
        elif email is not none:
            newsletter = Newsletter(email=email)
            newsletter.save()
            return render(request, "order_placed.html")
        return render(request, "index.html")
    else:
        return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def bakers(request):
    return render(request, "bakers.html")
