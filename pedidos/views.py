from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings
from tienda.forms import FormContact


# Create your views here.
#V21
def search_product(request):
    return render(request,"search.html")

#V22 - Formularios II
def search(request):
    #message="Articulo buscado: %r" %request.GET["searching"]
    product=request.GET["searching"]

    #V23 evaluar la cantidad de texto
    if len(product) > 20:
        message="Termino de busqueda demasiado largo!"
    else:
        articulos=Articulo.objects.filter(name__icontains=product)
        return render(request, "result.html",{"articulos":articulos,"query":product})
    return render(request,"search.html",{"message":message})

def contact(request):
    if request.method=="POST":
        subject=request.POST["subject"]
        message=request.POST["message"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["carlos.sosa.c0d3@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"thanks.html")
    return render(request,"contact_us.html")

def contact_api(request):
    if request.method=="POST":
        miForm=FormContact(request.POST)
        if miForm.is_valid():
            infForm=miForm.cleaned_data
            send_mail(infForm['asunto'],infForm['message'],
            infForm.get('email',''),['carlos.sosa.c0d3@gmail.com'],)
            return render(request,"thanks.html")
    else:
        miForm=FormContact()
    return render(request,"contact_formapi.html",{"form":miForm})