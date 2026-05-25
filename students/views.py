from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment
from datetime import datetime

# 1. Просмотр списка студентов и их курсов
def student_list(request):
    # prefetch_related оптимизирует SQL-запросы (решает проблему N+1)
    students = Student.objects.prefetch_related('enrollments__course').all()
    courses = Course.objects.all()
    return render(request, "students.html", {"students": students, "courses": courses})

# 2. Добавление студента
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        birth_date = request.POST.get("birth_date")
        
        if name and email and birth_date:
            Student.objects.create(name=name, email=email, birth_date=birth_date)
    return redirect("student_list")

# 3. Добавление курса
def add_course(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        if title and description:
            Course.objects.create(title=title, description=description)
    return redirect("student_list")

# 4. Запись студента на курс
def enroll_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        course_id = request.POST.get("course_id")
        
        if student_id and course_id:
            student = get_object_or_404(Student, id=student_id)
            course = get_object_or_404(Course, id=course_id)
            # get_or_create защитит от дубликатов, если уникальность не сработала в БД
            Enrollment.objects.get_or_create(student=student, course=course)
    return redirect("student_list")

# 5. Удаление студента (Каскадное удаление)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect("student_list")