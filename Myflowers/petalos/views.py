"""este comentario es para solucionar el missing doc string..."""
from django.shortcuts import render
# importar el sistema de autentificacion
from django.contrib.auth import authenticate, logout, login as auth_login
# importar los "decorators" que permiten evitar el ingreso a una pagina
# sin estar logeado
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Estado, Flores  # importar el modelo
# para lograr el ingreso de usuarios regsitrados al sistema, se debe
# incorporar el modelo de usuarios registrados de Django
#from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    """este comentario es para solucionar el missing doc string..."""
    return render(request, 'core/Home.html')
    # retorna la pagina renderizada


def cerrar_sesion(request):
    """este comentario es para solucionar el missing doc string..."""
    logout(request)
    return HttpResponse("<script>alert('cerrar sesion');window.location.href='/';</script>")


@login_required(login_url='/login/')
def agregar_carro(request, id):
    """este comentario es para solucionar el missing doc string..."""
    # recuperar una sesion llamada 'carrocompra' de no existir no deja nada ''
    sesion = request.session.get("carrocompra", "")
    # en la sesion 'carro' almaceno lo que trae la sesion mas el titulo de la flor
    request.session["carrocompra"] = sesion+str(id)+" "
    # recuperar el listado de flores
    flor = Flores.objects.all()
    msg = 'Agregar Flor'
    # renderizar la pagina,pasandole el listado de flores
    return render(request, 'core/Galeria.html', {'listaflor': flor, 'msg': msg})


@login_required(login_url='/login')
def carrocompra(request):
    """este comentario es para solucionar el missing doc string..."""
    lista = request.session.get("carrocompra", "")
    return render(request, "core/Carrito.html", {'lista': lista})


def login(request):
    """este comentario es para solucionar el missing doc string..."""
    return render(request, 'core/Login.html')


def login_iniciar(request):
    """este comentario es para solucionar el missing doc string..."""
    if request.POST:
        usr = request.POST.get("txtUsuario")
        pwd = request.POST.get("txtContra")
        usu = authenticate(request, username=usr, password=pwd)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request, 'core/Home.html')
    return render(request, 'core/Login.html')


@login_required(login_url='/login/')
def eliminar_flor(request, id):
    """este comentario es para solucionar el missing doc string..."""
    mensaje = ''
    flore = Flores.objects.get(name=id)
    try:
        flore.delete()
        mensaje = 'elimino flor del catalogo'
    except:
        mensaje = 'no se puede eliminar flor del catalogo'

    flor = Flores.objects.all()  # select * from flor
    return render(request, 'core/Galeria.html', {'listaflor': flor, 'msg': mensaje})


@login_required(login_url='/login/')
def galeria(request):
    """este comentario es para solucionar el missing doc string..."""
    flor = Flores.objects.all()  # select * from Flores
    return render(request, 'core/Galeria.html', {'listaflor': flor})


@login_required(login_url='/login/')
def formulario2(request):
    """este comentario es para solucionar el missing doc string..."""
    estados = Estado.objects.all()  # select from Categoria
    if request.POST:
        # recupero imagen desde formulario
        imagen = request.FILES.get("txImagen")
        nombre = request.POST.get("txtNombre")
        valor = request.POST.get("txtValor")
        descripcion = request.POST.get("txtDescripcion")
        estado = request.POST.get("cboEstado")
        # recupera el objeto con 'name' enviado desde el comboBox (cboEstado)
        obj_estado = Estado.objects.get(name=estado)
        stock = request.POST.get("txtStock")
        # Se crea una instancia de Flores(modelo)
        flores = Flores(
            imagen=imagen,
            name=nombre,
            valor=valor,
            descripcion=descripcion,
            estado=obj_estado,
            stock=stock
        )
        flores.save()  # graba objeto en bdd
        return render(request, 'core/Formulario2.html', {'lista': estados, 'msg': 'grabo', 'sw': True})
    # pasan los datos a la web
    return render(request, 'core/Formulario2.html', {'lista': estados})


@login_required(login_url='/login/')
def formulario(request):
    """este comentario es para solucionar el missing doc string..."""
    mensaje = ''
    buleano = False
    if request.POST:
        accion = request.POST.get("Accion")
        if accion == "Guardar":
            name = request.POST.get("txtEstado")
            est = Estado(
                name=name
            )
            est.save()
            mensaje = 'Grabo'
            buleano = True
        else: #accion == "Eliminar":
            name = request.POST.get("txtEstado")
            est = Estado.objects.get(name=name)
            est.delete()
            mensaje = "Elimino"
            buleano = True
    else:
        buleano = False

    estados = Estado.objects.all()  # select * from estado
    return render(request, 'core/Formulario.html', {'lista': estados, 'msg': mensaje, 'buleano': True})
