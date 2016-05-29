from django.contrib import admin

# Register your models here.

from .models import Question,Answer

class AnswerInTabularInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInTabularInline]
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
