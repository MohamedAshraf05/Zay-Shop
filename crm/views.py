from django.shortcuts import render ,redirect
from django.db.models import Q
from django.http import JsonResponse
from zayapp.models import Contact , Order , UserProfile , Products
from django.views.generic import ListView , UpdateView , DeleteView , DetailView , CreateView , FormView , View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import ProductsForm
# Create your views here.

class HomeView(ListView):
    queryset = Products.objects.all()
    template_name = "pages/crmhome.html"


class CrmView(LoginRequiredMixin,ListView):
    template_name = "pages/crm.html"
    context_object_name = 'customers'
    login_url = reverse_lazy('crm:login')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = query.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase
            print(f"Search Query: {query}")  # Debug print
            results = UserProfile.objects.filter(
                Q(user__username__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query)
            )
            print(f"Results Count: {results.count()}")  # Debug print
            return results
        return Contact.objects.all()
class CrmDetailView(LoginRequiredMixin , DetailView):
    queryset = Contact.objects.all()
    template_name = "pages/detail.html"
    context_object_name = "customersDetails"
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class DeleteCrmView(LoginRequiredMixin , DeleteView):
    model = Contact
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('crm:contact')
    context_object_name = 'contacts'


class Ordersview(LoginRequiredMixin , ListView):
    template_name = "pages/ordersAdmin.html"
    context_object_name = 'orders'
    login_url = reverse_lazy('crm:login')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = query.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase
            print(f"Search Query: {query}")  # Debug print
            results = Order.objects.filter(
                Q(user__user__username__icontains=query) |
                Q(product__name__icontains=query)|
                Q(product__price__icontains=query)
            )
            print(f"Results Count: {results.count()}")  # Debug print
            return results
        return Order.objects.all()
        
class UserListView(LoginRequiredMixin , ListView):
    template_name = "pages/userModel.html"
    context_object_name = 'users'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = query.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase
            print(f"Search Query: {query}")  # Debug print
            results = UserProfile.objects.filter(
                Q(user__username__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query) |
                Q(city__name__icontains=query)|
                Q(nationality__name__icontains=query)|
                Q(address__icontains=query)
            )
            print(f"Results Count: {results.count()}")  # Debug print
            return results
        return UserProfile.objects.all()
class ProductsListView(LoginRequiredMixin , ListView):
    template_name = "pages/productsAdmin.html"
    context_object_name = 'products'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = query.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase
            print(f"Search Query: {query}")  # Debug print
            results = Products.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query) |
                Q(category__name__iexact=query)
            )
            print(f"Results Count: {results.count()}")  # Debug print
            return results
        return Products.objects.all()
class ProductsCreateView(LoginRequiredMixin , FormView):
    template_name = "pages/create.html"
    form_class = ProductsForm
    success_url = reverse_lazy('crm:products')
    
    def form_valid(self , form):
        product = form.save(commit=False)
        product.added_by = self.request.user
        product.save()
        return super().form_valid(form)
    

class ProductsDetailView(LoginRequiredMixin , DetailView):
    queryset = Products.objects.all()
    template_name = 'pages/products-detail.html'
    context_object_name = 'product'