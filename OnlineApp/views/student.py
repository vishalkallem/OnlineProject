from django.views.generic import CreateView, UpdateView, DeleteView
from OnlineApp.forms.student import *
from OnlineApp.forms.mocktest1 import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class CreateStudentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'OnlineApp:login'
    permission_required = 'OnlineApp.add_student'
    permission_denied_message = "User does not have permission to add student"
    model = Student
    form_class = StudentForm
    template_name = 'OnlineApp/add_student.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        test_form = MockTestForm()
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
            'title': 'Add Student',
         })
        return context

    def post(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student_form = StudentForm(request.POST)
        test_form = MockTestForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()

        return redirect('OnlineApp:college_details', pk=college.id)


class UpdateStudentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'OnlineApp:login'
    permission_required = "OnlineApp.change_student"
    permission_denied_message = "User does not have permission to update student"
    model = Student
    form_class = UpdateStudentForm
    template_name = 'OnlineApp/edit_student.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form = UpdateMockTestForm(instance=student_form.mocktest1)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
            'title': 'Edit Student',
        })

        return context

    def post(self, request, *args, **kwargs):

        student_data = Student.objects.get(pk=kwargs.get('pk'))
        student_form = UpdateStudentForm(request.POST, instance=student_data)
        test_form = UpdateMockTestForm(request.POST, instance=student_data.mocktest1)

        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())

        student_form.save()
        test_form.save()

        return redirect("OnlineApp:college_details", self.kwargs.get('college_id'))


class DeleteStudentView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'OnlineApp:login'
    permission_required = 'OnlineApp.delete_student'
    permission_denied_message = 'User does not have permission to delete student'
    model = Student
    template_name = 'OnlineApp/confirm_delete.html'

    def get_success_url(self):
        return redirect('OnlineApp:college_details', **{'pk': self.kwargs.get('college_id')}).url
