from django.shortcuts import render ,redirect
from zayapp.models import Contact
from django.views.generic import ListView , UpdateView , DeleteView , DetailView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class CrmView(LoginRequiredMixin,ListView):
    queryset = Contact.objects.all()
    template_name = "pages/crm.html"
    context_object_name = 'customers'
    login_url = reverse_lazy('crm:login')

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
