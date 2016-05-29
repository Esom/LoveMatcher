from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from .models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)

=======
from .models import Question,Answer

class AnswerInTabularInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInTabularInline]
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
>>>>>>> 7b3d3c2e362e94caa18b2f5acca1f07ae3809da8
