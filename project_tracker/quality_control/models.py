from django.db import models
from django.contrib.auth.models import User
from tasks.models import Project, Task
# Create your models here.
class Bug_Report(models.Model):
    STATUS_CHOICES = [
        ("New", "Новый"),
        ("In_progress", "В работе"),
        ("Completed", "Завершен"),
    ]
    PRIORITY_CHOICES = [
        ("1","низкий"),
        ("2","ниже среднего"),
        ("3","средний"),
        ("4","выше среднего"),
        ("5","высокий"),
    ]
    task = models.ForeignKey(
        Task,

        on_delete= models.SET_NULL,
        null = True,
        blank = True,
    )
    project = models.ForeignKey(
        Project,

        on_delete=models.CASCADE
    )
    title = models.CharField(max_length= 100)
    description = models.TextField()
    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default= "New",
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default= "3",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(
        User,

        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.title
class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ("review", "рассмотрение"),
        ("accepted", "принято"),
        ("rejected", "отклонено"),
    ]
    PRIORITY_CHOICES = [
        ("1", "низкий"),
        ("2", "ниже среднего"),
        ("3", "средний"),
        ("4", "выше среднего"),
        ("5", "высокий"),
    ]
    task = models.ForeignKey(
        Task,

        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    project = models.ForeignKey(
        Project,

        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default="New",
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="3",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(
        User,
        related_name='FeatureRequest',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.title
