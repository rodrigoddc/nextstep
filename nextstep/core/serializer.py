from rest_framework import  serializers
from nextstep.core.models import Person, PersonMedia, PersonMediaType, PersonType


class PersonMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMedia
        fields = '__all__'
        depth = 1


class PersonMediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMediaType
        fields = '__all__'
        depth = 1


class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = '__all__'
        depth = 1


class PersonSerializer(serializers.ModelSerializer):
    media = PersonMediaSerializer()
    media_type = PersonMediaTypeSerializer()
    person_type = PersonTypeSerializer()

    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
