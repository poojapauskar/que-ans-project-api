"""bitchatapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('questions.urls')),
    url(r'^', include('answers.urls')),
    url(r'^', include('multi_choice.urls')),
    url(r'^', include('get_random_que.urls')),
    url(r'^', include('que_ans_list.urls')),
    url(r'^', include('check_usn_exists.urls')),
    url(r'^', include('set_session_0.urls')),
    url(r'^', include('deactivate_all_sessions.urls')),
    url(r'^', include('check_session_is_0.urls')),
]
