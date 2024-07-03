from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import login  , logout , authenticate
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView , FormView
from .models import Products , Category , Season , CartItem , Cart , City 
from django.contrib.auth.forms import UserCreationForm
 
# Create your views here.

class HomeView(ListView):
    queryset = Products.objects.all()
    template_name = 'pages/home.html'
    context_object_name = 'product'


class ProductView(ListView):
    queryset = Products.objects.all()
    context_object_name = 'products'
    template_name = 'pages/products.html'

class SingleProduct(DetailView):
    queryset = Products.objects.all()
    context_object_name = 'product'
    template_name = 'pages/single-product.html'
    
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Products, pk=kwargs['pk'])
        cart,created = Cart.objects.get_or_create(user=request.user)

        size = request.POST.get('product-size')
        quantity = int(request.POST.get('product-quantity', 1))

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        # Update the total items in the cart
        cart.update_total_items()

        if request.POST.get('submit') == 'buy':
            # Handle the buying process
            return redirect('zay:home')
        else:
            # Add to cart and redirect to cart detail
            print(f"The product added , with quantity {cart_item.quantity}") # Debugging print
            return redirect('zay:shop')
    


class CartDetailView(DetailView):
    model = Cart
    template_name = 'pages/cart_detail.html'  # #new
    context_object_name = 'cart'  # #new

    def get_object(self, queryset=None):
        return get_object_or_404(Cart, user=self.request.user)
    


class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'pages/cart_delete.html'  # #new

    def get_success_url(self):
        return reverse_lazy('zay:cart')  # #new

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'pages/cart_delete.html'

    def get_success_url(self):
        return reverse_lazy('zay:cart')
    
class MenView(ListView):
    queryset = Products.objects.all().filter(category=2)
    template_name = 'pages/men.html'
    context_object_name = 'men'


class WomenView(ListView):
    queryset = Products.objects.all().filter(category=3)
    template_name = 'pages/women.html'
    context_object_name = 'women'
    
    
class CustomerLoginView(LoginView):
    template_name = 'pages/login.html'
    fields = "__all__"
    success_url = reverse_lazy('zay:home')

    def get_success_url(self):
        return reverse_lazy('zay:home')
    def form_valid(self, form):
        print("Form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CustomerRegisterView(FormView):
    template_name = 'pages/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("zay:login")
    
    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(CustomerRegisterView , self).form_valid(form)
    def get(self,*args,**kwargs ):
        if self.request.user.is_authenticated :
            return redirect('zay:login')
        return super(CustomerRegisterView , self ).get(*args,**kwargs)
    def form_invalid(self,form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


def Logout(request):
    logout(request)
    return redirect('zay:login')