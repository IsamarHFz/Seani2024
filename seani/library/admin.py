from django.contrib import admin
from .models import Module, Question
# Register your models here.

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 3

@admin.register(Module)
class MouleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestionInLine]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question_text', 'module', 'correct']
    list_filter = ['module']