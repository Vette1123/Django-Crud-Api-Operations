from django.contrib import admin
from .models import Track, Student


class CustomStudent(admin.ModelAdmin):
    fieldsets = (['Student information', {'fields': [
        'Frst_Name', 'Last_Name', 'Age', 'Email', 'Phone']}],
        ['Student MetaData', {'fields': ['address', 'student_track']}],)
    list_display = ('Frst_Name', 'Last_Name', 'Age',
                    'Email', 'Phone', 'student_track', 'is_adult')
    search_fields = ['Frst_Name', 'Last_Name', 'Email', 'Age']
    list_filter = ('Age', 'student_track__title')


class inlineStudent(admin.StackedInline):
    model = Student
    extra = 0


class CustomTrack(admin.ModelAdmin):
    inlines = [inlineStudent]
    fieldsets = (['Track information', {'fields': [
        'title', 'description']}],)
    list_display = ('title', 'description')


# Register your models here.
admin.site.register(Track, CustomTrack)
admin.site.register(Student, CustomStudent)
