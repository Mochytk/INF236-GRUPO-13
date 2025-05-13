from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer



from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Usuario

class LoginAPIView(APIView):
    def post(self, request):
        correo = request.data.get('correo')
        contraseña = request.data.get('contraseña')

        try:
            usuario = Usuario.objects.get(email=correo)
        except Usuario.DoesNotExist:
            return Response({'error': 'Correo o contraseña inválidos'}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=usuario.username, password=contraseña)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'rol': user.rol,
                'username': user.username,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Correo o contraseña inválidos'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)