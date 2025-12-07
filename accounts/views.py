from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from . serializers import UserSerializer, LoginSerializer, EmptySerializer

class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'message': 'User registered successfully.'},
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                            'refresh': str(refresh),
                             'access': str('refresk.access_token'),
                             'email': user.username},
                             status=status.HTTP_200_OK)
        
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(generics.GenericAPIView):
    serializer_class = EmptySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if hasattr(request, 'access_token'): 
            request.user.access_token.delete()
        
            
        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
        



        
