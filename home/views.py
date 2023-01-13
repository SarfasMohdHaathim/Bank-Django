from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm
# Create your views here.
def home(request):
    return render(request,'index.html')




    
def signup(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('userlogin')
    return render(request,'signup.html',{'form':form})


def userlogout(request):    
    logout(request)
    return redirect('home')




def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print('user is not found')
    
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('invalid Credential')

    return render(request,'login.html')
