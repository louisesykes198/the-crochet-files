from django.shortcuts import render
from django.views import generic
from .models import CrochetItem

class   CrochetList(generic.ListView):
    model = CrochetItem
    template_name = "crochet_app/index.html"
    paginate_by = 6