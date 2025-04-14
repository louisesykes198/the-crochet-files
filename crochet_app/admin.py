from django.contrib import admin
from .models import Project
from .models import Comment
from .models import Like

admin.site.register(Project)
admin.site.register(Comment)
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'project')
    search_fields = ('user__username', 'project__name')
#@admin.register(CrochetItem)
#class CrochetAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'slug', 'status')
    #search_fields = ['title']
    #list_filter = ('status',)
    #prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)  # Specify the fields to use Summernote editor


