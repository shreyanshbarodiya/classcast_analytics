from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def question_stats(request, xblock_id):
	res = models.Classcast_questions.objects.get(xblock_id=xblock_id)
	res_json = serializers.serialize('json', res)
	return HttpResponse(res_json, content_type='application/json')
