from rest_framework import serializers

from tasks.models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'created_at')
