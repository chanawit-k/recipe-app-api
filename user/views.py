"""
Views for the user app
"""
from rest_framework import generics
from user.serializers import UserSerializers


class CreateUserview(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializers