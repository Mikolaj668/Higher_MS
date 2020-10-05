from django.db import models


# Create your models here.

class Candidate(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Recruiter(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Task(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.title}'


# on_delete=models.PROTECT in task and recruiter in order to keep track of all tasks and recruiters that took part in a process
class Grade(models.Model):
    value = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.PROTECT)
