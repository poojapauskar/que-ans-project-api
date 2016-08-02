from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from que_ans_list import views

urlpatterns = [
    # url(r'^que_ans_list/$', views.Que_ans_listList.as_view()),
    url(r'^que_ans_list/(?P<pk>[0-9]+)/$', views.Que_ans_listDetail.as_view()),


    url(r'^update_details/$', views.Que_ans_listList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)