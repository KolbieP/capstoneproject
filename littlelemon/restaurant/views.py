from django.shortcuts import render
from .models import Booking, MenuItem
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

def home(request):
    return render(request, 'index.html')