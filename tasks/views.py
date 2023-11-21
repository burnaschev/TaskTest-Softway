from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from tasks.models import Task
from tasks.paginators import TaskPaginator
from tasks.serializers import TaskSerializers


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    pagination_class = TaskPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status', 'created_at',)

    def perform_create(self, serializer):
        new_task = serializer.save(user=self.request.user)
        new_task.user = self.request.user
        new_task.save()
