from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginUserForm

from django.contrib import messages


@login_required
def profile_view(request):
    return render(request, "account/profile.html")



def register_view(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {
        'form': form
        }
            
    return render(request, 'account/register.html', context=context)


def login_view(request):
    form = LoginUserForm() # assign the form to variable
    
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('profile')
                
    context = {'form' : form }
    
    return render(request, 'account/login.html', context=context)



def logout_view(request):
    logout(request)
    messages.success(request, "Logout success!")
    return redirect("login")


