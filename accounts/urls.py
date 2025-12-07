from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('api/token', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token-verify'),
]