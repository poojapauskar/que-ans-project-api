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
  print sys.stderr, request.META.get('HTTP_MULTI1'),
  print sys.stderr, request.META.get('HTTP_MULTI2'),
  print sys.stderr, request.META.get('HTTP_MULTI3'),
  print sys.stderr, request.META.get('HTTP_INPUT'),

  my_string1 = request.META.get('HTTP_MULTI1')
  my_list1 = my_string1.split(",")

  my_string2 = request.META.get('HTTP_MULTI2')
  my_list2 = my_string2.split(",")

  my_string3 = request.META.get('HTTP_MULTI3')
  my_list3 = my_string3.split(",")

  my_string4 = request.META.get('HTTP_INPUT')
  my_list4 = my_string4.split(",")

  
  fields = []

  fields1=[]
  fields2=[]
  fields3=[]
  fields4=[]

  for index1 in range(len(my_list1)):
    multiple_que1= Questions.objects.filter(types="multiple").filter(pk=my_list1[index1])
    print sys.stderr, "---------multiple_que1----------"
    print sys.stderr, multiple_que1
    for obj1 in multiple_que1:
        fields1.append(
                {
                 'question_id':obj1.id,
                 'question':obj1.question,
                 'options':(json.dumps(list(Multi_choice.objects.filter(question_id=obj1.id).values_list('options')))).replace('"','').replace('[','').replace(']',''),  
                 }
              )

  for index2 in range(len(my_list2)):
    multiple_que2= Questions.objects.filter(types="multiple").filter(pk=my_list2[index2])
    print sys.stderr, "---------multiple_que2----------"
    print sys.stderr, multiple_que2
    for obj2 in multiple_que2:
        fields2.append(
                {
                 'question_id':obj2.id,
                 'question':obj2.question,
                 'options':(json.dumps(list(Multi_choice.objects.filter(question_id=obj2.id).values_list('options')))).replace('"','').replace('[','').replace(']',''),  
                 }
              )

  for index3 in range(len(my_list3)):
    multiple_que3= Questions.objects.filter(types="multiple").filter(pk=my_list3[index3])
    print sys.stderr, "---------multiple_que3----------"
    print sys.stderr, multiple_que3
    for obj3 in multiple_que3:
        fields3.append(
                {
                 'question_id':obj3.id,
                 'question':obj3.question,
                 'options':(json.dumps(list(Multi_choice.objects.filter(question_id=obj3.id).values_list('options')))).replace('"','').replace('[','').replace(']',''),  
                 }
              )

  for index4 in range(len(my_list4)):
    input_que= Questions.objects.filter(types="input").filter(pk=my_list4[index4])
    print sys.stderr, "---------input_que----------"
    print sys.stderr, input_que
    for obj4 in input_que:
      fields4.append(
              {
               'question_id':obj4.id,
               'question':obj4.question,
              }
            )
  
  


  fields.append(
         {
          'multi_choice_easy':fields1,
          'multi_choice_medium':fields2,
          'multi_choice_difficult':fields3,
          'input':fields4,
         }
    )
    
  # print >> sys.stderr,"-----------"
  # print >> sys.stderr,fields
  # print >> sys.stderr,"-----------"
  
  import sys
  from django.http import JsonResponse   
  return JsonResponse((list(fields)),safe=False)



  