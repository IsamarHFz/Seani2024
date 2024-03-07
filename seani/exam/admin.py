from django.contrib import admin
from .models import ExamModule, Exam
# Register your models here.
from .models import Stage

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['stage', 'month', 'year']

class ExamModuleIn(admin.TabularInline):
    model = ExamModule
    extra = 1
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'career', 'stage', 'score']
    list_filter = ['career', 'stage']
    inlines = [ExamModuleIn]