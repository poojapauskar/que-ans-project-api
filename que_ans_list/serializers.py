from rest_framework import serializers
from que_ans_list.models import Que_ans_list, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class Que_ans_listSerializer(serializers.ModelSerializer):

    class Meta:
        model = Que_ans_list
        fields = ('pk','firstname','session','lastname','email','phone','usn','question_list','answer_list','correct_ans_list')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        if(Que_ans_list.objects.filter(usn=validated_data.get('usn')).exists()):
         objects=Que_ans_list.objects.filter(usn=validated_data.get('usn')).update(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),question_list=validated_data.get('question_list'),answer_list=validated_data.get('answer_list'),correct_ans_list=validated_data.get('correct_ans_list'),session=1)
        else:
         objects=Que_ans_list.objects.create(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),usn=validated_data.get('usn'),question_list=validated_data.get('question_list'),answer_list=validated_data.get('answer_list'),correct_ans_list=validated_data.get('correct_ans_list'),session=1)
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.usn = validated_data.get('usn', instance.usn)
        instance.answer_list = validated_data.get('answer_list', instance.answer_list)
        instance.question_list = validated_data.get('question_list', instance.question_list)
        instance.correct_ans_list = validated_data.get('correct_ans_list', instance.correct_ans_list)
        instance.session = validated_data.get('session', instance.session)

        return instance


