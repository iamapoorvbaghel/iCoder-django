from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    return render (request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        
        if len(name)<0 or len(email)<10 or len(phone)<9 or len(desc)<8:
            messages.error(request, "Please enter the details correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message is sent successfully")

    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPosts = allPostsTitle.union(allPostsContent)
    params = {'allPosts': allPosts, 'query': query}
    return render(request, "home/search.html", params)

def handleSignUp(request):
    if request.method == "POST":
        #Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Checks
        if len(username)>10:
            messages.error(request, "Your username must be under 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain alpha numeric characters")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "The passwords do not match")
            return redirect('home')


        #Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your iCoder account is succesfully created')
        return redirect('home')
    else:
        return HttpResponse("404-Not found")
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')

    return HttpResponse('404 - Not found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')