from django.contrib.auth import get_user_model
from questions.models import UserAnswer

User = get_user_model()

users = User.objects.all()
all_user_answers  = UserAnswer.objects.all().order_by("user__id")


somkyd_esom = users[0]
alex_onozor =  users[1]

UserAnswer.objects.filter(user=somkyd_esom)
UserAnswer.objects.filter(user=alex_onozor)

Somkyd = somkyd_esom.useranswer_set.all()[0]
Alex = alex_onozor.useranswer_set.all()[0]


Somkyd.question.id == Alex.question.id


SomkydAns = Somkyd.my_answer
SomkydPref = Somkyd.their_answer

AlexAns = Alex.my_answer
AlexPref = Alex.their_answer

SomkydAns ==  AlexPref
SomkydPref ==  AlexAns


def get_match(user_a, user_b):
	user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
	user_b_answers = UserAnswer.objects.filter(user=user_b)[0]
	if user_a_answers.question.id == user_b_answers.question.id:
		user_a_answer = user_a_answers.my_answer
		user_a_pref = user_a_answers.their_answer
		user_b_answer = user_b_answers.my_answer
		user_b_pref = user_b_answers.their_answer
		if user_a_answer == user_b_pref:
			print "%s fits with %s preference" %(user_a_answers.user.username,user_b_answers.user.username)
		if user_a_pref == user_b_answer:
			print "%s fits with %s answer" %(user_a_answers.user.username,user_b_answers.user.username)
		if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
			print "This is an ideal answer for both"

get_match(somkyd_esom, alex_onozor)






