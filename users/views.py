from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from django.contrib.auth.models import User
import jwt, datetime
from rest_framework.authtoken.models import Token
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response()
        try:
            serializer.save()
            response.data = {
                'message': 'register succesfully'
            }
        except Exception  as e:
            print(e.msg)
            response.data = {
                'message': e.msg
            }
        return response

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        """token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')"""
        token, created=  Token.objects.get_or_create(user=user)
        response = Response()

        """response.set_cookie(key='Token', value=token, httponly=True)"""
        response.data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'roles': ['ROLE_ADMIN','ROLE_USER'],
            'accessToken': token.key,
        }
        return response
        

        
        