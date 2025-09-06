from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Course, Lesson_about, Review

@admin.register(Course)
class CourseAdmin(TranslatableAdmin):
    list_display = ('title', 'category', 'price', 'is_free')
    exclude = ('num_ratings', 'rating', 'num_students')


@admin.register(Lesson_about)
class LessonAdmin(TranslatableAdmin):
    list_display = ('title', 'course', 'duration')
    search_fields = ('translations__title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course',  'date_posted')
    search_fields = ('student_name', 'course__translations__title')
