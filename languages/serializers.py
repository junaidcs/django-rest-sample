from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm', 'desc')
