from django.contrib import admin
from .models import Category, Blog, Photos


class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'add_image')
    list_display_links = ('id', 'image')


class PhodoAdd(admin.StackedInline):
    model = Photos


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'time_cre', 'photo', 'published')

    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    list_editable = ('published',)
    list_filter = ('published', 'time_cre', 'title')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Photos, PhotosAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
