from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Notification
from .serializers import NotificationSerializer

# Create your views here.


class NotificationDetail(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.none()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        queryset = Notification.objects.filter(user=user)
        return queryset

    def update(self, request, id, *args, **kwargs):
        notification = Notification.objects.get(id=id)
        notification.read_at = timezone.now()
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)
