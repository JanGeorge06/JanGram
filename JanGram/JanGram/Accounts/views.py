from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from blog import views

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect(views.feed)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(user.get_username())
            print("User authenticated!")
            return redirect(views.feed)
        else:
            print("User unauthenticated")
            return render(request,'home.html',{"message":"Invalid credentials"})


def register(request):
    if request.user.is_authenticated:
        return redirect(views.feed)
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(views.feed)
    else:
        form = RegistrationForm()

    return render(request,'register.html',{'form':form})
        



