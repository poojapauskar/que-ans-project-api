from questions.models import Questions
from questions.serializers import QuestionsSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class QuestionsList(generics.ListCreateAPIView):
 queryset = Questions.objects.all()
 serializer_class = QuestionsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class QuestionsDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Questions.objects.all()
 serializer_class = QuestionsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

