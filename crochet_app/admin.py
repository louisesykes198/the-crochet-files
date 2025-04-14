from django.contrib import admin
from .models import Project, Comment, Like, Pattern 

# Register Comment model
admin.site.register(Comment)

# Register Like model with customization
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'project')
    search_fields = ('user__username', 'project__name')
    # Optional: You can also add ordering here
    ordering = ('user',)

# Register Project model with customization
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'skill_level', 'user', 'created_at')
    search_fields = ('name', 'description', 'user__username')  # Allow searching by username
    list_filter = ('category', 'skill_level')  # Filter by category and skill level
    ordering = ('-created_at',)  # Ordering by creation date (latest first)

# Register Pattern model with customization
@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ('name', 'description')
    # Optional: You could add ordering for patterns as well
    ordering = ('name',)



#@admin.register(CrochetItem)
#class CrochetAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'slug', 'status')
    #search_fields = ['title']
    #list_filter = ('status',)
    #prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)  # Specify the fields to use Summernote editor


