from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import SignUpSerializer
from ..models import User


class Register(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
