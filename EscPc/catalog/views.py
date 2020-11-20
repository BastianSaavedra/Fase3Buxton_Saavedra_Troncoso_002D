#!/usr/bin/python3
from django.shortcuts import render, redirect, get_object_or_404
from .models import PlacasMadre, Procesadore, Gpu, Ram, Almacenamiento,FuentesPoder, Gabinete, Monitore
from django.views.generic import ListView, DetailView
from .forms import PlacaForm, ContactoForm, ProceForm, GpuForm, RamForm, AlmacenamientoForm, FuentesPoderForm, GabineteForm, MonitoreForm
from django.contrib import messages


'''
   AQUI SE ENCUENTRAN LAS VISTAS DE LOS PRODUCTOS, AQUI UNO PUEDE SACAR LOS
   DATOS DE LOS MODELOS Y UTILIZARLOS PARA QUE CUMPLAN ALGUNA FUNCION,
   PRIMERO SE ENCUENTRAN UNOS "def" DONDE OBTENDRAN TODOS LOS OBJETOS DE
   CADA CLASE, LUEGO SE ENCUENTRAN LAS LISTAS DE LOS PRODUCTOS TANTO ListView
   COMO DetailVIEW, TAMBIEN SE ENCUENTRA EL CRUD DE CADA TIPO DE PRODUCTO DONDE ESTA EL CREAR, MODIFICAR Y ELIMINAR.
'''

def index(request):
   return render(request,'index.html',)


def placamadre(request):
   productoPlaca = PlacasMadre.objects.all()

   return render(
      request,
      'placasmadres.html',
      context={'productoPlaca':productoPlaca},
   )

def procesador(request):
   productoProce = Procesadore.objects.all()

   return render (
      request,
      'procesadores.html',
      context={'productoProce': productoProce},
   )

def video(request):
   productoGpu = Gpu.objects.all()

   return render (
      request,
      'tarjetadevideo.html',
      context={'productoGpu':productoGpu},
   )

def rams(request):
   productoRam = Ram.objects.all()

   return render(
      request,
      'ram.html',
      context={'productoRam':productoRam},
   )

def alma(request):
   productoAlmacenamiento = Almacenamiento.objects.all()

   return render(
      request,
      'almacenamiento.html',
      context={'productoAlmacenamiento':productoAlmacenamiento},
   )

def fuente(request):
   productoFuente = FuentesPoder.objects.all()

   return render(
      request,
      'fuenteDePoder.html',
      context={'productoFuente':productoFuente},
   )

def gabo(request):
   productoGabo = Gabinete.objects.all()

   return render(
      request,
      'gabinetes.html',
      context={'productoGabo':productoGabo},
   )

def moni(request):
   productoMoni = Monitore.objects.all()

   return render(
      request,
      'monitores.html',
      context={'productoMoni':productoMoni},
   )


class PlacaListView(ListView):
   model = PlacasMadre
   template_name = 'catalogo/PLacamadre/placasmadre_list.html'

class PlacaDetailView(DetailView):
   model = PlacasMadre
   template_name = 'catalogo/Placamadre/placasmadre_detail.html'


class ProceListView(ListView):
   model = Procesadore
   template_name = 'catalogo/Procesador/procesadore_list.html'

class ProceDetailView(DetailView):
   model = Procesadore
   template_name = 'catalogo/Procesador/procesadore_detail.html'


class GpuListView(ListView):
   model = Gpu
   template_name = 'catalogo/TargetaVideo/gpu_list.html'

class GpuDetailView(DetailView):
   model = Gpu
   template_name = 'catalogo/TargetaVideo/gpu_detail.html'


class RamListView(ListView):
   model = Ram
   template_name = 'catalogo/Ram/ram_list.html'

class RamDetailView(DetailView):
   model = Ram
   template_name = 'catalogo/Ram/ram_detail.html'

class AlmacenamientoListView(ListView):
   model = Almacenamiento
   template_name = 'catalogo/Almacenamiento/almacenamiento_list.html'

class AlmacenamientoDetailView(DetailView):
   model = Almacenamiento
   template_name = 'catalogo/Almacenamiento/almacenamiento_detail.html'

class FuentesPoderListView(ListView):
   model = FuentesPoder
   template_name = 'catalogo/FuentesPoder/fuentespoder_list.html'

class FuentesPoderDetailView(DetailView):
   model = FuentesPoder
   template_name = 'catalogo/FuentesPoder/fuentespoder_detail.html'

class GabineteListView(ListView):
   model = Gabinete
   template_name = 'catalogo/Gabinete/gabinete_list.html'

class GabineteDetailView(DetailView):
   model = Gabinete
   template_name = 'catalogo/Gabinete/gabinete_detail.html'

class MonitoreListView(ListView):
   model = Monitore
   template_name = 'catalogo/Monitor/monitore_list.html'

class MonitoreDetailView(DetailView):
   model = Monitore
   template_name = 'catalogo/Monitor/monitore_detail.html'


#CRUD PLACASMADRE
#AGREGAR PLACA
def nueva_placa(request):
   data = {
      'form':PlacaForm()
   }
   if request.method == 'POST':
      formulario = PlacaForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="placas")
   return render(request, 'catalogo/Placamadre/nueva_placa.html', data)
#MODIFICAR PLACA

def modificar_placa(request, id):
   placa = get_object_or_404(PlacasMadre, id=id)
   data = {
      'form':PlacaForm(instance=placa)
   }
   if request.method == 'POST':
      formulario = PlacaForm(data=request.POST, instance=placa, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="placas")
      data["form"] = formulario
   return render(request,'catalogo/Placamadre/modificar_placa.html', data)
#ELIMINAR PLACA

def eliminar_placa(request, id):
   placa = get_object_or_404(PlacasMadre, id=id)
   placa.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="placas")

#CRUD PROCESADOR
#AGREGAR PROCESADOR
def nuevo_procesador(request):
   data = {
      'proceform':ProceForm()
   }
   if request.method == 'POST':
      formulario = ProceForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="procesadores")
   return render(request, 'catalogo/Procesador/nuevo_procesador.html', data)
#MODICIAR PROCESDOR
def modicar_procesador(request, id):
   proce = get_object_or_404(Procesadore, id=id)
   data = {
      'proceform':ProceForm(instance=proce)
   }
   if request.method == 'POST':
      formulario = ProceForm(data=request.POST, instance=proce, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "producto modificado exitosamente!")
         return redirect(to="procesadores")
      data["proceform"] = formulario
   return render(request, 'catalogo/Procesador/modificar_procesador.html', data)
#ELIMINAR PROCESADOR
def eliminar_procesador(request, id):
   proce = get_object_or_404(Procesadore, id=id)
   proce.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="procesadores")

#CRUD Gpu
def nuevo_gpu(request):
   data = {
      'gpuForm':GpuForm()
   }
   if request.method == 'POST':
      formulario = GpuForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="gpus")
   return render(request, 'catalogo/TargetaVideo/nueva_gpu.html', data)

def modificar_gpu(request, id):
   video = get_object_or_404(Gpu, id=id)
   data = {
      'gpuForm':GpuForm(instance=video)
   }
   if request.method == 'POST':
      formulario  = GpuForm(data=request.POST, instance=video,
      files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="gpus")
      data["gpuForm"] = formulario
   return render(request, 'catalogo/TargetaVideo/modificar_gpu.html', data)

def eliminar_gpu(request, id):
   video = get_object_or_404(Gpu, id=id)
   video.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="gpus")

#CRUD RAM
def nueva_ram(request):
   data = {
      'ramForm': RamForm()
   }
   if request.method == 'POST':
      formulario = RamForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="memoriasram")
   return render(request, 'catalogo/Ram/nueva_ram.html', data)

def modificar_ram(request):
   ram = get_object_or_404(Ram, id=id)
   data = {
      'ramForm' : RamForm(instance=ram)
   }
   if request.method == 'POST':
      formulario = RamForm(data=request.POST, instance=ram, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="memoriasram")
      data["ramForm"] = formulario
   return render(request, 'catalogo/Ram/modificar_ram.html', data)

def eliminar_ram(request):
   ram = get_object_or_404(Ram, id=id)
   ram.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="memoriasram")

#CRUD ALMACENAMIENTO
def nuevo_almacenamiento(request):
   data = {
      'almacenamientoForm' : AlmacenamientoForm()
   }
   if request.method == 'POST':
      formulario = AlmacenamientoForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="almacenamientos")
   return render(request, 'catalogo/Almacenamiento/nuevo_almacenamiento.html', data)

def modificar_almacenamiento(request):
   almacenamiento = get_object_or_404(Almacenamiento, id=id)
   data = {
      'almacenamientoForm' : AlmacenamientoForm(instance=almacenamiento)
   }
   if request.method == 'POST':
      formulario = AlmacenamientoForm(data=request.POST, instance=almacenamiento, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="almacenamientos")
      data["almacenamientoForm"] = formulario
   return render(request, 'catalogo/Almacenamiento/modificar_almacenamiento.html', data)

def eliminar_almacenamiento(request):
   almacenamiento = get_object_or_404(Almacenamiento, id=id)
   almacenamiento.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="almacenamientos")

#CRUD FUENTES DE PODER
def nueva_fuente(request):
   data = {
      'fuenteForm': FuentesPoderForm()
   }
   if request.method == 'POST':
      formulario = FuentesPoderForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto ingresado exitosamente!")
         return redirect(to="fuentes")
   return render(request, 'catalogo/FuentesPoder/nueva_fuente.html', data)

def modificar_fuente(request):
   fuente = get_object_or_404(FuentesPoder, id=id)
   data = {
      'fuenteForm': FuentesPoderForm(instance=fuente)
   }
   if request.method == 'POST':
      formulario = FuentesPoderForm(data=request.POST, instance=fuente, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="fuentes")
      data["fuenteForm"] = formulario
   return render(request, 'catalogo/FuentesPoder/modificar_fuente.html', data)

def eliminar_fuente(request):
   fuente = get_object_or_404(FuentesPoder, id=id)
   fuente.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="fuentes")

#CRUD GABINETE
def nuevo_gabinete(request):
   data = {
      'gabineteForm' : GabineteForm()
   }
   if request.method == 'POST':
      formulario = GabineteForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto se ingreso exitosamente!")
         return redirect(to="gabinetes")
   return render(request, 'catalogo/Gabinete/nuevo_gabinete.html', data)

def modificar_gabinete(request):
   gabinete = get_object_or_404(Gabinete, id=id)
   data = {
      'gabineteForm' : GabineteForm(instance=gabinete)
   }
   if request.method == 'POST':
      formulario = GabineteForm(data=request.POST, instance=gabinete, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="gabinetes")
      data["gabineteForm"] = formulario
   return render(request, 'catalogo/Gabinete/modificar_gabinete.html', data)

def eliminar_gabinete(request):
   gabinete = get_object_or_404(Gabinete, id=id)
   gabinete.delete()
   messages.success(request, "Producto eliminado exitosamente!")
   return redirect(to="gabinetes")

#CRUD MONITOR
def nuevo_monitor(request):
   data = {
      'monitorForm': MonitoreForm()
   }
   if request.method == 'POST':
      formulario = MonitoreForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto se ingreso exitosamente!")
         return redirect(to="monitores")
   return render(request, 'catalogo/Monitor/nuevo_monitor.html', data)

def modificar_monitor(request):
   monitor = get_object_or_404(Monitore, id=id)
   data = {
      'monitorForm': MonitoreForm(instance=monitor)
   }
   if request.method == 'POST':
      formulario = MonitoreForm(data=request.POST, instance=monitor, files=request.FILES)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Producto modificado exitosamente!")
         return redirect(to="monitores")
      data["monitorForm"] = formulario
   return render(request, 'catalogo/Monitor/modificar_monitor.html', data)

def eliminar_monitor(request):
   monitor = get_object_or_404(Monitore, id=id)
   monitor.delete()
   messages.success(request, "Produto eliminado exitosamente!")
   return redirect(to="monitores")

#CONTACTO
def contacto(request):
   data = {
      'contactoform':ContactoForm()
   }
   if request.method == 'POST':
      formulario = ContactoForm(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         messages.success(request, "Mensaje enviado exitosamente!")
      else:
         data["contactoform"] = formulario
   return render(request, 'contacto.html', data)
