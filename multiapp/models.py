from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null = False, blank = False)
    total_cupos = models.SmallIntegerField()
    cupos_restantes = models.CharField(max_length=2)
    tipo_curso = models.ForeignKey('TipoCurso', 
                                blank = False, 
                                null = False, 
                                on_delete = models.PROTECT, 
                                db_column = "tipo_curso_id")
    usuario = models.ForeignKey('cuenta.Persona', 
                                blank = False, 
                                null = False, 
                                on_delete = models.PROTECT, 
                                db_column = "usuario_id")
    
    def __str__(self):
        return self.nombre_curso

    class Meta:
        db_table = 'multimedia\".\"curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-id']

class TipoCurso (models.Model):
    tipo_curso = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tipo_curso

    class Meta:
        db_table = 'multimedia\".\"tipo_curso'
        verbose_name = 'Tipo de Curso'
        verbose_name_plural = 'Tipo de Cursos'
        ordering = ['-id']


class Comentario(models.Model):
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(max_length=500)
    curso = models.ForeignKey('Curso',
                            blank = False, 
                            null = False, 
                            on_delete = models.PROTECT, 
                            db_column = "curso_id")
    
    usuario = models.ForeignKey('cuenta.Persona', 
                            blank = False, 
                            null = False, 
                            on_delete = models.PROTECT, 
                            db_column = "usuario_id")

    class Meta:
        db_table = 'multimedia\".\"comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-id']

    def __str__(self):
        return self.comentario