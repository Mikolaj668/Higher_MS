from django.db import models


# Create your models here.

class Candidate(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Recruiter(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Task(models.Model):
    title = models.CharField(max_length=128)


class Grade(models.Model):
    value = models.IntegerField()
    task = models.ForeignKey(Task)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter)
