from django.shortcuts import render,redirect
from django.http import HttpResponse
from .registro import Registrador
 



def home(request):
    return render(request,'texto.html')

def entrada(request):
    return render(request)


def registration_view(request):
    if request.method == 'POST':
        form = Registrador.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrada.html') 
    else:
        form = Registrador.RegistrationForm()
    return render(request, 'new_text.html', {'form': form})
