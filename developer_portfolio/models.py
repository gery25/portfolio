from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)

class Skill(models.Model):
    class Category(models.TextChoices):
        FRONTEND = 'Frontend', 'Frontend'
        BACKEND = 'Backend', 'Backend'
        DATABASE = 'Database', 'Database'
        DEVOPS = 'DevOps', 'DevOps'
        OTHER = 'Other', 'Other'
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    icon = models.ImageField(upload_to='developer_portfolio/static/developer_portfolio/image/icons/')