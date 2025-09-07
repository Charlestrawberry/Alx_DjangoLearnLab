from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register

urlpatterns = [
    path("books/", list_books, name="list_books"),  
      # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  
    # class-based view

   # Authentication
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("views.register/", register, name="register"),
]