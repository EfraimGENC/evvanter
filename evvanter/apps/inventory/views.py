from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Location, Inventory
from .serializers import LocationSerializer, InventorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
