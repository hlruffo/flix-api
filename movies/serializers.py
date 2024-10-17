from rest_framework import serializers
from .models import Movie
import datetime 


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
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