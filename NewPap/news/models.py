from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRunk = models.IntegerField(default=0)


class Category(models.Model):
    nameCategory = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    # варианты типов + кортеж
    news = 'NW'
    artical = 'AR'
    types = [
        (news, 'Новость'),
        (artical, 'Статья')
    ]
    # связь «один ко многим» с моделью Author;
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(max_length=2, choices=types, default=news)
    postCraTime = models.DateTimeField(auto_now_add=True)
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    postCtg = models.ManyToManyField(Category, through='PostCategory')
    postTitle = models.CharField(max_length=50)
    postText = models.TextField()
    postRunk = models.IntegerField(default=0)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commText = models.TextField(max_length=2000)
    commCreaTime = models.DateTimeField(auto_now_add=True)
    commRunk = models.IntegerField(default=0)

