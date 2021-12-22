from django.contrib import admin
from blog.models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','time')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

admin.site.register(Category)
admin.site.register(Comment)



