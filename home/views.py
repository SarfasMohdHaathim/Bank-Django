from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm
from .models import *
from django.contrib import messages
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
            try:
                Profile.objects.get(user=user)
                return redirect('home')
            except:
                return redirect('profile')
        else:
            print('invalid Credential')

    return render(request,'login.html')



def profile(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        date=request.POST['date']
        age=request.POST['age']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        gender=request.POST['gender']
        acctype=request.POST['acctype']
        district=request.POST['district']
        dc=request.POST.get('dc',False)
        cc=request.POST.get('cc',False)
        ps=request.POST.get('ps',False)
        if dc:
            dc=True
        if cc:
            cc=True
        if ps:
            ps=True
        print(dc,gender)
        Profile.objects.create(user=request.user
        ,name=fullname
        ,dob=date,
        age=age,phone=phone,email=email,address=address,district=district,gender=gender
        ,account_type=acctype,creditcard=cc,passbook=ps).save()
        messages.success(request, 'Form submission successful')


    return render(request,'createprofile.html')