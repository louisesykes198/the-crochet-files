# views.py
from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'crochet_app/project_list.html', {'projects': projects})





#from django.shortcuts import render
#from django.views import generic
#from .models import CrochetItem

#class   CrochetList(generic.ListView):
    #model = CrochetItem
    #template_name = "crochet_app/index.html"
    #paginate_by = 6