from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello from the listings app!")

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer