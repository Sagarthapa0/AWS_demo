from django.urls import path
from .views import UserListView,UpdateAPIView,UserCreateView,UserUpdateView,UserDeleteView,UserRetrieveView,LoginView,LogoutView

urlpatterns=[
    path("",UserListView.as_view(),name="user-list"),
    path("create/",UserCreateView.as_view(),name="user-create"),
    path("update/<int:pk>/",UserUpdateView.as_view(),name="user-update"),
    path("delete/<int:pk>/",UserDeleteView.as_view(),name="user-delete"),
    path("retrieve/<int:pk>/",UserRetrieveView.as_view(),name="user-retrieve"),

    path("login/",LoginView.as_view(),name="user-login"),
    path("logout/",LogoutView.as_view(),name="user-logout"),
    
]