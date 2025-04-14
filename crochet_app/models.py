from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Blankets', 'Blankets'),
        ('Cardigans', 'Cardigans'),
        ('Amigurumi', 'Amigurumi'),
        ('Scarves', 'Scarves'),
        ('Hats', 'Hats'),
        ('Dishcloths', 'Dishcloths'),
    ]

    SKILL_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES, default='Beginner')
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True, default='')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='projects/images/', blank=True)
    pattern = models.FileField(upload_to='projects/patterns/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Projects"

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
    
    # Like model to track project likes
class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')  # Prevents duplicate likes

    def __str__(self):
        return f"Like by {self.user.username} on {self.project.name}"



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

    

    

