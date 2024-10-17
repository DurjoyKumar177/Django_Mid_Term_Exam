from django.urls import path
from .views import OrderHistoryView, CarDetailView, CarListView
from .views import buy_car

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('order-history/', OrderHistoryView.as_view(), name='order_history'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_details'),  
    path('buy_car/<int:car_id>/', buy_car, name='buy_car'),
]
