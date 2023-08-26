from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    slug = models.SlugField(unique=True, db_index=True)
    # Add more attributes as needed
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more attributes as needed

class Parent(models.Model):
    name = models.CharField(max_length=100)
    # Add more attributes as needed

class Question(models.Model):
    text = models.TextField()

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    questions = models.ManyToManyField('Question')
    participants = models.ManyToManyField(Student, through='Participation')
