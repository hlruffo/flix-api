from rest_framework import serializers
from .models import Movie
from django.db.models import Avg

import datetime 


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_rate(self, obj):
        #import ipdb ; ipdb.set_trace()
        reviews_avg = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        #reviews = obj.reviews.all()
        if reviews_avg:
            # total = 0
            # for review in reviews:
            #     total += review.stars
            # reviews_count = reviews.count()
            # return round(total / reviews_count, 2)
            return round(reviews_avg, 2)
        return "Ainda não há notas para este filme."     
        
        
    def validade_release_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Data de lançamento não pode ser maior que a data atual.")
        
        if value < datetime.date(1900, 1, 1):
            raise serializers.ValidationError("Data de lançamento não pode ser menor que 01/01/1900.")
        return value
    
    def validate_resume(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("O resumo deve ter no mínimo 10 caracteres.")
        
        if len(value) > 500:
            raise serializers.ValidationError("O resumo deve ter no máximo 500 caracteres.")
        return value