from django.contrib import admin
from .models import PostBlog, Projects, Category, Achievements, Cv, Image
# Register your models here.

# giving permistion to the super user to be abel to add and post on the site 
admin.site.register(PostBlog)
admin.site.register(Projects)
admin.site.register(Achievements)
admin.site.register(Category)
admin.site.register(Cv)
admin.site.register(Image)