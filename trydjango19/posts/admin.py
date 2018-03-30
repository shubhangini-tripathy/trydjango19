from django.contrib import admin

# Register your models here.
from .models import Post
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["timestamp"]
    search_fields = ["title","content"]
    list_editable = ["title"]
    class meta:
        model = Post



admin.site.register(Post , PostModelAdmin)
