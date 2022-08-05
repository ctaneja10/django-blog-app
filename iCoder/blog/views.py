from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# To Serve HTML Templates
def index(request):
    return render(request, 'blog/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        txt = request.POST.get('txt')
        if len(name)<2 or len(email)<6 or len(number)<9:
            messages.warning(request, 'Please fill the form correctly')
        else:
            p = Contact(name=name, email=email, number=number, txt=txt)
            p.save()
            messages.success(request, 'Your details has been submitted.')
        return render(request, 'blog/contact.html')
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    all_blogs = Blog.objects.all()
    params = {'all_blogs':all_blogs}
    return render(request, 'blog/blog.html', params)

def iCoder(request):
    return render(request, 'blog/iCoder.html')

def blogpost(request, slug):
    # comments = BlogComment.objects.filter(blog=blog)
    all_blogs = Blog.objects.filter(blog_slug = slug)[0]
    params = {'all_blogs':all_blogs}
    return render(request, 'blog/blogpost.html', params)

def search(request):
    query = request.GET.get('search')
    if len(query) > 78:
        all_blogs = Blog.objects.none()
    else:
        all_title = Blog.objects.filter(blog_title__icontains=query)
        all_content = Blog.objects.filter(blog_content__icontains=query)
        all_blogs = all_title.union(all_content)
    params = {'all_blogs': all_blogs, 'query': query}
    return render(request, 'blog/search.html', params)

# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        # check for error inputs
        if pass1 != pass2:
            messages.warning(request, "Password does not match")
            return redirect('home')

        else:
            # create the user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created")

            return redirect('home')

    else:
        return HttpResponse('NOT ALLOWED')

def handleLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('loginusername')
        password = request.POST.get('loginpass')

        # now check in the database for the matching accounts
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('home')
        else:
            messages.warning(request, "Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse("404- Not found")

    return HttpResponse("login")

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('home')











