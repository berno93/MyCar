from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

# Permet de récupérer tous les données de notre models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Importation de notre models
from django.apps import apps
CarPost = apps.get_model(app_label='MyCar', model_name='CarPost')

# Récupère automatiquement tous les voitures que l'on a crée
class MyCarHome(ListView):
    model = CarPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        
        return queryset.filter(published=True)
    
    
class MyCarCreate(CreateView):
    model = CarPost
    template_name = "MyCar/carpost_create.html"
    fields = ['title', 'photo','price','content', 'created_on', 'published', 'slug', 'author']
    
class MyCarUpdate(UpdateView):
    model = CarPost
    template_name = "MyCar/carpost_edit.html"
    fields = ['title', 'photo','price','content', 'published']
    
class MyCarDetail(DetailView):
    model = CarPost
    context_object_name = "post"
    
class MyCarDelete(DeleteView):
    model = CarPost
    success_url = reverse_lazy("posts:home")
    context_object_name = "post"