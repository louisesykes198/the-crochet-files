from django.contrib import admin
from .models import Project

admin.site.register(Project)
#@admin.register(CrochetItem)
#class CrochetAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'slug', 'status')
    #search_fields = ['title']
    #list_filter = ('status',)
    #prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)  # Specify the fields to use Summernote editor


