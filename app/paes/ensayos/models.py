from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (('student', 'Estudiante'), ('teacher', 'Docente'))
    role = models.CharField(max_length=10, choices=ROLES, default='student')

class Ensayo(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pregunta(models.Model):
    exam = models.ForeignKey(Ensayo, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    correct_answer = models.CharField(max_length=1)  # Ej: 'A', 'B', etc.

class Intento(models.Model):
    student = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exam = models.ForeignKey(Ensayo, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)