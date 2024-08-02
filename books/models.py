from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from students.models import Student


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name
    
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.CharField(max_length=100)
    date_of_publish = models.DateField(max_length=100)
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return self.title


class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} borrowed {self.book}"