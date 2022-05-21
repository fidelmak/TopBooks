from django.contrib import admin

from .models import Book, author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields=("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter=("Author", "rating",)
    list_display = ("Author", "title")

admin.site.register(Book, BookAdmin)
admin.site.register(author)
admin.site.register(Address)
admin.site.register(Country)