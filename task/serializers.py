from rest_framework import serializers

from task.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    """Task model serializer."""

    class Meta:
        """Meta class."""

        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
        )