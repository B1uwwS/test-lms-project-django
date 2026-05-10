from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)


class Article(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)


class Review(models.Model):
    class Grade(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    author = models.CharField(max_length=50)
    grade = models.IntegerField(choices=Grade)

class Comment():
    pass

class Sharing():
    pass


class BreakingNews(models.Model):
    news = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/')
    approve = models.BooleanField()
    author_email = models.EmailField()















