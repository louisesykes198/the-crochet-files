from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    description = models.TextField(blank=True, null=True)  # Optional description
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,  # Apply the category choices
    )
    skill_level = models.CharField(
        max_length=50,
        choices=SKILL_LEVEL_CHOICES,  # Apply the skill level choices
    )
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True)  # Optional notes

    # Image and pattern fields
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    pattern = models.FileField(upload_to='projects/patterns/', blank=True, null=True)

    # ForeignKey relation with the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    likes = models.ManyToManyField(User, related_name='liked_projects', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Optional: Track when the comment was created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.name}"


class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='likes_set')  # Custom related_name
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')  # Prevents duplicate likes

    def __str__(self):
        return f"Like by {self.user.username} on {self.project.name}"


class Pattern(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description






#STATUS = ((0, "Draft"), (1, "Published"))

#class CrochetItem(models.Model):
    #title = models.CharField(max_length=200, unique=True)
    #slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(
        #User, on_delete=models.CASCADE, related_name="blog_posts", default=1
    #)
    #description = models.TextField()
    #created_on = models.DateTimeField(auto_now_add=True)
    #status = models.IntegerField(choices=STATUS, default=0)
    #excerpt = models.TextField(blank=True, null=True) 
    #updated_on = models.DateTimeField(auto_now=True)
    
    #class Meta:
        #ordering = ["-created_on"]

    #def __str__(self):
        #return f"{self.title} | written by {self.author}"
    
    # Comment model to store user comments on projects
#class Comment(models.Model):
    #crochet_project = models.ForeignKey(CrochetItem, on_delete=models.CASCADE, related_name="comments")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #comment = models.TextField()
    #approved = models.BooleanField(default=False)
    #created_on = models.DateTimeField(auto_now_add=True) 
    
    #class Meta:
        #ordering = ["created_on"]

    #def __str__(self):
        #return f"Comment by {self.user} on {self.crochet_project}"

    

    

