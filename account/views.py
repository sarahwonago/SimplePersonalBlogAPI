from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterUserSerializer, LoginSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    """
    Endpoint for user registration.

    Methods:
        POST:

    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST request for registering a new user.
        Validates a user data and creates a new user if valid.
        """

        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            # saves the user and sends success response
            serializer.save()
            response = {
                "message":"User Created successfully"
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        # returns error if the validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    Endpoint for user login, returns JWT tokens.

    Methods:
        POST:

    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST request for user login.
        """

        serializer = LoginSerializer(data=request.data)

        username = request.data.get("username")
        password = request.data.get("password")

        if serializer.is_valid():
            # authenticates user and generates JWT tokens

            user = authenticate(username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)

                response = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }

                return Response(
                    response,
                    status=status.HTTP_200_OK
                )
            return Response({"message":"Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

