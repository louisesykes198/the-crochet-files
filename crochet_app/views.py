# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Comment, Like, Pattern
from .forms import ProjectForm
from django.contrib.auth.views import LoginView


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

# Project Detail view (likes and comments handling)
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    from .models import Project, Like

def toggle_like(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    like, created = Like.objects.get_or_create(user=request.user, project=project)

    if not created:
        # If the like already exists, unlike it
        like.delete()

    return redirect('project_detail', project_id=project_id)

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # Optionally assign user, timestamps, etc.
            # project.user = request.user
            project.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'your_template_folder/form.html', {'form': form})

def pattern_list(request):
    patterns = Pattern.objects.all()
    return render(request, 'crochet_app/pattern_list.html', {'patterns': patterns})

def pattern_detail(request, pk):
    pattern = get_object_or_404(Pattern, pk=pk)
    return render(request, 'crochet_app/pattern_detail.html', {'pattern': pattern})

class CustomLoginView(LoginView):
    template_name = 'your_custom_path/login.html'






#from django.shortcuts import render
#from django.views import generic
#from .models import CrochetItem

#class   CrochetList(generic.ListView):
    #model = CrochetItem
    #template_name = "crochet_app/index.html"
    #paginate_by = 6