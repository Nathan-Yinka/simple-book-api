from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


books = {}
users = {}
borrowed_books = {}


book_id_counter = 1
user_id_counter = 1



class BookCreateView(APIView):
    """
    Create a new book in the library.
    
    Accepts title and author, returns the created book with a unique ID.
    """
    def post(self, request):
        """
        Create a new book.
        
        Args:
            request: Request object containing 'title' and 'author' in the body
            
        Returns:
            Created book object with status 201, or error message with status 400
        """
        global book_id_counter 

        title = request.data.get('title')
        author = request.data.get('author') 
        
        if not title or not author:
            return Response({"error": "Title and author are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        book = {
            "id": book_id_counter,
            "title": title,
            "author": author,
            "is_borrowed": False
        }

        books[book_id_counter] = book
        book_id_counter += 1

        return Response(book, status=status.HTTP_201_CREATED)
    
class UserCreateView(APIView):
    """
    Create a new user in the system.
    
    Accepts a name, returns the created user with a unique ID.
    """
    def post(self, request):
        """
        Create a new user.
        
        Args:
            request: Request object containing 'name' in the body
            
        Returns:
            Created user object with status 201, or error message with status 400
        """
        global user_id_counter 

        name = request.data.get('name')
        
        if not name:
            return Response({"error": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = {
            "id": user_id_counter,
            "name": name
        }

        users[user_id_counter] = user
        user_id_counter += 1

        return Response(user, status=status.HTTP_201_CREATED)
    

class BorrowBookView(APIView):
    """
    Borrow a book from the library.
    
    Associates a book with a user and marks it as borrowed.
    """
    def post(self, request):
        """
        Borrow a book for a user.
        
        Args:
            request: Request object containing 'userId' and 'bookId' in the body
            
        Returns:
            Success message with status 200, or error message with status 400/404
        """
        user_id = request.data.get('userId')
        book_id = request.data.get('bookId')

        if not user_id or not book_id:
            return Response({"error": "userId and bookId are required."}, status=status.HTTP_400_BAD_REQUEST)

        if user_id not in users:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if book_id not in books:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        book = books[book_id]
        
        if book['is_borrowed']:
            return Response({"error": "Book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)
        
        book['is_borrowed'] = True
        borrowed_books[book_id] = user_id

        return Response({"message": f"Book '{book['title']}' borrowed by user '{users[user_id]['name']}'."}, status=status.HTTP_200_OK)
    

class UserBorrowedBooksView(APIView):
    """
    Get all books borrowed by a specific user.
    
    Returns a list of all books currently borrowed by the user.
    """
    def get(self, request, user_id):
        """
        Retrieve all books borrowed by a user.
        
        Args:
            request: Request object
            user_id: ID of the user whose borrowed books to retrieve
            
        Returns:
            List of borrowed books with status 200, or error message with status 404
        """
        if user_id not in users:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        user_borrowed_books = [books[book_id] for book_id, uid in borrowed_books.items() if uid == user_id]

        return Response(user_borrowed_books, status=status.HTTP_200_OK)