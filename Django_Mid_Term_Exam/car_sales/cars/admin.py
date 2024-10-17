from django.contrib import admin
from .models import Car  # Import your Car model

@admin.register(Car)  # This registers the Car model
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'brand')  # Customize the fields you want to display in the list view
    search_fields = ('title', 'brand__name')  # Allow searching by title and brand name
