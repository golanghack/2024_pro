from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from matrix.models import Matrix
from students.forms import MatrixConnectionForm


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_matrix_list')
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class StudentMatrixView(LoginRequiredMixin, FormView):
    matrix = None
    form_class = MatrixConnectionForm
    def form_valid(self, form):
        self.matrix = form.cleaned_data['matrix']
        self.matrix.students.add(self.request.user)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('student_matrix_detail',
                            args=[self.matrix.id])


class StudentMatrixListView(LoginRequiredMixin, ListView):
    model = Matrix 
    template_name = 'students/matrix/list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentMatrixDetailView(DetailView):
    model = Matrix
    template_name = 'students/matrix/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        matrix = self.get_object()
        if 'block_id' in self.kwargs:
            
            context['block'] = matrix.blocks.get(
                                    id=self.kwargs['block_id'])
        else:
            # get first module
            context['block'] = matrix.blocks.all()[0]
        return context
