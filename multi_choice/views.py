from multi_choice.models import Multi_choice
from multi_choice.serializers import Multi_choiceSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Multi_choiceList(generics.ListCreateAPIView):
 queryset = Multi_choice.objects.all()
 serializer_class = Multi_choiceSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Multi_choiceDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Multi_choice.objects.all()
 serializer_class = Multi_choiceSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

