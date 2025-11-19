from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.ServiceListView.as_view()),
    path('<int:pk>/', views.ServiceDetailView.as_view()),
]