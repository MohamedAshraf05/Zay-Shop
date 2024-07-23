from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth.models import User
from django.contrib.auth import login  , logout , authenticate
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView , FormView
from .models import Products , Category , Season , CartItem , Cart , City , UserProfile , Order
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm , ContactForm
from django.contrib import messages
# Create your views here.

class HomeView(ListView):
    queryset = Products.objects.all()
    template_name = 'pages/home.html'
    context_object_name = 'product'

class AboutView(ListView):
    queryset = Products.objects.all()
    template_name = 'pages/about.html'

class ProductView(ListView):
    queryset = Products.objects.all()
    template_name = 'pages/products.html'
    context_object_name = 'products'
    paginate_by = 6
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Products.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query) 
            )
        return Products.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists() and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Product not found'}, status=404)
        paginator = Paginator(queryset, self.paginate_by)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        return render(request, self.template_name, {'products': products})

class SingleProduct(DetailView):
    queryset = Products.objects.all()
    context_object_name = 'product'
    template_name = 'pages/single-product.html'
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('submit') == 'addtocart':
            if not request.user.is_authenticated:
                messages.error(request, "You need to be logged in to perform this action.")
                return redirect(reverse("zay:login") + "?message=You need to be logged in to perform this action.")

            product = get_object_or_404(Products, pk=kwargs['pk'])
            cart, created = Cart.objects.get_or_create(user=request.user)

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
            
            messages.success(request, f"{product} is added successfully with quantity {quantity} ")
            return redirect(reverse("zay:cart") + f"?message={product} is added successfully with quantity {quantity} ")
        elif request.POST.get('submit') == 'buy':
            product = get_object_or_404(Products, pk=kwargs['pk'])
            size = request.POST.get('product-size')
            quantity = int(request.POST.get('product-quantity', 1))
            user_profile = UserProfile.objects.filter(user=request.user).first()
            
            if not user_profile or not user_profile.city or not user_profile.phone or not user_profile.address or not user_profile.nationality:
                messages.error(request, "Please complete your profile information before purchasing.")
                return redirect('zay:form')
            order, created = Order.objects.get_or_create(user=user_profile, product=product, size=size, quantity=quantity)
            order.save()
        return super().get(request, *args, **kwargs)
class CartDetailView(DetailView):
    model = Cart
    template_name = 'pages/cart_detail.html'  # #new
    context_object_name = 'cart'  # #new

    def get_object(self, queryset=None):
        return get_object_or_404(Cart, user=self.request.user)        


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
    success_url = reverse_lazy("zay:form")
    
    def form_valid(self, form):
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

class UserProfileFormView(FormView):
    template_name = 'pages/form.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('zay:home')

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user_profile.user = self.request.user
        user_profile.save()
        return super().form_valid(form)
    

class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('zay:home')

    def form_valid(self , form):
        contact = form.save(commit=False)
        contact.user = self.request.user
        contact.save()
        return super().form_valid(form)
    
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'pages/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
    
    def get(self , request , *args , **kwargs):
        user_profile = UserProfile.objects.filter(user=request.user).first()
        
        if not user_profile or not user_profile.city or not user_profile.phone or not user_profile.address or not user_profile.nationality:
            messages.error(request, "Please complete your profile information before purchasing.")
            return redirect(reverse("zay:form") + "?message=Please complete your profile information first.")

        if not request.user.is_authenticated:
            messages.info(request , "You need to be registered and logged in to view your profile")
            return redirect('zay:login')
        
        return super().get(request, *args, **kwargs)

class UserProfileUpdateView(LoginRequiredMixin , UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'pages/profile_update.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('zay:profile')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)


def Logout(request):
    logout(request)
    return redirect('zay:login')
