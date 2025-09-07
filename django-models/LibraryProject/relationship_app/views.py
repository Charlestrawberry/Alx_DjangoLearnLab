from django.shortcuts import render, redirect
from .models import Book
from .models import Library

from django.contrib.auth import login

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.detail import DetailView
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ log in the user right after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User Login (class-based view using built-in)
class LoginView(LoginView):
    template_name = "relationship_app/login.html"


# User Logout (class-based view using built-in)
class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"