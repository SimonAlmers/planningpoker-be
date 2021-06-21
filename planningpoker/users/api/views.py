from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..models import User
from .serializers import SignUpSerializer


class Register(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
