from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Project(models.Model):
    # Choices for category
    CATEGORY_CHOICES = [
        ('Blankets', 'Blankets'),
        ('Cardigans', 'Cardigans'),
        ('Amigurumi', 'Amigurumi'),
        ('Scarves', 'Scarves'),
        ('Hats', 'Hats'),
        ('Dishcloths', 'Dishcloths'),
    ]

    # Choices for skill level
    SKILL_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,  
    )
    skill_level = models.CharField(
        max_length=50,
        choices=SKILL_LEVEL_CHOICES,  
    )
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True)  

    # Image and pattern fields
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    pattern = models.FileField(upload_to='projects/patterns/', blank=True, null=True)

    # ForeignKey relation with the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    likes = models.ManyToManyField(User, related_name='liked_projects', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.name}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"Like by {self.user} on {self.project}"

class Pattern(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description
    
class Post(models.Model):
    # … Your other fields for Post model
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()



    

    

