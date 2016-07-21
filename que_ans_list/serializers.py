from rest_framework import serializers
from que_ans_list.models import Que_ans_list, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class Que_ans_listSerializer(serializers.ModelSerializer):

    class Meta:
        model = Que_ans_list
        fields = ('pk','name','usn','question_list','answer_list')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Que_ans_list.objects.create(name=validated_data.get('name'),usn=validated_data.get('usn'),question_list=validated_data.get('question_list'),answer_list=validated_data.get('answer_list'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.question_list = validated_data.get('question_list', instance.question_list)
        instance.answer_list = validated_data.get('answer_list', instance.answer_list)
        return instance


