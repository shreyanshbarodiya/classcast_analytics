from django.http import HttpResponse
import classcast.classcast_test_submissions.models as models
from django.http import JsonResponse
from django.core import serializers

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def question_stats(request, xblock_id):
	res = models.Classcast_questions.objects.filter(xblock_id=xblock_id)
	res_json = serializers.serialize('json', res)
	return HttpResponse(res_json, content_type='application/json')
