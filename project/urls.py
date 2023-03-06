from django.urls import path

from .views import ProjectDetailAPIView, ProjectListAPIView

urlpatterns = [
    path('list/', ProjectListAPIView.as_view()),
    path('list/<int:pk>/', ProjectDetailAPIView.as_view()),
]