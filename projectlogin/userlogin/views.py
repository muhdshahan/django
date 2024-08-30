from django.shortcuts import render,redirect
from django.contrib.auth import authenticate  
from django.views.decorators.cache import never_cache
# Create your views here.
@never_cache
def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    return redirect(login)
    
@never_cache
def login(request):
    if 'username' in request.session:
        return redirect('home')
    if request.POST:
        username = request.POST.get('name')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username
            return redirect('home')
    return render(request,'login.html')
@never_cache
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('user')
