from django.db import models


class University(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name


class Subject(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    subject = models.CharField(max_length=256)

    def __str__(self):
        return f"The {self.university} has next subjects: {self.subject}"
