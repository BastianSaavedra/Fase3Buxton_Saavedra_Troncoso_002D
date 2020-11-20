from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DeleteView
# Create your views here.


def registro(request):
   data = {
      'form': CustomUserCreationForm()
   }
   if request.method == 'POST':
      formulario = CustomUserCreationForm(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         user = authenticate(username=formulario.cleaned_data["username"],
                              password=formulario.cleaned_data["password1"])
         login(request, user)
         messages.success(request, "Su cuenta a sido creada exitosamente!")
         return redirect(to="index")
      data["form"] = formulario
   return render(request, 'registration/registro.html', data)

def nuevo_usuario(request):
   data = {
      'usuform': CustomUserCreationForm()
   }
   if request.method == 'POST':
      formulario = CustomUserCreationForm(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         user = authenticate(username=formulario.cleaned_data["username"],
                              password=formulario.cleaned_data["password1"])

         login(request, user)
         messages.success(request, "Su cuenta a sido creada exitosamente!")
         return redirect(to="index")
      data["usuform"] = formulario
   return render(request, 'Usuarios/nuevo_usuario.html', data)

class UserListView(ListView):
   model = User
   template_name = 'Usuarios/user_list.html'

class UserDeleteView(DeleteView):
   model = User
   success_url = reverse_lazy('usuario')
   template_name = 'Usuarios/usuario_confirm_delete.html'