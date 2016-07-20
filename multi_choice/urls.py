from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from multi_choice import views

urlpatterns = [
    url(r'^multi_choice/$', views.Multi_choiceList.as_view()),
    url(r'^multi_choice/$', views.Multi_choiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)