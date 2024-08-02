from django.shortcuts import render # Remove this line when using shortcut
from django.http import Http404 # Remove this line when using shortcut
from django.shortcuts import get_object_or_404, render
from .models import Student


# Display a list of all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/templates/list.html',{'students':students})


'''
# Display a single Student
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404("Student with the specified ID was not found!")
    return render(
        request,
        'students/templates/student/detail.html',
        {'student': student}
    )

'''

# Display a single Student with Shortcut 404 Error
def student_detail(request, id):
   student = get_object_or_404(Student,id=id)
   return render(
        request,
        'students/templates/student/detail.html',
        {'student': student}
    )


