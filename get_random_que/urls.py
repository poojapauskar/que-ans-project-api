from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_random_que import views

urlpatterns = [
    #url(r'^get_random_que/$', views.Get_listList.as_view()),
    url(r'^get_random_que/$', views.Get_random_que.as_view()),
    #url(r'^get_random_que/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]