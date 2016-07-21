from questions.models import Questions
from questions.serializers import QuestionsSerializer
from multi_choice.models import Multi_choice
from multi_choice.serializers import Multi_choiceSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)



def get_queryset(request):

  multiple_que= Questions.objects.filter(types="multiple")
  true_false_que= Questions.objects.filter(types="true_false")
  input_que= Questions.objects.filter(types="input")

  import sys
  print sys.stderr, multiple_que
  print sys.stderr, true_false_que
  print sys.stderr, input_que
  
  fields = []

  fields1=[]
  fields2=[]
  fields3=[]

  for obj1 in multiple_que:
      fields1.append(
              {
               'question_id':obj1.id,
               'question':obj1.question,
               'options':(json.dumps(list(Multi_choice.objects.filter(question_id=obj1.id).values_list('options')))).replace('"','').replace('[','').replace(']',''),  
               }
            )

  for obj2 in true_false_que:
      fields2.append(
              {
               'question_id':obj1.id,
               'question':obj2.question,
              }
            )

  for obj3 in input_que:
  	  fields3.append(
              {
               'question_id':obj3.id,
               'question':obj3.question,
              }
            )

  fields.append(
  	     {
  	     	'multi_choice':fields1,
  	     	'true_false':fields2,
  	     	'input':fields3,
  	     }
  	)
    
  print >> sys.stderr,"-----------"
  print >> sys.stderr,fields
  print >> sys.stderr,"-----------"
     
  return JsonResponse((list(fields)),safe=False)
  