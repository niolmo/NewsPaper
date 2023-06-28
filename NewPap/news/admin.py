from django.contrib import admin
from .models import Post, Author


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['postCraTime', 'postType', 'postTitle', 'postText', 'postAuthor', 'postRunk', ]
    list_filter = ['postCraTime', 'postType', 'postTitle', 'postAuthor']
    search_fields = ['postCraTime', 'postTitle', 'postAuthor']
    raw_id_fields = ['postAuthor']
    date_hierarchy = 'postCraTime'
    ordering = ['postCraTime']
@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['author', 'authorRunk']
    search_fields =['author']
    raw_id_fields = ['author']


# from .models import Author, Category, Post, Comment, PostCategory
# admin.site.register(Author)
# admin.site.register(Category)
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(PostCategory)
