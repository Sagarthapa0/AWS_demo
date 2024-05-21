from django.shortcuts import render
from .serializers import UserListSerializer,UserSerializer,LoginSerializer,LogoutSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly


# Create your views here.

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        username=serializer.validated_data.get("username")
        password=serializer.validated_data.get("password")

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"message":"Invalid credential"},status=401)
        
        if not user.check_password(password):
            return Response({"message":"Invalid credential"},status=401)
         
            #try:
         #        token = Token.objects.get(user=user)
        #    except Token.DoesNotExist:
        #        token = Token.objects.create(user=user)

            #instead of above

        token,created=Token.objects.get_or_create(user=user)

        return Response({"message":"Login SuccessFul","token":token.key})
    

class LogoutView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token_from_user=serializer.validated_data.get("token")

        try:
            token=Token.objects.get(key=token_from_user)
            token.delete()
            return Response({"message":"login successful"},status=200)
        except Token.DoesNotExist:
            return Response({"message":"Invalid token"},status=400) 


class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer

    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer

class UserDeleteView(DestroyAPIView):
    queryset=User.objects.all()

class UserRetrieveView(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer

