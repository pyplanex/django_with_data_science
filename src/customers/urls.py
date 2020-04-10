from django.urls import path
from .views import customer_corr_view

app_name = 'customers'

urlpatterns = [
    path('', customer_corr_view, name='main-customers-view'),
]