from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class TestViewAdmin(APIView): 
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("soy admin ")

class TestViewUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("soy Usuario")

class TestViewMode(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("soy moderador ")


class TestViewAll(APIView): 
    def get(self, request):
        return Response('Es de dominio para todos')
       
       
       
       
       
       
       