from rest_framework import serializers

from core.constants import AdoptionStatus
from core.models import Animal, AnimalAdoptions


class CreateAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = ('name', 'breed', 'health_status', 'species', 'age')

class RetrieveAnimalDetails(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Animal
        fields = ('id', 'name', 'breed', 'health_status', 'species', 'status', 'age')

    def get_status(self, obj):
        return AdoptionStatus(obj.status).name

class RequestAdoptionSerializer(serializers.ModelSerializer):

    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), many=False)
    description =  serializers.CharField(
        required=True,
        error_messages={
            'required' : "This field is required."
        }
    )
    class Meta:
        model = AnimalAdoptions
        fields = ('animal', 'description')


class RetrieveAdoptionsRequests(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.email')
    animal_name = serializers.CharField(source='animal.name')

    class Meta:
        model = AnimalAdoptions

        fields = ('username', 'animal_name', 'status')

    def get_status(self, obj):
        return AdoptionStatus(obj.status).name