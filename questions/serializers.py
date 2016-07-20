from rest_framework import serializers
from questions.models import Questions, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('pk','question','types')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Questions.objects.create(question=validated_data.get('question'),types=validated_data.get('types'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.question = validated_data.get('question', instance.question)
        instance.types = validated_data.get('types', instance.type)
        return instance


