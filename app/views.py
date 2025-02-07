from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def salir(request):
    logout(request)
    return redirect('login')

def inicio(request):
    mensaje_error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print(username)

        if user is not None and username == "tienda01": #Nombre del dueño de la tienda
            login(request, user)
            return redirect('d_welcome', user_id=user.id)  # Redirige al ID del usuario
        if user is not None and username != "tienda01": 
            login(request, user)
            return redirect('e_welcome', user_id=user.id) 
        else:
            mensaje_error = "Nombre de usuario o contraseña incorrectos."
    return render(request, 'login/login.html', {'mensaje_error': mensaje_error})



@login_required
def d_welcome(request, user_id):
    return render(request, 'duenio/d_welcome.html')

@login_required
def e_welcome(request, user_id):
    return render(request, 'empleado/e_welcome.html')

 