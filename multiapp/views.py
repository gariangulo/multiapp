from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .models import Curso, TipoCurso, Comentario
from django.utils import timezone
from .forms import CursosForm

# Librerias de terceros
import requests
from dal import autocomplete

# Librerias en carpetas locales
from cuenta.models import Persona

class ComentariosView(TemplateView):
    template_name = 'comentarios/comentarios.html'
    extra_context = {'titulo':'Comentarios Pages'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['porcentaje'] = int(self.kwargs['porcentaje'])
        context['fecha'] = timezone.now()
        return context

class Cursosview(TemplateView):
    template_name ='comentarios/cursos.html'
    extra_context = {'titulo': 'Cursos Cupos','fecha':timezone.now()}

class CursosList(ListView):
    queryset = Curso.objects.all()
    template_name = 'comentarios/cursos.html'
    context_object_name = 'cursos'
    extra_context = {'titulo':'Cursos List','fecha':timezone.now()}

class ComentariosList(ListView):
    queryset = Comentario.objects.all()
    template_name = 'comentarios/comentarios.html'
    context_object_name = 'comentarios'
    extra_context = {'titulo':'Comentarios List','fecha':timezone.now()}


class CuposList(ListView):
    queryset = Curso.objects.all()
    template_name = 'comentarios/cupos.html'
    context_object_name = 'cursos'
    extra_context = {'titulo':'Cupos List','fecha':timezone.now()}


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cupos_cursos = []
        for i in self.queryset:
            porcentaje = ((i.cupos_restantes * 100)/i.total_cupos)
            print(int(porcentaje))

        context['porcentaje'] = porcentaje
        
        return context


class CursosCrear(CreateView):
    model = Curso
    template_name = 'comentarios/crearcurso.html'
    form_class = CursosForm
    success_url = reverse_lazy('multiapps:cursoslist')
    extra_context = {'titulo':'Crear curso','fecha':timezone.now()}

# class CursoAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):

#         qs = TipoCurso.objects.all()

#         if self.q:
#             qs = qs.filter(tipo_curso__icontains=self.q)
            
#         return qs