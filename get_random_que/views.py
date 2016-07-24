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

class Get_random_que(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):

  import sys
  print sys.stderr, request.META.get('HTTP_MULTI'),
  print sys.stderr, request.META.get('HTTP_INPUT'),

  my_string1 = request.META.get('HTTP_MULTI')
  my_list1 = my_string1.split(",")

  my_string2 = request.META.get('HTTP_INPUT')
  my_list2 = my_string2.split(",")

  
  fields = []

  fields1=[]
  fields2=[]

  for index1 in range(len(my_list2)):
    input_que= Questions.objects.filter(types="input").filter(pk=my_list2[index1])
    print sys.stderr, "---------input_que----------"
    print sys.stderr, input_que
    for obj2 in input_que:
      fields2.append(
              {
               'question_id':obj2.id,
               'question':obj2.question,
              }
            )
  
  for index in range(len(my_list1)):
    multiple_que= Questions.objects.filter(types="multiple").filter(pk=my_list1[index])
    print sys.stderr, "---------multiple_que----------"
    print sys.stderr, multiple_que
    for obj1 in multiple_que:
        fields1.append(
                {
                 'question_id':obj1.id,
                 'question':obj1.question,
                 'options':(json.dumps(list(Multi_choice.objects.filter(question_id=obj1.id).values_list('options')))).replace('"','').replace('[','').replace(']',''),  
                 }
              )


  fields.append(
         {
          'multi_choice':fields1,
          'input':fields2,
         }
    )
    
  # print >> sys.stderr,"-----------"
  # print >> sys.stderr,fields
  # print >> sys.stderr,"-----------"
  
  import sys
  from django.http import JsonResponse   
  return JsonResponse((list(fields)),safe=False)



  