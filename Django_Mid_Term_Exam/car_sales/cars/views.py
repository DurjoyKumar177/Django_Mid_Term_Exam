from django.views.generic import ListView
from orders.models import Order
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Car
from django.contrib.auth.decorators import login_required

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'  
    context_object_name = 'cars'  

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    def get_object(self):
        return get_object_or_404(Car, id=self.kwargs['pk'])  # Use 'pk' to get car by ID


class OrderHistoryView(ListView):
    model = Order
    template_name = 'profile.html'  
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.quantity > 0:
        car.quantity -= 1  # Reduce quantity
        car.save()  

        # Create an Order record 
        Order.objects.create(user=request.user, car=car)

        return redirect('profile')  
    else:
        return redirect('home')  