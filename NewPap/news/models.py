from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRunk = models.IntegerField(default=0)

    # МЕТОДЫ

    def update_rating(self):
        poRunk = self.posts.all().aggregate(postRating=Sum('postRunk'))
        p_R = 0
        p_R += poRunk.get(postRating=Sum('postRunk'))

        comRunk = self.comments.all().aggregate(commRating=Sum('commRunk'))
        c_R = 0
        c_R += comRunk.get('commRating')

        self.authorRunk = p_R * 3 + c_R


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

    # МЕТОДЫ
    def like(self):
        self.postRunk += 1
        self.save()

    def dislike(self):
        self.postRunk -= 1
        self.save()

    def preview(self):
        return self.postText[0: 124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commText = models.TextField(max_length=2000)
    commCreaTime = models.DateTimeField(auto_now_add=True)
    commRunk = models.IntegerField(default=0)

    def like(self):
        self.commRunk += 1
        self.save()

    def dislike(self):
        self.commRunk -= 1
        self.save()
