from answers.models import Answers
from answers.serializers import AnswersSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class AnswersList(generics.ListCreateAPIView):
 queryset = Answers.objects.all()
 serializer_class = AnswersSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class AnswersDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Answers.objects.all()
 serializer_class = AnswersSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

