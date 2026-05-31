from django.contrib import admin
from .models import Documents, Category
from users.models import MainUser

# Register your models here.

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'slug', 'price', 'description', 'image')
    list_display_links = ('id', 'user', 'name', 'slug')
    search_fields = ('name', 'price', 'description', 'slug')
    list_editable = ('image',)
    list_filter = ('time_create',)
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'avatar', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('email', 'username')

admin.site.register(Documents, DocumentsAdmin)
admin.site.register(MainUser, UserAdmin)
admin.site.register(Category, CategoryAdmin)