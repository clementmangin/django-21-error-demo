from django.db import models


class Parent(models.Model):

    name = models.CharField(max_length=20)


class Child(models.Model):

    parent = models.ForeignKey(Parent, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=20)
