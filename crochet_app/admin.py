from django.contrib import admin
from .models import Project, Comment, Like, Pattern 

# Register Comment model
admin.site.register(Comment)

# Register Like model with customization
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'created_at')
    ordering = ('user',)
    search_fields = ('user__username', 'post__title')

# Register Project model with customization
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'skill_level', 'user', 'created_at')
    search_fields = ('name', 'description', 'user__username')  
    list_filter = ('category', 'skill_level')  
    ordering = ('-created_at',)  

# Register Pattern model with customization
@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ('name', 'description')
    ordering = ('name',)



#@admin.register(CrochetItem)
#class CrochetAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'slug', 'status')
    #search_fields = ['title']
    #list_filter = ('status',)
    #prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)  # Specify the fields to use Summernote editor


