from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from questions import views

urlpatterns = [
    url(r'^questions/$', views.QuestionsList.as_view()),
    url(r'^questions/$', views.QuestionsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)