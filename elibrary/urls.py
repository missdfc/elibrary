from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view()),
    path('bookdetail/<int:pk>/', BookDetail.as_view()),
]