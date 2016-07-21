from que_ans_list.models import Que_ans_list
from que_ans_list.serializers import Que_ans_listSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Que_ans_listList(generics.ListCreateAPIView):
 queryset = Que_ans_list.objects.all()
 serializer_class = Que_ans_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Que_ans_listDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Que_ans_list.objects.all()
 serializer_class = Que_ans_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

