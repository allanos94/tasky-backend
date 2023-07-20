from rest_framework import viewsets
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskModelSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """ Task view model set """
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    # permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(serializer.data)
