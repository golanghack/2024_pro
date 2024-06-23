from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import modelform_factory
from django.apps import apps
from django.db.models import Count
from django.core.cache import cache
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from students.forms import MatrixConnectionForm
from matrix.forms import BlockFormSet
from matrix.models import Matrix
from matrix.models import Block, Content
from matrix.models import Subject


class ManageMatrixListView(ListView):
    model = Matrix
    template_name = 'matrix/manage/matrix/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerMatrixMixin(OwnerMixin,
                       LoginRequiredMixin,
                       PermissionRequiredMixin):
    model = Matrix
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_matrix_list')


class OwnerMatrixEditMixin(OwnerMatrixMixin, OwnerEditMixin):
    template_name = 'matrix/manage/matrix/form.html'


class ManageMatrixListView(OwnerMatrixMixin, ListView):
    template_name = 'matrix/manage/matrix/list.html'
    permission_required = 'matrix.view_matrix'


class MatrixCreateView(OwnerMatrixEditMixin, CreateView):
    permission_required = 'matrix.add_matrix'


class MatrixUpdateView(OwnerMatrixEditMixin, UpdateView):
    permission_required = 'matrix.change_matrix'


class MatrixDeleteView(OwnerMatrixMixin, DeleteView):
    template_name = 'matrix/manage/matrix/delete.html'
    permission_required = 'matrix.delete_matrix'


class MatrixBlockUpdateView(TemplateResponseMixin, View):
    template_name = 'matrix/manage/block/formset.html'
    course = None

    def get_formset(self, data=None):
        return BlockFormSet(instance=self.course,
                             data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Matrix,
                                        id=pk,
                                        owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'matrix': self.course,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_matrix_list')
        return self.render_to_response({'matrix': self.course,
                                        'formset': formset})


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'matrix/manage/matrix/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='matrix',
                                  model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'order',
                                                 'created',
                                                 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(Block,
                                       id=module_id,
                                       course__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner=request.user)
        return super().dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance=self.obj,
                             data=request.POST,
                             files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
               
                Content.objects.create(module=self.module,
                                       item=obj)
            return redirect('block_content_list', self.module.id)
        return self.render_to_response({'form': form,
                                        'object': self.obj})


class ContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(Content,
                               id=id,
                               module__course__owner=request.user)
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('block_content_list', module.id)


class BlockContentListView(TemplateResponseMixin, View):
    template_name = 'matrix/manage/block/content_list.html'

    def get(self, request, module_id):
        module = get_object_or_404(Block,
                                   id=module_id,
                                   course__owner=request.user)
        return self.render_to_response({'block': module})


class BlockOrderView(CsrfExemptMixin,
                      JsonRequestResponseMixin,
                      View):
    def post(self, request):
        for id, order in self.request_json.items():
            Block.objects.filter(id=id,
                   matrix__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})


class ContentOrderView(CsrfExemptMixin,
                       JsonRequestResponseMixin,
                       View):
    def post(self, request):
        for id, order in self.request_json.items():
            Content.objects.filter(id=id,
                       block__matrix__owner=request.user) \
                       .update(order=order)
        return self.render_json_response({'saved': 'OK'})


class MatrixListView(TemplateResponseMixin, View):
    model = Matrix
    template_name = 'matrix/matrix/list.html'
    def get(self, request, subject=None):
        subjects = cache.get('all_subjects')
        if not subjects:
            subjects = Subject.objects.annotate(
                            total_courses=Count('matrix'))
            cache.set('all_subjects', subjects)
        all_matrixes = Matrix.objects.annotate(
                        total_modules=Count('block'))
        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            key = f'subject_{subject.id}_matrix'
            matrixes = cache.get(key)
            if not matrixes:
                matrixes = all_matrixes.filter(subject=subject)
                cache.set(key, matrixes)
        else:
            matrixes = cache.get('all_matrix')
            if not matrixes:
                matrixes = all_matrixes
                cache.set('all_matrixes', matrixes)
        return self.render_to_response({'subjects': subjects,
                                        'subject': subject,
                                        'matrixes': matrixes})


class MatrixDetailView(DetailView):
    model = Matrix
    template_name = 'matrix/matrix/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matrix_connection_form'] = MatrixConnectionForm(
                                   initial={'matrix':self.object})
        return context
