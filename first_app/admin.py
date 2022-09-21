from django.contrib import admin

from .models import Book, Publisher
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price','isbn']
    # list_editable = ['genre']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']
    # fieldsets = ({'date': ('date_published',)},{'name': ('title','isbn')})


# admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
