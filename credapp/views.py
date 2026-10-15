from django.shortcuts import render

# Create your views here 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'credapp/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department']
        )
        return redirect('student_list')

    return render(request, 'credapp/student.html')


def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.department = request.POST['department']
        student.save()
        return redirect('student_list')

    return render(request, 'credapp/student.html', {'student': student})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

    return redirect('student_list')
