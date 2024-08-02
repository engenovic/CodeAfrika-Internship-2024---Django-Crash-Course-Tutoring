from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['regno', 'first_name', 'last_name', 'email', 'phone']
    list_filter = ['regno']
    search_fields = ['regno', 'first_name']
    show_facets = admin.ShowFacets.ALWAYS

