from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
# models of data to save in data bass

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

class PostBlog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='postblog')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='web_images/', null=True, blank=True)


    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='project')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='web_images/', null=True, blank=True)
    url = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

class Achievements(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='web_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Cv(models.Model):
    image = models.ImageField(upload_to='web_images/', null=True, blank=True)

    def __str__(self):
        return self.image

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.email, self.name, self.message
    
class Comment(models.Model):
    post = models.ForeignKey(PostBlog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"