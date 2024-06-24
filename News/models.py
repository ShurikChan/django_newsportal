from django.db import models
from django.contrib.auth.models import User
from News.config import PUBLICATIONS
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.user}' 

    def update_rating(self):
        posts_rating = 0
        comments_rating = 0
        posts_comments_rating = 0
        posts = Post.objects.filter(author = self)
        for p in posts:
            posts_rating += p.rating
        comments = Comment.objects.filter(user = self.user)
        for c in comments:
            comments_rating += c.rating
        posts_comments = Comment.objects.filter(post__author=self)
        for pc in posts_comments:
            posts_comments_rating += pc.rating

        self.rating = posts.rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(unique = True,max_length = 50)
    subscribers = models.ManyToManyField(User, through = 'CategorySubs', related_name='subs')

    def __str__(self):
        return f'{self.name}' 


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    news_type = models.CharField(max_length = 2,
                                 choices = PUBLICATIONS,
                                 default = 'publication')
    time_in = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory', related_name='posts')
    heading = models.CharField(max_length = 100)
    text = models.CharField(max_length = 255)
    like_rating = models.IntegerField(default = 0)
    dislike_rating = models.IntegerField(default = 0)


        
    def get_absolute_url(self):
        return f'/post/{self.id}'
    

# p1.set(category = 'Sports')
    def like(self):
        self.like_rating += 1
        self.save()
        
    
    def dislike(self):
        self.dislike_rating += 1
        self.save()

    
    def preview(self):
            if len(self.text) < 125:
                return self.text
            else:
                return self.text[:125] + '...'
            
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class CategorySubs(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 255)
    time_in = models.DateTimeField(auto_now_add = True)
    com_like_rating = models.IntegerField(default = 0)
    com_dislike_rating = models.IntegerField(default = 0)


    def like(self):
        self.com_like_rating += 1
        self.save()
        
    
    def dislike(self):
        self.com_dislike_rating += 1
        self.save()




