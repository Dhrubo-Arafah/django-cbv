from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# class IndexView(View):
# def get(self, request):
#     return HttpResponse("Hello World")
from core import models


class IndexView(TemplateView):
    template_name = 'portal/index.html'


class StudentView(ListView):
    context_object_name = 'student_list'
    model = models.Student
    template_name = 'portal/all_students.html'


class AddStudent(CreateView):
    fields = '__all__'
    model = models.Student
    template_name = 'portal/student-form.html'


class StudentDetail(DetailView):
    context_object_name = 'student'
    model = models.Student
    template_name = 'portal/student-detail.html'


class UpdateStudent(UpdateView):
    fields = '__all__'
    model = models.Student
    template_name = 'portal/student-form.html'


class DeleteStudent(DeleteView):
    context_object_name = 'student'
    fields='__all__'
    model = models.Student
    template_name = 'portal/delete-student.html'
    success_url = reverse_lazy('all_students')
