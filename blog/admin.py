from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post, CategoryPost

# Register your models here.


@admin.register(CategoryPost)
class CategoryPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Post)
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
