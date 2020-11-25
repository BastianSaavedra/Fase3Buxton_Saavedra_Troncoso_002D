from django.shortcuts import redirect
from catalog.models import PlacasMadre, Procesadore, Gpu, Ram
from django.contrib.auth.decorators import login_required
from .cart import Cart

# Create your views here.
@login_required(login_url="/registration/login")
def add_product(request, product_id):
   cart = Cart(request)
   product = PlacasMadre.objects.get(id=product_id)
   cart.add(product=product)
   return redirect("placamadre")

@login_required(login_url="/registration/login")
def remove_product(request, product_id):
   cart = Cart(request)
   product = PlacasMadre.objects.get(id=product_id)
   cart.remove(product)
   return redirect("placamadre")

@login_required(login_url="/registration/login")
def decrement_product(request, product_id):
   cart = Cart(request)
   product = PlacasMadre.objects.get(id=product_id)
   cart.decrement(product=product)
   return redirect("placamadre")

@login_required(login_url="/registration/login")
def clear_cart(request):
   cart = Cart(request)
   cart.clear()
   return redirect("placamadre")



# PROCESADOR
@login_required(login_url="/registration/login")
def add_procesador(request, product_id):
   cart = Cart(request)
   product = Procesadore.objects.get(id=product_id)
   cart.add(product=product)
   return redirect("procesador")

@login_required(login_url="/registration/login")
def remove_procesador(request, product_id):
   cart = Cart(request)
   product = Procesadore.objects.get(id=product_id)
   cart.remove(product)
   return redirect("procesador")

@login_required(login_url="/registration/login")
def decrement_procesador(request, product_id):
   cart = Cart(request)
   product = Procesadore.objects.get(id=product_id)
   cart.decrement(product=product)
   return redirect("procesador")

@login_required(login_url="/registration/login")
def clear_cart_procesador(request):
   cart = Cart(request)
   cart.clear()
   return redirect("procesador")

# GPU

@login_required(login_url="/registration/login")
def add_gpu(request, product_id):
   cart = Cart(request)
   product = Gpu.objects.get(id=product_id)
   cart.add(product=product)
   return redirect("video")

@login_required(login_url="/registration/login")
def remove_gpu(request, product_id):
   cart = Cart(request)
   product = Gpu.objects.get(id=product_id)
   cart.remove(product)
   return redirect("video")

@login_required(login_url="/registration/login")
def decrement_gpu(request, product_id):
   cart = Cart(request)
   product = Gpu.objects.get(id=product_id)
   cart.decrement(product=product)
   return redirect("video")

@login_required(login_url="/registration/login")
def clear_cart_gpu(request):
   cart = Cart(request)
   cart.clear()
   return redirect("video")

# RAM
@login_required(login_url="/registration/login")
def add_ram(request, product_id):
   cart = Cart(request)
   product = Ram.objects.get(id=product_id)
   cart.add(product=product)
   return redirect("rams")

@login_required(login_url="/registration/login")
def remove_ram(request, product_id):
   cart = Cart(request)
   product = Ram.objects.get(id=product_id)
   cart.remove(product)
   return redirect("rams")

@login_required(login_url="/registration/login")
def decrement_ram(request, product_id):
   cart = Cart(request)
   product = Ram.objects.get(id=product_id)
   cart.decrement(product=product)
   return redirect("rams")

@login_required(login_url="/registration/login")
def clear_cart_ram(request):
   cart = Cart(request)
   cart.clear()
   return redirect("rams")

