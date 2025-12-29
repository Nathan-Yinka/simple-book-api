from django.urls import path
from .views import BookCreateView, UserCreateView, BorrowBookView, UserBorrowedBooksView

urlpatterns = [
    path('books', BookCreateView.as_view(), name='create-book'),
    path('users', UserCreateView.as_view(), name='create-user'),
    path('borrow', BorrowBookView.as_view(), name='borrow-book'),
    path('users/<int:user_id>/borrowed-books', UserBorrowedBooksView.as_view(), name='user-borrowed-books'),
]