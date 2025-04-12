from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CrochetItem  # Import your model

@admin.register(CrochetItem)
class CrochetAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)  # Specify the fields to use Summernote editor


