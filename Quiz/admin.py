from django.contrib import admin

# Register your models here.
from .models import Users,questions


class StudentAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    list_display = ("name")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text")

admin.site.register(StudentAdmin)
admin.site.register(QuestionAdmin)