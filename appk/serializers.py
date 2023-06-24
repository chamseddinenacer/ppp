from rest_framework import serializers
from .models import *



class AnimauxlostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animauxlost
        fields = ('id','userlost', 'name','bred','size','species', 'age','descri','couleur','gender','distmarkings','addrs','datelost','image')
        read_only_fields = ('id',)

    def validate_publication_date(self, value):
        # Add custom validation logic for publication date
        # For example, ensure the publication date is not in the future
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value   



class AnimauxfoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animauxfound
        fields = ('id','userfound','bred','size','species', 'age','descri','couleur','gender','distmarkings','addrs','datefound','image')
        read_only_fields = ('id',)

    def validate_publication_date(self, value):
        # Add custom validation logic for publication date
        # For example, ensure the publication date is not in the future
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value   


 

class AnimauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animaux
        fields = ('id','useridan','name','bred','size','species', 'age','descri','couleur','gender','distmarkings','addrs','daten','image')
        read_only_fields = ('id',)

    def validate_publication_date(self, value):
        # Add custom validation logic for publication date
        # For example, ensure the publication date is not in the future
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value   


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id','userid','animid')
        read_only_fields = ('id',)


