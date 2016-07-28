from django.db import models
import time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
from random import randint

from django.contrib.postgres.fields import ArrayField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='questions')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Que_ans_list(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=True,default='')
    lastname = models.CharField(max_length=100, blank=True,default='')
    email = models.CharField(max_length=100, blank=True,default='')
    phone = models.CharField(max_length=100, blank=True,default='')
    usn = models.CharField(max_length=100, blank=True,default='')
    question_list = ArrayField(models.TextField(blank=True, default='',editable=True))
    answer_list = ArrayField(models.TextField(blank=True, default='',editable=True))
    correct_ans_list = ArrayField(models.TextField(blank=True, default='',editable=True))
   
    class Meta:
        ordering = ('created',)

