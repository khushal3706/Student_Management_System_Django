from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # Uses ORM internally to CREATE
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else: # GET method
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Create'})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() # Uses ORM internally to UPDATE
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else: # GET method
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Update'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete() # Uses ORM to DELETE
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    # GET method
    return render(request, 'students/student_confirm_delete.html', {'student': student})
