from django.db import models

class About(models.Model):
    content = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return str(self.content)

class Intro(models.Model):
    content = models.TextField(max_length=1000, null=True)
    image = models.ImageField(null=True)

class Contact(models.Model):
    content = models.TextField(max_length=1000, null=True)
    image = models.ImageField(null=True)

class Work(models.Model):
    content = models.TextField(max_length=1000, null=True)
    image = models.ImageField(null=True)

class Enter(models.Model):
    title = models.TextField(max_length=50, null=True)
    content = models.TextField(max_length=500, null=True)
    content_two = models.TextField(max_length=500, null=True)
