from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import uuid 
from django.views.generic import ListView, DetailView, CreateView
from .utils import DataMixin
from .models import Documents, Category
from .forms import AddPostForm, AddCategory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import DeleteView

class MainPage(LoginRequiredMixin, DataMixin, ListView):
    model = Documents
    paginate_by = 2
    template_name = 'home.html'
    context_object_name = 'documents'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = self.request.GET.get('cat')
        c_def = self.get_context_user(cat)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        cat = self.request.GET.get('cat')
        if not cat:
            return Documents.objects.filter(user=self.request.user).select_related('category').order_by('-time_create')
        return Documents.objects.filter(user=self.request.user, category__slug=cat)

class DetailDocument(DetailView):
    model = Documents
    template_name = 'document/document_detail.html'
    context_object_name = 'doc'
    slug_url_kwarg = 'document_slug' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object and self.object.category:
            context['cat_selected'] = self.object.category.slug
        else:
            context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Documents.objects.filter(user=self.request.user)

class AddDocument(CreateView):
    form_class = AddPostForm
    template_name = 'document/addpage.html'
    success_url = 'home'
    
    def get_form_kwargs(self):
        malumot = super().get_form_kwargs()
        malumot['user'] = self.request.user
        return malumot
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.cleaned_data['name'])
        return super().form_valid(form)
    
class AddCategoryView(CreateView):
    template_name = 'document/addcat.html'
    form_class = AddCategory
    success_url = 'home'
    
    def get_form_kwargs(self):
        malumot = super().get_form_kwargs()
        malumot['user'] = self.request.user
        return malumot
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.cleaned_data['name'])
        return super().form_valid(form)

class DeleteDocumentView(DeleteView):
    model = Documents
    success_url = 'home'
    slug_url_kwarg = 'document_slug'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)