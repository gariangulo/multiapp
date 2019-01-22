# Librerias Django

from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from multiapp.views import ComentariosView, Cursosview, CuposList, CursosList, ComentariosList, CursosCrear
# Librerias en carpetas locales

app_name = 'multiapp'

urlpatterns = [
   path('cupos/', CuposList.as_view(),name='cupos'),
#    path('cursos/', Cursosview.as_view(),name='cursos'),
   path('cursoslist/', CursosList.as_view(),name='cursoslist'),
   path('comentarios/', ComentariosList.as_view(),name='comentarioslist'),
   # path('tipo-de-curso/', CursoAutocomplete.as_view(), name='tipo_de_curso'),
   path('crearcurso/', CursosCrear.as_view(), name='crearcurso'),
]
