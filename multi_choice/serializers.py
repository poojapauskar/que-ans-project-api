from rest_framework import serializers
from multi_choice.models import Multi_choice, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class Multi_choiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multi_choice
        fields = ('pk','question_id','options')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        objects=Multi_choice.objects.create(question_id=validated_data.get('question_id'),options=validated_data.get('options'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.options = validated_data.get('options', instance.options)
        return instance


