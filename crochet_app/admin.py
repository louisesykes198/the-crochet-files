from django.contrib import admin
from .models import Project, Comment, Like, Pattern

admin.site.register(Comment)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'project')
    search_fields = ('user__username', 'project__name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'skill_level')
    search_fields = ('name', 'description')

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ('name', 'description')


#@admin.register(CrochetItem)
#class CrochetAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'slug', 'status')
    #search_fields = ['title']
    #list_filter = ('status',)
    #prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)  # Specify the fields to use Summernote editor


