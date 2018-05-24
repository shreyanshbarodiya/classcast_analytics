from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    url(r'^hello$', views.hello, name = 'hello'),
    url(r'^question_stats/(?P<xblock_id>[A-Za-z0-9_.-]+)/$', views.question_stats, name='question_stats'),
)
