from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import *


def get_all_colleges_data(request):
    colleges_data = College.objects.values('name', 'acronym').order_by('name')
    context = {'colleges_data': colleges_data}
    return render(request=request, template_name='OnlineApp\colleges_data.html', context=context)


def get_all_students_data(request):
    students_data = Student.objects.values('name', 'email', 'college__acronym').order_by('name')
    context = {'students_data': students_data}
    return render(request=request, template_name='OnlineApp\students_data.html', context=context)


def get_student_data(request, student_id):
    try:
        student_data = Student.objects.values('name', 'email', 'college__acronym').get(pk=student_id)
        context = {'student_data': student_data}
        return render(request=request, template_name='OnlineApp\student_data.html', context=context)
    except Student.DoesNotExist:
        raise Http404("Student with particular id %d is not found!" % student_id)


def get_student_score(request):
    students_data = Student.objects.values('name', 'email', 'college__acronym', 'mocktest1__total')
    context = {'students_data': students_data}
    return render(request=request, template_name='OnlineApp\students_scores_data.html', context=context)


def get_session(request):
    request.session.setdefault('counter', 0)
    call_count = request.session['counter'] + 1
    request.session['counter'] = call_count
    return HttpResponse(f"This link is clicked [{call_count}] times")
