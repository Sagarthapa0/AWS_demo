from django.shortcuts import render
from .serializers import BlogSerializer,CommentSerializer,BlogWriteSerializer
from .models import Blog,Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import  GenericAPIView,ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BlogListView(ListAPIView):
    request: Request
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    authentication_classes=[TokenAuthentication]

    def get_queryset(self):  # sourcery skip: use-named-expression
        author_id=self.request.query_params.get("author_id")
        if author_id:
            return Blog.objects.filter(author__pk=author_id)
        else:
            return Blog.objects.all()



class BlogCreateView(CreateAPIView):
    serializer_class=BlogWriteSerializer

class BlogRetrieveView(RetrieveAPIView):
    queryset=Blog.objects.all()


class BlogUpdateView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogDeleteView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogLikeView(GenericAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        blog=Blog.objects.get(pk=kwargs.get('pk'))
        user=self.request.query_params.get('user')

        if blog.like.filter(pk=user.id).exists():
            blog.like.remove(user)
            return Response({"message":"Like removed successfully"})
        else:
            blog.like.add(user)
        
        return Response({"message":"Like added successfully"})

#For comments
    

class CommentListView(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class CommentCreateView(CreateAPIView):
    serializer_class=CommentSerializer

class CommentRetrieveView(RetrieveAPIView):
    queryset=Comment.objects.all()


class CommentUpdateView(UpdateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class CommentDeleteView(DestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer