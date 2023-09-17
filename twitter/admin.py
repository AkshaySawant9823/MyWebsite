from django.contrib import admin
from .models import StudentInfo
# Register your models here.

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'username', 'time', 'upvotes', 'downvotes', 'comments', 'tweet_text')