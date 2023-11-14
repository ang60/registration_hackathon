from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import CustomUserCreationForm
from django.views import generic


class RegistrationView(generic.TemplateView):
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with the URL you want to redirect to after registration
        return render(request, self.template_name, {'form': form})

class HomeView(generic.TemplateView):
    template_name = 'home.html'
    
    