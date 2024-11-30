from django.shortcuts import render, redirect, get_object_or_404
from .models import PostBlog, Projects, Category, Achievements, Cv, Image, Comment
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import ContectForm
# Create your views here.


# function to go to home page
def home(request):
    return render(request, 'website/home.html')

# to view the list of blogs
def post_list(request):
    blogs = PostBlog.objects.all()
    return render(request, 'website/blog_posts.html', {'blogs':blogs})

#to viev secifice blog and if user is loged in can comment
def blog_details(request, pk):
    post = get_object_or_404(PostBlog, pk=pk)
    comments = post.comments.all() 
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_details', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'website/blog_details.html', {'post':post, 'comments':comments, 'form':form})
# to view acjievments 
def achievments(request):
    achievments  = Achievements.objects.all()
    return render(request, 'website/achievments.html', {'achievments':achievments})
# view project totrials
def projects(request):
    projects = Projects.objects.all()
    return render(request, 'website/projects.html', {'projects':projects})
# view a spcifec project
def project_details(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == "POST":
        return redirect('project_details', pk=project.pk)
    else:
        return render(request, 'website/project_details.html', {'project':project})
# function to view contact page
def contect(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            # Send an email
            def send_email(name, email, message):
                send_mail(name, message, 'jake1521996@gmail.com', [email], fail_silently=False,
                          )   
            #send_email(name, email, message)
            form.save()
            return redirect('contect')
    else:
        form = ContectForm
    return render(request, 'website/contact.html', {'form':form})    

# view galery
def gallery(request):
    images = Image.objects.all()
    return render(request, 'website/gallery.html', {'images': images})

def cv(request, image_id):
    image = get_object_or_404(Cv, pk=image_id)
    with open(image.image.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')  # Adjust content_type as needed
        response['Content-Disposition'] = 'attachment; filename="%s"' % image.image.name
        return response

# User Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Error during registration. Please try again.')
    else:
        form = RegisterForm()
    return render(request, 'website/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog')  # Redirect to post list page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AuthenticationForm()
    return render(request, 'website/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')