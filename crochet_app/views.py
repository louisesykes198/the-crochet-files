from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Comment, Like
from .forms import ProjectForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CommentForm

# Home view
def home(request):
    try:
        projects = Project.objects.all()
    except Exception as e:
        print("Error in home view:", e)
        projects = []
    return render(request, 'home.html', {'projects': projects})


# Project List view
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'crochet_app/project_list.html', {'projects': projects})

# Category view (projects based on category)
def category_view(request, category_name):
    projects = Project.objects.filter(category__iexact=category_name)
    return render(request, 'category_view.html', {'projects': projects, 'category': category_name})


# Add Project view
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, "Project added successfully!")
            return redirect('project_list')
        else:
            messages.error(request, "There was an error with your form submission.")
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# Edit Project view
@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Replace 'project_list' with your URL name
    else:
        form = ProjectForm(instance=project)

    return render(request, 'crochet_app/edit_project.html', {'form': form, 'project': project})

# Delete Project view
@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                messages.success(request, "Logged in successfully!")
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Project Detail view (likes and comments handling)
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        if 'like' in request.POST:
            if not Like.objects.filter(project=project, user=request.user).exists():
                Like.objects.create(project=project, user=request.user)
                messages.success(request, "You liked this project!")
            else:
                messages.error(request, "You have already liked this project.")
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment_text')
            if comment_text:
                Comment.objects.create(project=project, user=request.user, comment=comment_text)
                messages.success(request, "Your comment was posted!")
            else:
                messages.error(request, "Comment cannot be empty.")
    comments = Comment.objects.filter(project=project)
    likes = Like.objects.filter(project=project).count()
    return render(request, 'crochet_app/project_detail.html', {
        'project': project,
        'comments': comments,
        'likes': likes
    })

# CustomLoginView for Login
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Add Comment view
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form, 'project': project})

# Toggle Like view
def toggle_like(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
    else:
        project.likes.add(request.user)
    return redirect('project_detail', project_id=project.id)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_view(request):
    return render(request, 'my_template.html')

