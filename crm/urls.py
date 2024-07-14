from django.urls import path
from .views import CrmView , CrmDetailView , DeleteCrmView


app_name = 'crm'

urlpatterns = [
    path('' , CrmView.as_view() , name='contact'),
    path('detail/<int:pk>/' , CrmDetailView.as_view(),name='detail'),
    path('detail/<int:pk>/delete/' , DeleteCrmView.as_view() , name='delete' )

]