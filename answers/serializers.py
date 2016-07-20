from rest_framework import serializers
from answers.models import Answers, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ('pk','question_id','answer')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Answers.objects.create(question_id=validated_data.get('question_id'),answer=validated_data.get('answer'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.answer = validated_data.get('answer', instance.answer)
        return instance


