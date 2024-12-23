from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import RegisterForm,MusicianForm
from . import models
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = RegisterForm()
    
    return render(request, 'signup.html', {'form':form})

class UserLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)
    

@login_required
def Profile(request):
    return render(request,'profile.html')


@method_decorator(login_required,name='dispatch')
class AddMusician(CreateView):
    model = models.MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self,form):
        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class EditMusician(UpdateView):
    model = models.MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


class DeleteMusician(DeleteView):
    model = models.MusicianModel
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
    


def UserLogout(request):
    logout(request)
    return redirect('signup')