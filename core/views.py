from django.shortcuts import render, redirect
from .models import Gato, Perro
from .form import GatoForm, PerroForm

def index (request):
    comentario ={"titulo":"COMENTARIO ENVIADO DESDE DJANGO A LA PAGINA"}
    return render(request, "core/index.html", comentario)

def nosotros (request):
    return render(request, "core/nosotros.html")

def perros (request):
    perros = Perro.objects.all()
    return render(request, "core/perros.html", {"perros":perros})

def gatos (request):
    gatos = Gato.objects.all()
    return render(request, "core/gatos.html",{"gatos":gatos})     

class Perros:
    def __init__(self, nombre, raza):
        self.nombre= nombre
        self.raza = raza
        super().__init__

def contactanos (request):
    lista=["Santiago","Valparaiso","Quilpue","Concon","Reñaca","Viña del Mar"]
    perro = Perros("Kira", "Dalmata")
    variables = {"ciudad":lista, "perro": perro}
    return render(request, "core/contactanos.html", variables)   

def login(request):
    return render(request,"core/admin/login.html")

def indexadmin(request):
    gato = Gato.objects.all()
    perro = Perro.objects.all()
    conext ={"gato":gato, "perro":perro}
    return render(request,"core/admin/indexadmin.html", conext)

def save_gato(request):
    form=GatoForm
    mensaje = ""

    if request.method == 'POST':
        form = GatoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = request.POST.get('nombre', None)
            if nombre in Gato.objects.values_list('nombre', flat=True):
                mensaje = "Este gato ya existe en la base de datos, intente con otro."
            else:
                form.save()
                mensaje = "Datos guardados con éxito."
    return render(request,"core/admin/save_gato.html",{"mensaje": mensaje,"form":form})

def form_modgato(request, id):
    gato=Gato.objects.get(nombre=id)
    mensaje = ""
    if request.method == 'POST':
        form = GatoForm(request.POST, request.FILES, instance=gato)
        if form.is_valid():
            form.save()
            mensaje = "Datos modificados con éxito"
            return redirect(to="indexadmin")
    return render(request, "core/admin/form_modgato.html",{"form":GatoForm(instance=gato), "mensaje":mensaje})

def delete_gato(request, id):
    gato = Gato.objects.get(nombre=id)
    gato.delete()
    return redirect(to="indexadmin")

def save_perro(request):
    form=PerroForm
    mensaje = ""

    if request.method == 'POST':
        form = PerroForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = request.POST.get('nombre', None)
            if nombre in Perro.objects.values_list('nombre', flat=True):
                mensaje = "Este perro ya existe en la base de datos, intente con otro."
            else:
                form.save()
                mensaje = "Datos guardados con éxito."
    return render(request,"core/admin/save_perro.html",{"mensaje": mensaje,"form":form})

def form_modperro(request, id):
    perro=Perro.objects.get(nombre=id)
    mensaje = ""
    if request.method == 'POST':
        form = PerroForm(request.POST, request.FILES, instance=perro)
        if form.is_valid():
            form.save()
            mensaje = "Datos modificados con éxito"
            return redirect(to="indexadmin")
    return render(request, "core/admin/form_modperro.html",{"form":PerroForm(instance=perro), "mensaje":mensaje})

def delete_perro(request, id):
    perro = Perro.objects.get(nombre=id)
    perro.delete()
    return redirect(to="indexadmin")