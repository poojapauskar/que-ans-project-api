from que_ans_list.models import Que_ans_list
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

  fields = []
      

  # usn = request.META.get('HTTP_USN')
  usn = '2gi10ec122'
  import sys
  print sys.stderr, usn

  if(Que_ans_list.objects.filter(usn=usn).exists()):
    if(Que_ans_list.objects.filter(usn=usn).filter(session=1).exists()):
    	fields.append(
              {
               'status':400,
               'message':'Usn exists, session active',
               'question_list':list(Que_ans_list.objects.filter(usn=usn).values_list('question_list')),
               'answer_list':list(Que_ans_list.objects.filter(usn=usn).values_list('answer_list')),
               }
            )
    	return JsonResponse((list(fields)),safe=False)
    else:
      fields.append(
              {
               'status':401,
               'message':'Usn exists, session expired',
               'question_list':list(Que_ans_list.objects.filter(usn=usn).values_list('question_list')),
               'answer_list':list(Que_ans_list.objects.filter(usn=usn).values_list('answer_list')),
               }
            )
      return JsonResponse((list(fields)),safe=False)
  else:
    fields.append(
              {
               'status':200,
               'message':'New user',
               }
            )
    return JsonResponse((list(fields)),safe=False)
  
  #return objects


 