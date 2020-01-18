from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
<<<<<<< HEAD
from .models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)

=======
from .models import Question,Answer
=======
from .models import Question,Answer, UserAnswer
>>>>>>> 609b2ae3992f5730ec42b4e127ed9ba52d0cb79f

class AnswerInTabularInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInTabularInline]
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
<<<<<<< HEAD
>>>>>>> 7b3d3c2e362e94caa18b2f5acca1f07ae3809da8
=======
admin.site.register(UserAnswer)

>>>>>>> 609b2ae3992f5730ec42b4e127ed9ba52d0cb79f
