from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path(
        'students/',
        views.StudentListView.as_view(),
        name='student_list'
    ),
    path(
        'students/<pk>/',
        views.StudentDetailView.as_view(),
        name='student_detail'
    ),
]
