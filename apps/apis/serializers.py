import json

from rest_framework import serializers

from apps.Products.models import Command, Argument, Source
from apps.Servers.models import TemplateServer, ServerProfile, Parameters
from apps.Testings.models import Keyword, Collection
from apps.Users.models import Task


class ArgumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = '__all__'


class SourceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class CommandsSerializer(serializers.ModelSerializer):
    arguments = ArgumentsSerializer(many=True)
    source = SourceSerialzer(many=True)

    class Meta:
        model = Command
        fields = '__all__'


class BasicCommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = [
            'id',
            'name',
            'description'
        ]


class ParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = '__all__'


class TemplateServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateServer
        fields = '__all__'

    def create(self, validated_data):
        params = json.loads(self.initial_data['params'])
        template = TemplateServer.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            category=validated_data['category']
        )
        for param in params:
            template.parameters.add(param)
        template.save()
        return template


class KeywordsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Keyword
        fields = '__all__'


class ServerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerProfile
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'