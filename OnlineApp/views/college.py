from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from OnlineApp.forms.college import *
from OnlineApp.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404


class CollegeListView(LoginRequiredMixin, ListView):
    login_url = 'OnlineApp:login'
    model = College
    context_object_name = 'colleges_data'
    template_name = 'OnlineApp/colleges.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Colleges',
            'user_permissions': self.request.user.get_all_permissions,
        })
        return context


class CollegeDetailView(LoginRequiredMixin, DetailView):
    login_url = 'OnlineApp:login'
    model = College
    context_object_name = 'college_data'

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailView, self).get_context_data(**kwargs)
        college = context.get('college_data')
        students = list(college.student_set.order_by('-mocktest1__total'))
        context.update({
            'students': students,
            'college': college,
            'title': 'College Details',
            'user_permissions': self.request.user.get_all_permissions,
        })
        return context


class CreateCollegeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'OnlineApp:login'
    permission_required = 'OnlineApp.add_college'
    permission_denied_message = "User does not have to permission to add college."
    model = College
    form_class = AddCollege
    template_name = 'OnlineApp/add_college.html'
    success_url = reverse_lazy('OnlineApp:all_colleges')


class UpdateCollegeView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'OnlineApp:login'
    permission_required = 'OnlineApp.change_college'
    permission_denied_message = "User does not have permission to edit college."
    model = College
    form_class = UpdateCollege
    template_name = 'OnlineApp/edit_college.html'
    success_url = reverse_lazy('OnlineApp:all_colleges')

    def get_object(self, queryset=None):
        return get_object_or_404(College, **{'pk': self.kwargs.get('college_id')})

    def get_context_data(self, **kwargs):
        context = super(UpdateCollegeView, self).get_context_data(**kwargs)
        college = context.get('college')
        students = list(college.student_set.order_by('-mocktest1__total'))
        context.update({
            'students': students,
            'title': 'Edit College',
        })
        return context


class DeleteCollegeView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'OnlineApp:login'
    permission_required = 'OnlineApp.delete_college'
    permission_denied_message = "User does not have permission to delete college"
    model = College
    template_name = 'OnlineApp/confirm_delete.html'
    success_url = reverse_lazy('OnlineApp:all_colleges')

    def get_object(self, queryset=None):
        return get_object_or_404(College, **{'pk': self.kwargs.get('college_id')})


class CollegeView(LoginRequiredMixin, View):
    login_url = 'OnlineApp:login'

    def get(self, request):
        colleges_list = College.objects.all()
        return render(request=request, template_name='OnlineApp/colleges.html',
                      context={'colleges_data': colleges_list, 'title': 'Colleges'})
