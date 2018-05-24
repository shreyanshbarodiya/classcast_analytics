from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    url(r'^hello$', views.hello, name = 'hello'),
    url(r'^question_stats/<xblock_id>$', views.question_stats, name='question_stats'),
)
