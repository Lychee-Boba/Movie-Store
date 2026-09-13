from django.contrib import admin
from .models import Movie, Review, Report

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class ReportAdmin(admin.ModelAdmin):
    ordering = ['date']
    list_display = [
        'id',
        'movie',
        'review_author',
        'reason',
        'review_text',
        'date'
    ]


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Report)