# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Comment

def home(request):
    return render(request, 'home.html') 

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'crochet_app/project_list.html', {'projects': projects})

# Define the project_detail view
def project_detail(request, project_id):
    # Fetch the project based on the project_id
    project = get_object_or_404(Project, pk=project_id)
    
    # Return the project detail template with the project context
    return render(request, 'project_detail.html', {'project': project})

def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated

    if request.method == 'POST':
        comment_text = request.POST.get('comment')  # Get comment text from the form
        if comment_text:
            # Create a new comment associated with the project and user
            Comment.objects.create(
                project=project,
                user=request.user,
                comment=comment_text
            )
            return redirect('project_detail', project_id=project.id)  # Redirect back to project details

    return render(request, 'crochet_app/add_comment.html', {'project': project})





#from django.shortcuts import render
#from django.views import generic
#from .models import CrochetItem

#class   CrochetList(generic.ListView):
    #model = CrochetItem
    #template_name = "crochet_app/index.html"
    #paginate_by = 6