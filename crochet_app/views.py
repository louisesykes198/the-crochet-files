from django.shortcuts import render
from django.views import generic
from .models import CrochetItem

class   CrochetList(generic.ListView):
    model = CrochetItem