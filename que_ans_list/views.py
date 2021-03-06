from que_ans_list.models import Que_ans_list
from que_ans_list.serializers import Que_ans_listSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions

class Que_ans_listList(generics.ListAPIView):
 queryset = Que_ans_list.objects.all()
 serializer_class = Que_ans_listSerializer

class Que_ans_listDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Que_ans_list.objects.all()
 serializer_class = Que_ans_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)




class Update_details(generics.ListCreateAPIView):
 def put(self, request, *args, **kwargs):
  from django.http import JsonResponse

  
  import sys
  firstname= request.data['firstname']
  lastname= request.data['lastname']
  usn= request.data['usn']
  email= request.data['email']
  phone= request.data['phone']
  question_list= request.data['question_list']
  answer_list= request.data['answer_list']
  correct_ans_list= request.data['correct_ans_list']
  session= request.data['session']
  seconds= request.data['seconds']

  print sys.stderr, request.data['firstname']
  print sys.stderr, request.data['lastname']
  print sys.stderr, request.data['usn']
  print sys.stderr, request.data['email']
  print sys.stderr, request.data['phone']
  print sys.stderr, request.data['question_list']
  print sys.stderr, request.data['answer_list']
  print sys.stderr, request.data['correct_ans_list']
  print sys.stderr, request.data['session']
  print sys.stderr, request.data['seconds']


  details=[]
  if(Que_ans_list.objects.filter(usn=usn).filter(session=0)):
    details.append(
                  {
                   'status':400,
                   'message':'Session expired',
                   # 'result':list(update),
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(details[0],safe=False)

  else:
    if(Que_ans_list.objects.filter(usn=usn).exists()):
      objects=Que_ans_list.objects.filter(usn=usn).update(seconds=seconds,firstname=firstname,lastname=lastname,email=email,phone=phone,question_list=question_list,answer_list=answer_list,correct_ans_list=correct_ans_list,session=1)
      details.append(
                  {
                   'status':200,
                   'message':'Data saved',
                   # 'result':list(update),
                  }
                 )
    else:
      objects=Que_ans_list.objects.create(seconds=seconds,firstname=firstname,lastname=lastname,email=email,phone=phone,usn=usn,question_list=question_list,answer_list=answer_list,correct_ans_list=correct_ans_list,session=1)
      details.append(
                  {
                   'status':200,
                   'message':'Data saved',
                   # 'result':list(update),
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(details[0],safe=False)

