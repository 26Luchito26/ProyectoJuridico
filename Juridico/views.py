from django.shortcuts import render, HttpResponse
from datetime import datetime

# Vistas de mi App Principal

def inicio(request):
    return render(request, "Juridico/inicio.html")

def servicios(request):
    return render(request, "Juridico/servicios.html")

def blog(request):
    return render(request, "Juridico/blog.html")

def contacto(request):
    return render(request, "Juridico/contacto.html")

"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
#Imprime un mensaje cualquiera en pantalla

def m_pantalla(request):
    mensaje_texto = "Esto imprime un mensaje cualquera en pantalla"
    mensaje_acceso = "Acceder al panel admin de Django => usuario: luchito, contraseña:000000ñ"
    nombre = "Luis"
    apellido = "Huanel"
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    context = {
        "nombre_persona": nombre,
        "apellido_persona": apellido,
        "fecha_actual": fecha_actual,
        "mensaje_T":mensaje_texto,
        "mensaje_A":mensaje_acceso,
    }

    return render(request, "Juridico/m_pantalla.html", context)