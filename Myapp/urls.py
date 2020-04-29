from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('books/user/<int:user>/', BookView.as_view()),
    path('books/user/<int:user>/<int:pk>', BookDetailView.as_view()),
    path('users/<int:user>/', UserView.as_view()),
    path('users/<int:user>/<int:pk>', UserDetailView.as_view()),

]