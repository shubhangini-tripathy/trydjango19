from django.contrib import admin

# Register your models here.
from .models import Post
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__' , 'timestamp']
    class meta:
        model = Post



admin.site.register(Post , PostModelAdmin)
