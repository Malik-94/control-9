from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import GalleryForm
from webapp.models import Gallery



class IndexView(ListView):
    template_name = 'galerriy/index.html'
    context_object_name = 'Gallerys'
    model = Gallery
    ordering = '-created_at'


class GalleryView(DetailView):
    template_name = 'galerriy/deteil.html'
    pk_url_kwarg = 'pk'
    model = Gallery



class GalleryCreateView(CreateView):
    template_name = 'galerriy/create.html'
    model = Gallery
    form_class = GalleryForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse('webapp:index', kwargs={'pk': self.object.pk})


class GalleryUpdateView(UpdateView):
    model = Gallery
    template_name = 'galerriy/update.html'
    fields = ['images', 'signature', 'author', 'laike']
    context_object_name = 'objects'

    def test_func(self):
        images_pk = self.kwargs.get('pk')
        images = Gallery.objects.get(pk=images_pk)
        return self.request.user == images.author or self.request.user.has_perm('webapp.')

    def get_success_url(self):
        return reverse('webapp:index')


class GalleryDeleteView(DeleteView):
    template_name = 'galerriy/delete.html'
    model = Gallery
    context_object_name = 'objects'
    success_url = reverse_lazy('webapp:index')


